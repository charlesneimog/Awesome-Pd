<h1 align="center">Awesome Pd</h1>

<h3 align="center">
  Complete list go to
  <a href="https://charlesneimog.github.io/Awesome-Pd/">Awesome-Pd</a>
</h3>

## What this is

This project collects and categorizes Pure Data (Pd) externals, abstractions, build tools, Pd-for-web projects, and related resources. Use the site or this repo as a quick reference when searching for Pd objects, compilation helpers, or web deployment tools.

## Contents (high level)

- Externals (AI, Ambisonics, Reverbs, Synthesis, MIDI, etc.)
- Compilation tools (pd-lib-builder, pd.cmake, etc.)
- Pd-for-web (pd4web, WebPd, hvcc)
- Pd-to-C converters and related tooling
- Scripts and docs used to build/deploy the site

Refer to the site for the full, categorized list. :contentReference[oaicite:2]{index=2}

## Preview the site locally

The documentation site is built with [Zensical](https://zensical.org/). Create a
virtual environment, install the site dependencies, and start the preview server:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
zensical serve
```

To create a production build in `site/`, run `zensical build --clean`.

## Generate descriptions from Deken packages

[`scripts/deken_descriptions.py`](scripts/deken_descriptions.py) reads `.dek`,
`.zip`, `.tar`, `.tar.gz`, and `.tgz` packages without extracting their binaries.
It finds `*-help.pd` files, saves their useful text, and can ask Codex CLI or
Gemini CLI to write concise descriptions.

Extract text without making AI calls:

```sh
python scripts/deken_descriptions.py /path/to/dekens --backend none
```

Test a single Codex description before processing everything:

```sh
python scripts/deken_descriptions.py /path/to/dekens --backend codex --limit 1
```

Process selected packages with Codex:

```sh
python scripts/deken_descriptions.py /path/to/dekens \
  --backend codex \
  --package 'else*' \
  --package 'cyclone*'
```

To avoid spending AI calls on objects already present in this repository, add:

```sh
--skip-existing docs/objects_raw
```

Use Gemini instead:

```sh
python scripts/deken_descriptions.py /path/to/dekens --backend gemini
```

Descriptions are appended to `deken-descriptions.jsonl`; extracted patch text is
written under `deken-help-text/`. Successful entries are skipped on later runs,
so an interrupted AI run can be resumed with the same command.

Import successful descriptions as site objects, regenerate the derived pages and
navigation, and build the site:

```sh
python scripts/import_deken_descriptions.py
python app.py --update
zensical build --clean
```

New imports have no automatically inferred category and therefore appear under
**Uncategorized**. The importer skips existing titles and reports collisions. To
refresh descriptions for existing objects from the same Deken library, use
`python scripts/import_deken_descriptions.py --update-existing`.

Categorize imported Deken objects with the authenticated Codex CLI. Results are
saved after every batch, and a later run automatically skips completed objects:

```sh
python scripts/categorize_deken_objects.py --dry-run
python scripts/categorize_deken_objects.py
```

Use `--limit 10` for a small first run, or `--batch-size 25` if a smaller prompt
is preferable. The script only changes Deken-derived records whose `categories`
list is still empty; pass `--include-all-empty` to include other empty records.

Research missing library descriptions, repositories, and issue trackers with
Codex live web search:

```sh
python scripts/enrich_libraries.py --dry-run
python scripts/enrich_libraries.py --library fd_lib --library ossia
python scripts/enrich_libraries.py
```

Each library is researched separately using only its name. The JSON receives a
`research` block containing confidence, evidence URLs, and notes. Completed
records are skipped on later runs; use `--retry-partial` or `--overwrite` when a
result needs another pass.

## Contributing

Contributions, suggestions and improvements are welcome.

Preferred workflow:

1. Fork the repository.
2. Make your changes (edit files under `docs/` for site content or add entries).
3. Submit a pull request with a short description of the change.

If you prefer, you can also use the site’s **Submit** flow (the live site contains a submit link). ([charlesneimog.github.io][1])

Please:

* Add only accurate links and short descriptions for each item.
* Keep categories consistent.
* Prefer upstream/homepage links for each external (not fork mirrors), and indicate installability when possible (e.g., “installable via Pd → Help → Find Externals”).
