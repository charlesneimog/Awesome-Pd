#!/usr/bin/env python3
"""Research and enrich library JSON files with the Codex CLI and live web search.

Each library is researched independently. Successful results are saved immediately,
and a ``research`` block records confidence and evidence URLs so uncertain or missing
results are distinguishable from libraries that have not been checked yet.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_TIMEOUT = 600
DEFAULT_RETRIES = 2

RESULT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "description": {"type": "string"},
        "repository_url": {"type": "string"},
        "issues_url": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "sources": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "string"},
    },
    "required": [
        "description",
        "repository_url",
        "issues_url",
        "confidence",
        "sources",
        "notes",
    ],
    "additionalProperties": False,
}


def is_http_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def normalize_url(value: str) -> str:
    value = value.strip()
    if value.endswith(".git"):
        value = value[:-4]
    return value.rstrip("/")


def research_prompt(library: str) -> str:
    return f"""Research this Pure Data (Pd) library using live web search.

Find the canonical project repository, preferably its official GitHub or GitLab
repository, its issue tracker when one exists, and enough authoritative evidence
to write a simple factual description of one or two sentences.

Search using combinations of the exact library name, "Pure Data", "Pd external",
"Deken", GitHub, and GitLab. Resolve name collisions using public evidence.
Prefer official repositories, project websites, Deken pages, and maintainer pages
over aggregators or mirrors.

Rules:
- Never guess a URL or project identity.
- Use an empty string when a repository or issue tracker cannot be verified.
- The description must be plain English and supported by the sources.
- `sources` must contain the authoritative pages used to verify the result.
- Use high confidence only for a clearly verified official project.
- Return only the JSON required by the output schema.

Library name: {library}
"""


def validate_result(value: dict) -> dict:
    if not isinstance(value, dict):
        raise ValueError("Codex output is not a JSON object")
    required = set(RESULT_SCHEMA["required"])
    if set(value) != required:
        raise ValueError(f"unexpected result fields: {sorted(set(value) ^ required)}")
    for field in ("description", "repository_url", "issues_url", "notes"):
        if not isinstance(value[field], str):
            raise ValueError(f"{field} is not a string")
        value[field] = value[field].strip()
    if value["confidence"] not in {"high", "medium", "low"}:
        raise ValueError("invalid confidence")
    if not isinstance(value["sources"], list) or not all(
        isinstance(source, str) for source in value["sources"]
    ):
        raise ValueError("sources is not a string array")

    for field in ("repository_url", "issues_url"):
        if value[field] and not is_http_url(value[field]):
            raise ValueError(f"invalid {field}: {value[field]!r}")
        value[field] = normalize_url(value[field]) if value[field] else ""
    sources = []
    for source in value["sources"]:
        source = normalize_url(source)
        if not is_http_url(source):
            raise ValueError(f"invalid source URL: {source!r}")
        if source not in sources:
            sources.append(source)
    value["sources"] = sources
    if any(value[field] for field in ("description", "repository_url", "issues_url")):
        if not sources:
            raise ValueError("a non-empty result requires at least one evidence URL")
    if len(value["description"]) > 800:
        raise ValueError("description is longer than 800 characters")
    return value


def run_codex(
    prompt: str,
    codex_bin: str,
    model: str | None,
    timeout: int,
    work_dir: Path,
) -> dict:
    schema_path = work_dir / "library.schema.json"
    output_path = work_dir / "last-message.json"
    schema_path.write_text(json.dumps(RESULT_SCHEMA), encoding="utf-8")
    output_path.unlink(missing_ok=True)
    command = [
        codex_bin,
        "--search",
        "exec",
        "--ephemeral",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(output_path),
        "--cd",
        str(work_dir),
    ]
    if model:
        command.extend(["--model", model])
    command.append("-")
    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip().splitlines()
        message = detail[-1] if detail else "no error message"
        raise RuntimeError(f"Codex exited with {completed.returncode}: {message}")
    return validate_result(json.loads(output_path.read_text(encoding="utf-8")))


def research_status(result: dict) -> str:
    if result["description"] and result["repository_url"]:
        return "verified" if result["confidence"] != "low" else "partial"
    if any(result[field] for field in ("description", "repository_url", "issues_url")):
        return "partial"
    return "not_found"


def apply_result(current: dict, result: dict, overwrite: bool) -> dict:
    updated = dict(current)
    values = {
        "description": result["description"],
        "link": result["repository_url"],
        "issues": result["issues_url"],
    }
    for field, value in values.items():
        if overwrite or not str(updated.get(field, "")).strip():
            updated[field] = value
    updated["research"] = {
        "status": research_status(result),
        "confidence": result["confidence"],
        "sources": result["sources"],
        "notes": result["notes"],
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    return updated


def atomic_write_json(path: Path, data: dict) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    temporary = path.with_name(f".{path.name}.tmp")
    try:
        temporary.write_text(
            json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        temporary.chmod(mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def is_complete(data: dict) -> bool:
    return all(str(data.get(field, "")).strip() for field in ("description", "link"))


def select_libraries(
    libraries_dir: Path,
    patterns: list[str],
    overwrite: bool,
    retry_partial: bool,
) -> list[tuple[Path, dict]]:
    selected = []
    for path in sorted(libraries_dir.glob("*.json"), key=lambda item: item.name.casefold()):
        name = path.stem
        if patterns and not any(fnmatch.fnmatch(name, pattern) for pattern in patterns):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: cannot read {path}: {exc}", file=sys.stderr)
            continue
        status = data.get("research", {}).get("status")
        if overwrite or (retry_partial and status in {"partial", "not_found"}):
            selected.append((path, data))
        elif status or is_complete(data):
            continue
        else:
            selected.append((path, data))
    return selected


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--libraries-dir", type=Path, default=Path("docs/libraries")
    )
    parser.add_argument(
        "--library",
        action="append",
        default=[],
        metavar="GLOB",
        help="research matching library names; repeat for multiple patterns",
    )
    parser.add_argument("--limit", type=int, help="maximum libraries to research")
    parser.add_argument("--model", help="optional Codex model override")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--overwrite", action="store_true", help="replace existing metadata"
    )
    parser.add_argument(
        "--retry-partial",
        action="store_true",
        help="research libraries previously marked partial or not found",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="list candidates without calling Codex"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.timeout < 1 or args.retries < 0:
        print("Error: timeout must be positive and retries cannot be negative", file=sys.stderr)
        return 2
    libraries_dir = args.libraries_dir.expanduser().resolve()
    if not libraries_dir.is_dir():
        print("Error: libraries directory does not exist", file=sys.stderr)
        return 2
    if not args.dry_run and shutil.which(args.codex_bin) is None:
        print(f"Error: `{args.codex_bin}` CLI was not found in PATH", file=sys.stderr)
        return 2

    candidates = select_libraries(
        libraries_dir, args.library, args.overwrite, args.retry_partial
    )
    if args.limit is not None:
        candidates = candidates[: max(0, args.limit)]
    print(
        f"Found {len(candidates)} "
        f"{'library' if len(candidates) == 1 else 'libraries'} to research."
    )
    if args.dry_run:
        for path, _data in candidates:
            print(f"  {path.stem}")
        return 0
    if not candidates:
        return 0

    completed_count = failed_count = 0
    with tempfile.TemporaryDirectory(prefix="enrich-libraries-") as temporary:
        work_dir = Path(temporary)
        for number, (path, data) in enumerate(candidates, 1):
            library = path.stem
            prompt = research_prompt(library)
            print(f"[{number}/{len(candidates)}] Researching {library}...")
            result = None
            for attempt in range(args.retries + 1):
                try:
                    result = run_codex(
                        prompt, args.codex_bin, args.model, args.timeout, work_dir
                    )
                    break
                except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
                    print(
                        f"  Attempt {attempt + 1}/{args.retries + 1} failed: {exc}",
                        file=sys.stderr,
                    )
            if result is None:
                failed_count += 1
                continue
            updated = apply_result(data, result, args.overwrite)
            atomic_write_json(path, updated)
            print(
                f"  {updated['research']['status']} ({result['confidence']}): "
                f"{updated.get('link') or 'no repository found'}"
            )
            completed_count += 1

    print(f"Done: {completed_count} researched, {failed_count} failed")
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
