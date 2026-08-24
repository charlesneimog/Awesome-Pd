#!/usr/bin/env python3
"""Research and enrich Pure Data library JSON files with the Codex CLI.

Libraries are researched in batches using Codex and live web research.
Successful results are saved after every batch, and a ``research`` block records
confidence and evidence URLs so interrupted runs can resume safely.
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
DEFAULT_RETRIES = 1
DEFAULT_BATCH_SIZE = 8
DEFAULT_EFFORT = "low"


RESULT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "description": {
            "type": "string",
        },
        "repository_url": {
            "type": "string",
        },
        "issues_url": {
            "type": "string",
        },
        "confidence": {
            "type": "string",
            "enum": [
                "high",
                "medium",
                "low",
            ],
        },
        "sources": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
        "notes": {
            "type": "string",
        },
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


def batch_result_schema(libraries: list[str]) -> dict:
    """Return a compact schema that requires one result per library."""
    item_properties = {
        "library": {"type": "string", "enum": libraries},
        **RESULT_SCHEMA["properties"],
    }
    return {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "minItems": len(libraries),
                "maxItems": len(libraries),
                "items": {
                    "type": "object",
                    "properties": item_properties,
                    "required": ["library", *RESULT_SCHEMA["required"]],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["results"],
        "additionalProperties": False,
    }


def research_prompt(batch: list[tuple[Path, dict]]) -> str:
    libraries = []
    for path, data in batch:
        item = {"library": path.stem}
        existing = {
            key: str(data.get(key, "")).strip()
            for key in ("description", "link", "issues")
            if str(data.get(key, "")).strip()
        }
        if existing:
            item["existing_hints"] = existing
        libraries.append(item)

    return f"""Research every listed Pure Data (Pd) library with live web search.
Find its canonical repository, issue tracker, and a factual 1-2 sentence
description. Search the exact name with terms such as Pure Data, Pd external,
Deken, GitHub, or GitLab. Resolve name collisions with public evidence.

Prefer official repositories/sites, then Deken/Pure Data or maintainer pages.
Never guess identity or URLs. Use empty strings for unverified fields. Sources
must be URLs actually used. Confidence is high only for a clearly verified
official project, medium for likely identity, and low for weak evidence. Return
every library exactly once and preserve its name. Do not modify files or run
shell commands.

Libraries: {json.dumps(libraries, separators=(",", ":"), ensure_ascii=False)}
"""


def validate_result(value: dict) -> dict:
    if not isinstance(value, dict):
        raise ValueError("Codex output is not a JSON object")

    required = set(RESULT_SCHEMA["required"])

    if set(value) != required:
        unexpected = sorted(set(value) ^ required)

        raise ValueError(f"unexpected result fields: {unexpected}")

    for field in (
        "description",
        "repository_url",
        "issues_url",
        "notes",
    ):
        if not isinstance(
            value[field],
            str,
        ):
            raise ValueError(f"{field} is not a string")

        value[field] = value[field].strip()

    if value["confidence"] not in {
        "high",
        "medium",
        "low",
    }:
        raise ValueError("invalid confidence")

    if not isinstance(
        value["sources"],
        list,
    ) or not all(isinstance(source, str) for source in value["sources"]):
        raise ValueError("sources is not a string array")

    for field in (
        "repository_url",
        "issues_url",
    ):
        if value[field]:
            if not is_http_url(value[field]):
                raise ValueError(f"invalid {field}: " f"{value[field]!r}")

            value[field] = normalize_url(value[field])
        else:
            value[field] = ""

    sources: list[str] = []

    for source in value["sources"]:
        source = normalize_url(source)

        if not is_http_url(source):
            raise ValueError(f"invalid source URL: " f"{source!r}")

        if source not in sources:
            sources.append(source)

    value["sources"] = sources

    if any(
        value[field]
        for field in (
            "description",
            "repository_url",
            "issues_url",
        )
    ):
        if not sources:
            raise ValueError(
                "a non-empty result " "requires at least one " "evidence URL"
            )

    if len(value["description"]) > 800:
        raise ValueError("description is longer " "than 800 characters")

    return value


def validate_batch_result(value: dict, libraries: list[str]) -> dict[str, dict]:
    if not isinstance(value, dict) or set(value) != {"results"}:
        raise ValueError("Codex output has no results array")
    rows = value["results"]
    if not isinstance(rows, list):
        raise ValueError("Codex results is not an array")

    expected = set(libraries)
    results: dict[str, dict] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("batch result is not an object")
        library = row.get("library")
        if library not in expected:
            raise ValueError(f"unexpected library: {library!r}")
        if library in results:
            raise ValueError(f"duplicate library: {library!r}")
        result = dict(row)
        del result["library"]
        results[library] = validate_result(result)

    missing = expected - results.keys()
    if missing:
        raise ValueError(f"missing libraries: {sorted(missing)}")
    return results


def run_codex(
    prompt: str,
    schema: dict,
    codex_bin: str,
    model: str | None,
    effort: str,
    timeout: int,
    work_dir: Path,
) -> dict:
    """Run Codex headlessly and return its structured final message."""

    schema_path = work_dir / "library-batch.schema.json"
    output_path = work_dir / "last-message.json"
    schema_path.write_text(
        json.dumps(schema, separators=(",", ":")), encoding="utf-8"
    )
    output_path.unlink(missing_ok=True)

    command = [
        codex_bin,
        "--search",
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(output_path),
        "--cd",
        str(work_dir),
        "--config",
        f'model_reasoning_effort="{effort}"',
    ]

    if model:
        command.extend(
            [
                "--model",
                model,
            ]
        )

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
    if not output_path.is_file():
        raise RuntimeError("Codex returned no final message")
    try:
        result = json.loads(output_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("Codex final message is not valid JSON") from exc
    if not isinstance(result, dict):
        raise ValueError("Codex structured output is not a JSON object")
    return result


def research_status(
    result: dict,
) -> str:
    if result["description"] and result["repository_url"]:
        if result["confidence"] == "low":
            return "partial"

        return "verified"

    if any(
        result[field]
        for field in (
            "description",
            "repository_url",
            "issues_url",
        )
    ):
        return "partial"

    return "not_found"


def apply_result(
    current: dict,
    result: dict,
    overwrite: bool,
) -> dict:
    updated = dict(current)

    values = {
        "description": (result["description"]),
        "link": (result["repository_url"]),
        "issues": (result["issues_url"]),
    }

    for field, value in values.items():
        if (
            overwrite
            or not str(
                updated.get(
                    field,
                    "",
                )
            ).strip()
        ):
            updated[field] = value

    updated["research"] = {
        "status": (research_status(result)),
        "confidence": (result["confidence"]),
        "sources": (result["sources"]),
        "notes": (result["notes"]),
        "checked_at": (datetime.now(timezone.utc).isoformat(timespec="seconds")),
    }

    return updated


def atomic_write_json(
    path: Path,
    data: dict,
) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)

    temporary = path.with_name(f".{path.name}.tmp")

    try:
        temporary.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

        temporary.chmod(mode)

        os.replace(
            temporary,
            path,
        )

    finally:
        temporary.unlink(missing_ok=True)


def is_complete(
    data: dict,
) -> bool:
    return all(
        str(
            data.get(
                field,
                "",
            )
        ).strip()
        for field in (
            "description",
            "link",
        )
    )


def select_libraries(
    libraries_dir: Path,
    patterns: list[str],
    overwrite: bool,
    retry_partial: bool,
) -> list[tuple[Path, dict]]:
    selected: list[tuple[Path, dict]] = []

    paths = sorted(
        libraries_dir.glob("*.json"),
        key=lambda item: (item.name.casefold()),
    )

    for path in paths:
        name = path.stem

        if patterns and not any(
            fnmatch.fnmatch(
                name,
                pattern,
            )
            for pattern in patterns
        ):
            continue

        try:
            data = json.loads(path.read_text(encoding="utf-8"))

        except (
            OSError,
            json.JSONDecodeError,
        ) as exc:
            print(
                f"Warning: cannot read " f"{path}: {exc}",
                file=sys.stderr,
            )

            continue

        status = data.get(
            "research",
            {},
        ).get("status")

        if overwrite:
            selected.append((path, data))
            continue

        if retry_partial and status in {
            "partial",
            "not_found",
        }:
            selected.append((path, data))
            continue

        if status or is_complete(data):
            continue

        selected.append((path, data))

    return selected


def batches(items: list, size: int):
    for start in range(0, len(items), size):
        yield items[start : start + size]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
    )

    parser.add_argument(
        "--libraries-dir",
        type=Path,
        default=Path("docs/libraries"),
    )

    parser.add_argument(
        "--library",
        action="append",
        default=[],
        metavar="GLOB",
        help=("research matching library " "names; repeat for multiple " "patterns"),
    )

    parser.add_argument(
        "--limit",
        type=int,
        help=("maximum number of libraries " "to research"),
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=(
            "libraries per Codex request "
            f"(default: {DEFAULT_BATCH_SIZE}; use 1 for legacy behavior)"
        ),
    )

    parser.add_argument(
        "--model",
        help="optional Codex model override",
    )

    parser.add_argument(
        "--effort",
        choices=("low", "medium", "high"),
        default=DEFAULT_EFFORT,
        help=f"reasoning effort (default: {DEFAULT_EFFORT})",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=("maximum seconds for each " "Codex request"),
    )

    parser.add_argument(
        "--retries",
        type=int,
        default=DEFAULT_RETRIES,
        help=("number of retries after " "a failed request"),
    )

    parser.add_argument(
        "--codex-bin",
        default="codex",
        help="Codex CLI executable (default: codex)",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help=("replace existing metadata " "with researched values"),
    )

    parser.add_argument(
        "--retry-partial",
        action="store_true",
        help=("research libraries previously " "marked partial or not found"),
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=("list candidates without " "calling Codex"),
    )

    return parser


def main(
    argv: list[str] | None = None,
) -> int:
    args = build_parser().parse_args(argv)

    if args.batch_size < 1 or args.timeout < 1 or args.retries < 0:
        print(
            "Error: batch size and timeout must be positive; "
            "retries cannot be negative",
            file=sys.stderr,
        )

        return 2

    if args.limit is not None and args.limit < 0:
        print(
            "Error: limit cannot be negative",
            file=sys.stderr,
        )

        return 2

    libraries_dir = args.libraries_dir.expanduser().resolve()

    if not libraries_dir.is_dir():
        print(
            "Error: libraries directory " f"does not exist: " f"{libraries_dir}",
            file=sys.stderr,
        )

        return 2

    if not args.dry_run and shutil.which(args.codex_bin) is None:
        print(
            f"Error: `{args.codex_bin}` " "was not found in PATH",
            file=sys.stderr,
        )

        return 2

    candidates = select_libraries(
        libraries_dir,
        args.library,
        args.overwrite,
        args.retry_partial,
    )

    if args.limit is not None:
        candidates = candidates[: args.limit]

    count = len(candidates)

    print(
        f"Found {count} " f"{'library' if count == 1 else 'libraries'} " "to research."
    )

    if args.dry_run:
        for path, _data in candidates:
            print(f"  {path.stem}")

        return 0

    if not candidates:
        return 0

    completed_count = failed_count = 0
    batch_list = list(batches(candidates, args.batch_size))

    with tempfile.TemporaryDirectory(prefix="enrich-libraries-") as temporary:
        work_dir = Path(temporary)
        for number, batch in enumerate(batch_list, 1):
            libraries = [path.stem for path, _data in batch]
            prompt = research_prompt(batch)
            schema = batch_result_schema(libraries)
            noun = "library" if len(batch) == 1 else "libraries"
            print(
                f"[{number}/{len(batch_list)}] Researching {len(batch)} {noun}: "
                f"{', '.join(libraries)}..."
            )

            results: dict[str, dict] | None = None

            for attempt in range(args.retries + 1):
                try:
                    raw_result = run_codex(
                        prompt=prompt,
                        schema=schema,
                        codex_bin=args.codex_bin,
                        model=args.model,
                        effort=args.effort,
                        timeout=args.timeout,
                        work_dir=work_dir,
                    )
                    results = validate_batch_result(raw_result, libraries)

                    break

                except KeyboardInterrupt:
                    print(
                        "\nInterrupted.",
                        file=sys.stderr,
                    )

                    return 130

                except subprocess.TimeoutExpired:
                    print(
                        f"  Attempt "
                        f"{attempt + 1}/"
                        f"{args.retries + 1} "
                        f"failed: timeout",
                        file=sys.stderr,
                    )

                except (
                    OSError,
                    ValueError,
                    RuntimeError,
                ) as exc:
                    print(
                        f"  Attempt "
                        f"{attempt + 1}/"
                        f"{args.retries + 1} "
                        f"failed: {exc}",
                        file=sys.stderr,
                    )

            if results is None:
                failed_count += len(batch)
                continue

            for path, data in batch:
                result = results[path.stem]
                updated = apply_result(data, result, args.overwrite)
                try:
                    atomic_write_json(path, updated)
                except OSError as exc:
                    print(f"  Failed to write {path}: {exc}", file=sys.stderr)
                    failed_count += 1
                    continue
                print(
                    f"  {path.stem}: {updated['research']['status']} "
                    f"({result['confidence']}): "
                    f"{updated.get('link') or 'no repository found'}"
                )
                completed_count += 1

    print(f"Done: " f"{completed_count} researched, " f"{failed_count} failed")

    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
