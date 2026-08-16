#!/usr/bin/env python3
"""Categorize imported Deken objects with the Codex CLI.

Only Deken-derived JSON records with an empty ``categories`` list are selected.
Successful batches are saved immediately, so rerunning the script safely resumes
after the last completed object.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable


DEFAULT_BATCH_SIZE = 50
DEFAULT_TIMEOUT = 600
DEFAULT_RETRIES = 2


def category_paths(model: dict, parents: tuple[str, ...] = ()) -> dict[str, str]:
    """Return leaf category names mapped to human-readable taxonomy paths."""
    paths: dict[str, str] = {}
    for name, children in model.items():
        current = (*parents, name)
        if isinstance(children, dict):
            descendants = category_paths(children, current)
            duplicates = paths.keys() & descendants.keys()
            if duplicates:
                raise ValueError(f"duplicate leaf categories: {sorted(duplicates)}")
            paths.update(descendants)
        elif isinstance(children, list):
            paths[name] = " > ".join(current)
        else:
            raise ValueError(f"invalid taxonomy value for {name!r}")
    return paths


def load_candidates(objects_dir: Path, include_all_empty: bool) -> list[tuple[Path, dict]]:
    candidates: list[tuple[Path, dict]] = []
    for path in sorted(objects_dir.glob("*.json"), key=lambda item: item.name.casefold()):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: cannot read {path}: {exc}", file=sys.stderr)
            continue
        categories = data.get("categories", [])
        if not isinstance(categories, list):
            print(f"Warning: categories is not a list in {path}", file=sys.stderr)
            continue
        if categories:
            continue
        is_deken = bool(data.get("source_archive") or data.get("source_member"))
        if include_all_empty or is_deken:
            candidates.append((path, data))
    return candidates


def batches(items: list, size: int) -> Iterable[list]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def output_schema(ids: list[str], categories: list[str]) -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {
            "classifications": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "enum": ids},
                        "categories": {
                            "type": "array",
                            "items": {"type": "string", "enum": categories},
                        },
                    },
                    "required": ["id", "categories"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["classifications"],
        "additionalProperties": False,
    }


def classification_prompt(
    batch: list[tuple[Path, dict]], taxonomy: dict[str, str]
) -> str:
    objects = []
    for path, data in batch:
        objects.append(
            {
                "id": path.name,
                "title": str(data.get("title", "")),
                "library": str(data.get("library_name", "")),
                "description": str(data.get("description", "")),
            }
        )
    category_lines = "\n".join(
        f"- {name}: {path}" for name, path in taxonomy.items()
    )
    return f"""Classify each Pure Data (Pd) object into one to three categories.

Use only category names from the taxonomy below. Prefer the smallest number of
specific categories that accurately describe the object's primary function.
Do not infer unsupported behavior. Classify every input object exactly once and
preserve its `id` exactly. Return only the JSON required by the output schema.

Taxonomy:
{category_lines}

Objects:
{json.dumps(objects, indent=2, ensure_ascii=False)}
"""


def parse_classifications(
    value: dict, expected_ids: set[str], allowed_categories: set[str]
) -> dict[str, list[str]]:
    rows = value.get("classifications") if isinstance(value, dict) else None
    if not isinstance(rows, list):
        raise ValueError("output has no classifications array")
    result: dict[str, list[str]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("classification is not an object")
        object_id = row.get("id")
        categories = row.get("categories")
        if object_id not in expected_ids:
            raise ValueError(f"unexpected object id: {object_id!r}")
        if object_id in result:
            raise ValueError(f"duplicate object id: {object_id!r}")
        if not isinstance(categories, list) or not 1 <= len(categories) <= 3:
            raise ValueError(f"invalid categories for {object_id!r}")
        if len(categories) != len(set(categories)):
            raise ValueError(f"duplicate categories for {object_id!r}")
        unknown = set(categories) - allowed_categories
        if unknown:
            raise ValueError(f"unknown categories for {object_id!r}: {sorted(unknown)}")
        result[object_id] = categories
    missing = expected_ids - result.keys()
    if missing:
        raise ValueError(f"missing object ids: {sorted(missing)}")
    return result


def run_codex(
    prompt: str,
    schema: dict,
    codex_bin: str,
    model: str | None,
    timeout: int,
    work_dir: Path,
) -> dict:
    schema_path = work_dir / "categories.schema.json"
    output_path = work_dir / "last-message.json"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")
    output_path.unlink(missing_ok=True)
    command = [
        codex_bin,
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
    return json.loads(output_path.read_text(encoding="utf-8"))


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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--objects-dir", type=Path, default=Path("docs/objects_raw")
    )
    parser.add_argument(
        "--taxonomy", type=Path, default=Path("docs/categories_model.json")
    )
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--limit", type=int, help="maximum objects to categorize")
    parser.add_argument("--model", help="optional Codex model override")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--include-all-empty",
        action="store_true",
        help="also categorize empty records not created by the Deken importer",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="list candidates without calling Codex"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.batch_size < 1 or args.timeout < 1 or args.retries < 0:
        print(
            "Error: batch size and timeout must be positive; retries cannot be negative",
            file=sys.stderr,
        )
        return 2
    objects_dir = args.objects_dir.expanduser().resolve()
    taxonomy_path = args.taxonomy.expanduser().resolve()
    if not objects_dir.is_dir() or not taxonomy_path.is_file():
        print("Error: objects directory or taxonomy file does not exist", file=sys.stderr)
        return 2
    if not args.dry_run and shutil.which(args.codex_bin) is None:
        print(f"Error: `{args.codex_bin}` CLI was not found in PATH", file=sys.stderr)
        return 2

    model = json.loads(taxonomy_path.read_text(encoding="utf-8"))
    taxonomy = category_paths(model)
    if not taxonomy:
        print("Error: taxonomy has no leaf categories", file=sys.stderr)
        return 2
    candidates = load_candidates(objects_dir, args.include_all_empty)
    if args.limit is not None:
        candidates = candidates[: max(0, args.limit)]
    print(
        f"Found {len(candidates)} uncategorized "
        f"{'object' if len(candidates) == 1 else 'objects'} in scope."
    )
    if args.dry_run:
        for path, data in candidates:
            print(f"  {path.name}: {data.get('library_name', '')}")
        return 0
    if not candidates:
        return 0

    completed_count = failed_count = 0
    all_categories = set(taxonomy)
    batch_list = list(batches(candidates, args.batch_size))
    with tempfile.TemporaryDirectory(prefix="categorize-deken-") as temporary:
        work_dir = Path(temporary)
        for number, batch in enumerate(batch_list, 1):
            ids = [path.name for path, _data in batch]
            schema = output_schema(ids, list(taxonomy))
            prompt = classification_prompt(batch, taxonomy)
            print(f"[{number}/{len(batch_list)}] Classifying {len(batch)} objects...")
            classifications = None
            for attempt in range(args.retries + 1):
                try:
                    raw = run_codex(
                        prompt, schema, args.codex_bin, args.model, args.timeout, work_dir
                    )
                    classifications = parse_classifications(
                        raw, set(ids), all_categories
                    )
                    break
                except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
                    print(
                        f"  Attempt {attempt + 1}/{args.retries + 1} failed: {exc}",
                        file=sys.stderr,
                    )
            if classifications is None:
                failed_count += len(batch)
                continue
            for path, data in batch:
                data["categories"] = classifications[path.name]
                atomic_write_json(path, data)
                print(f"  {path.name} -> {', '.join(data['categories'])}")
                completed_count += 1

    print(f"Done: {completed_count} categorized, {failed_count} failed")
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
