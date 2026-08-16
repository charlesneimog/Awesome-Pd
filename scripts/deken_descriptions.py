#!/usr/bin/env python3
"""Extract Pd help patches from Deken archives and generate descriptions with AI.

Archives are read in place: only ``*-help.pd`` members are loaded, and binaries
are never extracted. Results are appended to JSONL so interrupted runs can resume.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Iterator


ARCHIVE_SUFFIXES = (".dek", ".zip", ".tar.gz", ".tgz", ".tar")
DEFAULT_MAX_PATCH_BYTES = 2 * 1024 * 1024
DEFAULT_MAX_PROMPT_CHARS = 30_000

PACKAGE_NAME_ALIASES = {
    "fd_lib-macos": "fd_lib",
    "ossia-v-(windows-i386-32)-externals": "ossia",
}

DESCRIPTION_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {"description": {"type": "string"}},
    "required": ["description"],
    "additionalProperties": False,
}


@dataclass(frozen=True)
class HelpPatch:
    archive: Path
    package: str
    member: str
    title: str
    content: str

    @property
    def key(self) -> tuple[str, str]:
        return (self.archive.name, self.member)

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.content.encode("utf-8")).hexdigest()


def archive_stem(path: Path) -> str:
    """Return the probable Deken package name from an archive filename."""
    name = path.name
    for suffix in sorted(ARCHIVE_SUFFIXES, key=len, reverse=True):
        if name.lower().endswith(suffix):
            name = name[: -len(suffix)]
            break
    name = re.split(r"\[v[^]]*\]", name, maxsplit=1, flags=re.IGNORECASE)[0]
    old_style_version = re.search(r"-v?\d+(?=[._~-])", name, flags=re.IGNORECASE)
    if old_style_version:
        name = name[: old_style_version.start()]
    name = name.rstrip("-_ ") or path.stem
    return PACKAGE_NAME_ALIASES.get(name.casefold(), name)


def safe_member_name(name: str) -> str | None:
    """Normalize an archive member name and reject traversal/absolute paths."""
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    if path.is_absolute() or ".." in path.parts:
        return None
    return str(path)


def decode_patch(data: bytes) -> str:
    """Decode old and new Pd patches without failing the entire archive."""
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1", errors="replace")


def read_limited(stream, limit: int, label: str) -> bytes:
    data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"{label} is larger than {limit} bytes")
    return data


def iter_zip_patches(path: Path, max_bytes: int) -> Iterator[HelpPatch]:
    with zipfile.ZipFile(path) as archive:
        for member in sorted(archive.infolist(), key=lambda item: item.filename):
            name = safe_member_name(member.filename)
            if member.is_dir() or not name or not name.lower().endswith("-help.pd"):
                continue
            if member.file_size > max_bytes:
                raise ValueError(f"{path.name}:{name} is larger than {max_bytes} bytes")
            with archive.open(member) as stream:
                content = decode_patch(read_limited(stream, max_bytes, name))
            title = PurePosixPath(name).name[: -len("-help.pd")]
            yield HelpPatch(path, archive_stem(path), name, title, content)


def iter_tar_patches(path: Path, max_bytes: int) -> Iterator[HelpPatch]:
    with tarfile.open(path, mode="r:*") as archive:
        members = sorted(archive.getmembers(), key=lambda item: item.name)
        for member in members:
            name = safe_member_name(member.name)
            if not member.isfile() or not name or not name.lower().endswith("-help.pd"):
                continue
            if member.size > max_bytes:
                raise ValueError(f"{path.name}:{name} is larger than {max_bytes} bytes")
            stream = archive.extractfile(member)
            if stream is None:
                continue
            with stream:
                content = decode_patch(read_limited(stream, max_bytes, name))
            title = PurePosixPath(name).name[: -len("-help.pd")]
            yield HelpPatch(path, archive_stem(path), name, title, content)


def iter_help_patches(path: Path, max_bytes: int) -> Iterator[HelpPatch]:
    """Read help patches from ZIP, tar, tar.gz, tgz, or extensionless .dek data."""
    if zipfile.is_zipfile(path):
        yield from iter_zip_patches(path, max_bytes)
        return
    if tarfile.is_tarfile(path):
        yield from iter_tar_patches(path, max_bytes)
        return
    raise ValueError("not a supported ZIP or tar archive")


def discover_archives(directory: Path, patterns: list[str]) -> list[Path]:
    archives = [
        path
        for path in directory.iterdir()
        if path.is_file()
        and any(path.name.lower().endswith(suffix) for suffix in ARCHIVE_SUFFIXES)
    ]
    if patterns:
        archives = [
            path
            for path in archives
            if any(
                fnmatch.fnmatch(path.name, pattern)
                or fnmatch.fnmatch(archive_stem(path), pattern)
                for pattern in patterns
            )
        ]
    return sorted(archives, key=lambda path: path.name.casefold())


def pd_unescape(text: str) -> str:
    return (
        text.replace("\\,", ",")
        .replace("\\;", ";")
        .replace("\\ ", " ")
        .replace("\\$", "$")
    )


def patch_context(content: str, max_chars: int) -> str:
    """Reduce a .pd patch to prose plus informative object/message boxes."""
    sections: dict[str, list[str]] = {"Text": [], "Objects": [], "Messages": []}
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line.startswith("#X "):
            continue
        if line.endswith(";"):
            line = line[:-1]
        parts = line.split(maxsplit=4)
        if len(parts) < 5:
            continue
        kind, value = parts[1], pd_unescape(parts[4]).strip()
        if not value:
            continue
        if kind == "text":
            sections["Text"].append(value)
        elif kind == "obj":
            sections["Objects"].append(value)
        elif kind in {"msg", "floatatom", "symbolatom", "listbox"}:
            sections["Messages"].append(value)

    chunks = []
    for heading, values in sections.items():
        if values:
            chunks.append(f"{heading}:\n" + "\n".join(values))
    context = "\n\n".join(chunks) or content
    if len(context) > max_chars:
        context = context[:max_chars].rstrip() + "\n[context truncated]"
    return context


def description_prompt(patch: HelpPatch, context: str) -> str:
    return f"""You are a technical writer familiar with Pure Data (Pd).

Write a concise English description of the `{patch.title}` object using only the
evidence in its help patch below. Explain what it does, its purpose, and one key
usage detail when supported. Use 2-3 sentences, wrap Pd object names in backticks,
and do not invent behavior. If the patch is insufficient, say so plainly.

Return only a JSON object with exactly one string field named `description`.

Package: {patch.package}
Archive member: {patch.member}

{context}
"""


def parse_json_object(text: str) -> dict:
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("AI output did not contain a JSON object")
        value = json.loads(text[start : end + 1])
    if not isinstance(value, dict) or not isinstance(value.get("description"), str):
        raise ValueError("AI output must contain a string `description` field")
    return value


def run_codex(
    prompt: str,
    model: str | None,
    schema_path: Path,
    work_dir: Path,
    timeout: int,
) -> dict:
    output_path = work_dir / "last-message.json"
    command = [
        "codex",
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
    result = subprocess.run(
        command,
        input=prompt,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else ""
        raise RuntimeError(f"Codex exited with {result.returncode}: {detail}")
    return parse_json_object(output_path.read_text(encoding="utf-8"))


def run_gemini(prompt: str, model: str | None, timeout: int) -> dict:
    command = ["gemini"]
    if model:
        command.extend(["-m", model])
    command.extend(["-p", prompt])
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else ""
        raise RuntimeError(f"Gemini exited with {result.returncode}: {detail}")
    return parse_json_object(result.stdout)


def load_completed(path: Path) -> tuple[set[tuple[str, str]], set[tuple[str, str]]]:
    completed: set[tuple[str, str]] = set()
    digests: set[tuple[str, str]] = set()
    if not path.exists():
        return completed, digests
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            print(f"Warning: ignoring invalid JSONL line {number}", file=sys.stderr)
            continue
        if record.get("description"):
            completed.add((str(record.get("archive", "")), str(record.get("member", ""))))
            digests.add(
                (
                    str(record.get("title", "")).casefold(),
                    str(record.get("patch_sha256", "")),
                )
            )
    return completed, digests


def safe_output_name(patch: HelpPatch) -> str:
    package = re.sub(r"[^A-Za-z0-9._~-]+", "_", patch.package)
    title = re.sub(r"[^A-Za-z0-9._~-]+", "_", patch.title)
    return f"{package}__{title}__{patch.digest[:10]}.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive_dir", type=Path, help="directory containing Deken archives")
    parser.add_argument(
        "--backend",
        choices=("codex", "gemini", "none"),
        default="codex",
        help="AI CLI to call, or 'none' to extract patch text only (default: codex)",
    )
    parser.add_argument("--model", help="optional model override for the selected CLI")
    parser.add_argument(
        "--output", type=Path, default=Path("deken-descriptions.jsonl")
    )
    parser.add_argument(
        "--text-dir", type=Path, default=Path("deken-help-text")
    )
    parser.add_argument(
        "--package",
        action="append",
        default=[],
        metavar="GLOB",
        help="process matching package/archive names; repeat for multiple patterns",
    )
    parser.add_argument("--limit", type=int, help="maximum number of new patches")
    parser.add_argument(
        "--skip-existing",
        type=Path,
        metavar="OBJECT_JSON_DIR",
        help="skip titles already present as JSON files in this directory",
    )
    parser.add_argument("--overwrite", action="store_true", help="ignore completed JSONL entries")
    parser.add_argument("--timeout", type=int, default=300, help="AI timeout in seconds")
    parser.add_argument("--max-patch-bytes", type=int, default=DEFAULT_MAX_PATCH_BYTES)
    parser.add_argument("--max-prompt-chars", type=int, default=DEFAULT_MAX_PROMPT_CHARS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    archive_dir = args.archive_dir.expanduser().resolve()
    if not archive_dir.is_dir():
        print(f"Error: archive directory does not exist: {archive_dir}", file=sys.stderr)
        return 2
    if args.backend != "none" and shutil.which(args.backend) is None:
        print(f"Error: `{args.backend}` CLI was not found in PATH", file=sys.stderr)
        return 2

    output = args.output.expanduser().resolve()
    text_dir = args.text_dir.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)
    completed, completed_digests = (
        (set(), set()) if args.overwrite else load_completed(output)
    )
    existing_titles: set[str] = set()
    if args.skip_existing:
        existing_dir = args.skip_existing.expanduser().resolve()
        if not existing_dir.is_dir():
            print(f"Error: object JSON directory does not exist: {existing_dir}", file=sys.stderr)
            return 2
        existing_titles = {path.stem.casefold() for path in existing_dir.glob("*.json")}
    archives = discover_archives(archive_dir, args.package)
    if not archives:
        print("No matching archives found.", file=sys.stderr)
        return 1

    processed = skipped = failures = 0
    with tempfile.TemporaryDirectory(prefix="deken-descriptions-") as temporary:
        work_dir = Path(temporary)
        schema_path = work_dir / "description.schema.json"
        schema_path.write_text(json.dumps(DESCRIPTION_SCHEMA), encoding="utf-8")

        with output.open("a", encoding="utf-8") as destination:
            for archive_index, archive in enumerate(archives, 1):
                if args.limit is not None and processed >= args.limit:
                    break

                print(f"[{archive_index}/{len(archives)}] {archive.name}")
                try:
                    patches: Iterable[HelpPatch] = iter_help_patches(
                        archive, args.max_patch_bytes
                    )
                    for patch in patches:
                        content_key = (patch.title.casefold(), patch.digest)
                        if (
                            patch.key in completed
                            or content_key in completed_digests
                            or patch.title.casefold() in existing_titles
                        ):
                            skipped += 1
                            continue
                        completed_digests.add(content_key)
                        if args.limit is not None and processed >= args.limit:
                            print(
                                f"Done: {processed} processed, {skipped} skipped, "
                                f"{failures} failed"
                            )
                            return 0 if failures == 0 else 1

                        context = patch_context(patch.content, args.max_prompt_chars)
                        text_path = text_dir / safe_output_name(patch)
                        text_path.write_text(context + "\n", encoding="utf-8")
                        record = {
                            "archive": patch.archive.name,
                            "package": patch.package,
                            "member": patch.member,
                            "title": patch.title,
                            "patch_sha256": patch.digest,
                            "text_file": str(text_path),
                        }
                        try:
                            if args.backend == "codex":
                                response = run_codex(
                                    description_prompt(patch, context),
                                    args.model,
                                    schema_path,
                                    work_dir,
                                    args.timeout,
                                )
                                record["description"] = response["description"].strip()
                            elif args.backend == "gemini":
                                response = run_gemini(
                                    description_prompt(patch, context),
                                    args.model or "gemini-2.5-flash",
                                    args.timeout,
                                )
                                record["description"] = response["description"].strip()
                            else:
                                record["description"] = None
                        except Exception as exc:
                            record["error"] = str(exc)
                            failures += 1
                            print(f"  ERROR {patch.title}: {exc}", file=sys.stderr)

                        destination.write(json.dumps(record, ensure_ascii=False) + "\n")
                        destination.flush()
                        processed += 1
                        print(f"  {patch.title}")
                except Exception as exc:
                    failures += 1
                    print(f"  ERROR archive: {exc}", file=sys.stderr)

    print(f"Done: {processed} processed, {skipped} skipped, {failures} failed")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
