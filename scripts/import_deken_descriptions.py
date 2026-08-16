#!/usr/bin/env python3
"""Import generated Deken descriptions into ``docs/objects_raw``.

New objects receive the complete schema expected by ``app.py``. Existing objects
are never overwritten unless ``--update-existing`` is supplied, and even then
only the generated description/source fields are refreshed for the same library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PLATFORM_ALIASES = {
    "linux": "Linux",
    "windows": "Windows",
    "darwin": "Mac",
    "mac": "Mac",
    "macos": "Mac",
    "osx": "Mac",
}

LIBRARY_NAME_ALIASES = {
    "fd_lib-macos": "fd_lib",
    "ossia-v-(windows-i386-32)-externals": "ossia",
}


def canonical_library_name(name: str) -> str:
    """Remove platform/build qualifiers from known Deken package names."""
    cleaned = name.strip()
    return LIBRARY_NAME_ALIASES.get(cleaned.casefold(), cleaned)


def platforms_from_archive(name: str) -> list[str]:
    lowered = name.casefold()
    found: list[str] = []
    for token, platform in PLATFORM_ALIASES.items():
        if re.search(rf"(?<![a-z]){re.escape(token)}(?![a-z])", lowered):
            if platform not in found:
                found.append(platform)
    return [name for name in ("Mac", "Linux", "Windows") if name in found]


def safe_filename(title: str) -> str | None:
    """Return a site-compatible JSON filename, or None for unsafe titles."""
    if not title or title in {".", ".."} or "/" in title or "\\" in title:
        return None
    if any(ord(character) < 32 for character in title):
        return None
    return f"{title}.json"


def load_records(path: Path) -> list[dict]:
    records: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"Warning: ignoring invalid JSONL line {number}: {exc}", file=sys.stderr)
            continue
        if isinstance(record, dict) and str(record.get("description", "")).strip():
            records.append(record)
    return records


def load_existing(directory: Path) -> dict[str, tuple[Path, dict]]:
    existing: dict[str, tuple[Path, dict]] = {}
    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: cannot read {path}: {exc}", file=sys.stderr)
            continue
        title = str(data.get("title", "")).strip().casefold()
        if title:
            existing[title] = (path, data)
    return existing


def new_object(record: dict) -> dict:
    return {
        "runs_on": platforms_from_archive(str(record.get("archive", ""))),
        "download_link": "",
        "available_on_deken": True,
        "bug_reports": "",
        "developers": [],
        "part_of_library": True,
        "library_name": canonical_library_name(str(record.get("package", ""))),
        "articles": [],
        "videos": [],
        "musics": [],
        "contributors": [],
        "ai": True,
        "title": str(record.get("title", "")).strip(),
        "description": str(record.get("description", "")).strip(),
        "categories": [],
        "similar": [],
        "source_archive": str(record.get("archive", "")),
        "source_member": str(record.get("member", "")),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", nargs="?", type=Path, default=Path("deken-descriptions.jsonl")
    )
    parser.add_argument(
        "--objects-dir", type=Path, default=Path("docs/objects_raw")
    )
    parser.add_argument(
        "--update-existing",
        action="store_true",
        help="refresh descriptions when title and library both match",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    source = args.input.expanduser().resolve()
    objects_dir = args.objects_dir.expanduser().resolve()
    if not source.is_file():
        print(f"Error: input does not exist: {source}", file=sys.stderr)
        return 2
    objects_dir.mkdir(parents=True, exist_ok=True)

    existing = load_existing(objects_dir)
    added = updated = skipped = collisions = 0
    imported_titles: set[str] = set()

    for record in load_records(source):
        obj = new_object(record)
        title_key = obj["title"].casefold()
        filename = safe_filename(obj["title"])
        if not filename:
            print(f"Warning: unsafe object title skipped: {obj['title']!r}", file=sys.stderr)
            skipped += 1
            continue

        if title_key in imported_titles:
            print(f"Warning: duplicate Deken title skipped: {obj['title']}", file=sys.stderr)
            collisions += 1
            continue
        imported_titles.add(title_key)

        if title_key in existing:
            path, old = existing[title_key]
            old_library = str(old.get("library_name", "")).strip().casefold()
            new_library = obj["library_name"].casefold()
            if args.update_existing and old_library == new_library:
                old["description"] = obj["description"]
                old["ai"] = True
                old["source_archive"] = obj["source_archive"]
                old["source_member"] = obj["source_member"]
                if obj["runs_on"]:
                    old["runs_on"] = obj["runs_on"]
                if not args.dry_run:
                    path.write_text(
                        json.dumps(old, indent=4, ensure_ascii=False) + "\n",
                        encoding="utf-8",
                    )
                updated += 1
            else:
                if old_library != new_library:
                    print(
                        f"Warning: title collision skipped: {obj['title']} "
                        f"({old_library or 'no library'} vs {new_library or 'no library'})",
                        file=sys.stderr,
                    )
                    collisions += 1
                else:
                    skipped += 1
            continue

        path = objects_dir / filename
        if not args.dry_run:
            path.write_text(
                json.dumps(obj, indent=4, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        existing[title_key] = (path, obj)
        added += 1

    prefix = "Dry run: " if args.dry_run else ""
    print(
        f"{prefix}{added} added, {updated} updated, {skipped} skipped, "
        f"{collisions} title collisions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
