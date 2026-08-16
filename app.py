import copy
import json
import os
import re
import sys
import tomllib
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Union, Dict, List, Optional, TypeAlias
from urllib.parse import parse_qs, urlparse

import numpy as np
import requests
import tomli_w
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

NavItem: TypeAlias = Union[str, Dict[str, object]]

# ==========================
# Markdown/HTML Fragments
# ==========================

GISCUS_SCRIPT_BLOCK = """
<script src="https://giscus.app/client.js"
    data-repo="charlesneimog/Awesome-PD"
    data-repo-id="R_kgDOLaunFg"
    data-category="Comments"
    data-category-id="DIC_kwDOLaunFs4CnXHy"
    data-mapping="title"
    data-strict="0"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="preferred_color_scheme"
    data-lang="en"
    data-loading="lazy"
    crossorigin="anonymous"
    async>
</script>
"""

SIMILAR_SECTION = """
---
<h3>Similar</h3>

<div class="grid cards ">
    <ul id="random-objects"></ul>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {{
    addSimilar({project_name});
}});
</script>

"""

COMMENTS_SECTION = f"""
---
<h3>Comments</h3>
{GISCUS_SCRIPT_BLOCK}
"""

AI_GENERATED_ADMONITION = """
!!! info "AI Generated"
    This content was generated with the assistance of AI. If you notice any errors, please report them or submit a fix using [Submit](../../submit.md). Check the prompt used [here](../../prompts/helppatchai.md).

---
"""

LIB_CONTRIBUTORS_HEADER = """
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>
"""

LIB_CONTRIBUTORS_SCRIPT_TEMPLATE = """
<script>
async function updateList() {{
    let repoOwner = '{repo_owner}';
    let repoName = '{repo_name}';
    try {{
        let res = await fetch(`https://api.github.com/repos/${{repoOwner}}/${{repoName}}/contributors`);
        let contributors = await res.json();
        let container = document.getElementById('libcontributors');
        contributors.forEach(user => {{
            let link = document.createElement('a');
            link.href = user.html_url;
            link.target = '_blank';
            let img = document.createElement('img');
            img.src = user.avatar_url;
            img.alt = user.login;
            img.className = 'libavatar';

            link.appendChild(img);
            container.appendChild(link);
        }});
    }} catch(err) {{
        console.error(err);
    }}
}}
updateList();
</script>
"""

CONTRIBUTORS_SECTION_TEMPLATE = """
<h3>Contributors</h3>

<div id="avatars"></div>

<script>
let nicknames = {nicknames_json};
let container = document.getElementById('avatars');
nicknames.forEach(nick => {{
  let link = document.createElement('a');
  link.href = `https://github.com/${{nick}}`;
  link.target = '_blank'; // opens in new tab
  let img = document.createElement('img');
  img.src = `https://github.com/${{nick}}.png`;
  img.alt = nick;
  img.className = 'avatar';
  link.appendChild(img);
  container.appendChild(link);
}});
</script>
"""


# ==========================
# Utilities
# ==========================


def slugify(name: str) -> str:
    return name.replace(" ", "_").replace("/", "_").lower()


def strip_md_links(text: str) -> str:
    # Replace [label](url) -> label
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


@dataclass(frozen=True)
class Paths:
    base_dir: Path
    docs: Path

    artists: Path
    libraries: Path
    pieces: Path
    pieces_raw: Path
    objects: Path
    objects_raw: Path

    @staticmethod
    def from_base(base: Optional[Path] = None) -> "Paths":
        base_dir = base or Path(__file__).resolve().parent
        docs = base_dir / "docs"
        return Paths(
            base_dir=base_dir,
            docs=docs,
            artists=docs / "artists",
            libraries=docs / "libraries",
            pieces=docs / "pieces",
            pieces_raw=docs / "pieces_raw",
            objects=docs / "objects",
            objects_raw=docs / "objects_raw",
        )


# ==========================
# Main Class
# ==========================


class AwesomePd:
    """
    Orchestrates:
    - Reading open issues to ingest JSON payloads describing objects/externals.
    - Generating Markdown pages for each object in docs/objects/*.md.
    - Optionally updating categories.json and zensical.toml navigation.
    """

    UPDATE_CATEGORIES_AND_CONFIG = False

    WEB_TOOLS = {
        "pd4web": "web/pd4web.md",
        "pdwebparty": "web/pdwebparty.md",
        "purrdata": "web/purrdata.md",
        "pdxr": "web/pdxr.md",
    }
    TOOLS = {
        "deken": "deken.md",
        "pd.cmake": "devs/pd.cmake.md",
        "pd-lib-builder": "devs/pdlibbuilder.md",
    }
    OS_ICON_MAP = {
        "Windows": ":fontawesome-brands-windows:",
        "Mac": ":fontawesome-brands-apple:",
        "Linux": ":fontawesome-brands-linux:",
    }

    OWNER = "charlesneimog"
    REPO = "Awesome-Pd"
    UNCATEGORIZED_CATEGORY = "Uncategorized"

    @classmethod
    def _categories_for(cls, item: dict) -> List[str]:
        """Return usable page categories without changing the source JSON."""
        categories = [
            str(category).strip()
            for category in item.get("categories", [])
            if str(category).strip()
        ]
        return categories or [cls.UNCATEGORIZED_CATEGORY]

    def __init__(self, update_docs: bool = False) -> None:
        self.paths = Paths.from_base()
        with open("docs/categories_model.json", "r", encoding="utf-8") as f:
            self.objects: Dict[str, Union[dict, list]] = json.load(f)
        with open("docs/categories_model_pieces.json", "r", encoding="utf-8") as f:
            self.pieces: Dict[str, Union[dict, list]] = json.load(f)
        with open("zensical.toml", "rb") as f:
            self.config = tomllib.load(f)

        self.videos: List[dict] = []
        self.music: List[dict] = []
        self.articles: List[dict] = []

        self.UPDATE_CATEGORIES_AND_CONFIG = update_docs
        if update_docs:
            self.home_update()
        else:
            self.github_actions()
            return

        # Deduplicate by link
        self.videos = list({item["link"]: item for item in self.videos}.values())
        self.music = list({item["link"]: item for item in self.music}.values())
        self.articles = list({item["link"]: item for item in self.articles}.values())

        (self.paths.docs / "all_videos.json").write_text(
            json.dumps(self.videos, indent=4), encoding="utf-8"
        )
        (self.paths.docs / "all_music.json").write_text(
            json.dumps(self.music, indent=4), encoding="utf-8"
        )
        (self.paths.docs / "all_articles.json").write_text(
            json.dumps(self.articles, indent=4), encoding="utf-8"
        )

    # --------------------------
    # GitHub Issues Integration
    # --------------------------

    def _get_open_issues(self) -> List[dict]:
        url = f"https://api.github.com/repos/{self.OWNER}/{self.REPO}/issues?state=open"
        headers = {"Accept": "application/vnd.github+json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def github_actions(self) -> None:
        """
        Runs in CI mode: fetch open issues, ingest new JSON object definitions,
        and regenerate Markdown after each issue processing.
        """
        issues = self._get_open_issues()
        for issue in issues:
            self.check_new_issues(issue)
            # self.create_markdowns()

    # --------------------------
    # Rendering Helpers
    # --------------------------

    def youtube_embed(self, url: str) -> str:
        """Return a YouTube iframe embed for any YouTube watch URL."""
        query = parse_qs(urlparse(url).query)
        video_id = query.get("v", [""])[0]
        if not video_id:
            raise Exception(f"Not possible parse the video {video_id}")
        return (
            f'<iframe style="border-radius: 8px" width="560" height="315"\n'
            f'        src="https://www.youtube.com/embed/{video_id}"\n'
            f'        title="YouTube video player" frameborder="0"\n'
            f'        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"\n'
            f'        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
        )

    # --------------------------
    # Markdown Generation
    # --------------------------

    def _build_info_lines(self, project: dict) -> List[str]:
        """
        Builds the bullet lines for the info grid. Output preserved.
        """
        lines: List[str] = []
        obj_name = project["title"]
        if obj_name == "index":
            obj_name = project["library_name"] + "_" + obj_name

        # Download / Deken
        if project.get("download_link") or project.get("available_on_deken"):
            deken_text = (
                " or use [Deken](../../deken.md)."
                if project.get("available_on_deken")
                else ""
            )
            dl_text = (
                f"[here]({project['download_link']})"
                if project.get("download_link")
                else ""
            )
            if project.get("download_link"):
                download_line = (
                    f":octicons-download-16: __Download__ {dl_text}{deken_text}."
                )
            else:
                download_line = (
                    f":octicons-download-16: __Download__ via [Deken](../../deken.md)."
                )
            if project.get("library_name"):
                download_line += (
                    f'  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. '
                    f'Search for <code>{project["library_name"]}</code> and install it. '
                    f'Then create an object with `declare -lib {project["library_name"]} -path {project["library_name"]}`. '
                    f'Finally, use `{obj_name}` or any other object from `{project["library_name"]}`._</p>'
                )
            lines.append(f"- {download_line}")

        # Developers
        if project.get("developers"):
            lines.append(
                f"- :fontawesome-brands-dev: Library developed mainly by **{', '.join(project['developers'])}**."
            )

        # Bug Reports
        if project.get("bug_reports"):
            lines.append(
                f"- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here]({project['bug_reports']})!"
            )

        # OS icons
        if project.get("runs_on"):
            os_icons = " ".join(
                self.OS_ICON_MAP.get(os_name, os_name)
                for os_name in project.get("runs_on", [])
            )
            lines.append(
                f"- :fontawesome-solid-computer: __Available__ for {os_icons}."
            )

        return lines

    def _render_articles(self, project: dict) -> str:
        if not project.get("articles"):
            return ""
        out: List[str] = []
        out.append("---\n<h3>Articles</h3>\n")
        out.append('<div class="grid cards" markdown>\n')
        for a in project["articles"]:
            out.append("- :octicons-book-24: \n")
            out.append(f"    <h4>{escape(a['title'])}</h4>\n")
            out.append(f"    *by {', '.join(map(escape, a['authors']))}*\n\n")
            out.append(f"    [Link]({a['link']})\n")
            self.articles.append(a)
        out.append("</div>\n\n")
        return "".join(out)

    def _render_videos(self, project: dict) -> str:
        if not project.get("videos"):
            return ""
        out: List[str] = []
        out.append("---\n<h3>Videos</h3>\n\n")
        out.append('<div style="display: flex; justify-content: center; gap: 20px;">\n')
        for v in project["videos"]:
            self.videos.append(v)
            out.append(f"    {self.youtube_embed(v['link'])}\n")
        out.append("</div>\n\n")
        return "".join(out)

    def _render_musics(self, project: dict) -> str:
        if not project.get("musics"):
            return ""
        out: List[str] = []
        out.append("---\n<h3>Music</h3>\n\n")
        out.append('<div style="display: flex; justify-content: center; gap: 20px;">\n')
        for m in project["musics"]:
            self.music.append(m)
            out.append(f"    {self.youtube_embed(m['link'])}\n")
        out.append("</div>\n\n---\n\n")
        return "".join(out)

    def _render_similar_block(self, project) -> str:
        title = project.get("title")
        if not title:
            return ""
        js_title = json.dumps(title)  # garante string JS válida
        out: List[str] = []
        out.append("---\n<h3>Similar</h3>\n\n")
        out.append('<div class="grid cards ">\n')
        out.append('    <ul id="random-objects"></ul>\n')
        out.append("</div>\n\n")
        out.append("<script>\n")
        out.append('document.addEventListener("DOMContentLoaded", () => {\n')
        out.append(f"    addSimilar({js_title});\n")
        out.append("});\n")
        out.append("</script>\n")
        return "".join(out)

    def _render_comments_block(self) -> str:
        """
        Returns the comments block string. Output preserved.
        """
        return COMMENTS_SECTION

    def _render_contributors(self, contributors: List[str]) -> str:
        """
        Returns the contributors block. Output preserved.
        """
        js_array = json.dumps(contributors)
        return CONTRIBUTORS_SECTION_TEMPLATE.format(nicknames_json=js_array)

    def create_pieces_markdowns(self) -> None:
        """
        Iterate over docs/pieces_raw/*.json (or fallback to objects_raw) and produce corresponding .md files.
        Structure and blocks mirror create_objects_markdowns but adapted to "pieces".
        """
        piece_dir = self.paths.pieces
        json_dir = getattr(self.paths, "pieces_raw", self.paths.pieces_raw)
        json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]
        for json_file in json_files:
            print(f"Creating piece markdown for {json_file.replace('.json', '')}")
            path = json_dir / json_file
            with open(path, "r", encoding="utf-8") as f:
                project = json.load(f)

            title = project.get("title", "")
            description = project.get("description", "")
            parts: List[str] = []
            parts.append(f"# {title}\n\n{description}\n\n---\n")

            # Build info lines specific to pieces
            def _build_piece_info_lines(p) -> List[str]:
                lines: List[str] = []

                def _fmt_list(val):
                    if isinstance(val, list):
                        return ", ".join([str(x) for x in val if str(x).strip()])
                    return str(val or "").strip()

                composers = _fmt_list(p.get("developers", []))
                performers = _fmt_list(p.get("performers", []))
                year = str(p.get("year") or "").strip()
                instruments = str(p.get("instruments") or "").strip()

                # Add cards only for fields that exist
                if composers:
                    lines.append(f"-   **Composer(s):** {composers}")
                if performers:
                    lines.append(f"-   **Performer(s):** {performers}")
                if year:
                    lines.append(f"-   **Year:** {year}")
                if instruments:
                    lines.append(f"-   **Instruments:** {instruments }")

                return lines

            lines = _build_piece_info_lines(project)
            if lines:
                parts.append('<div class="grid cards" markdown>\n')
                parts.append("\n".join(lines))
                parts.append("\n</div>")

            # Media blocks (reuse existing helpers)
            parts.append(self._render_articles(project))
            parts.append(self._render_videos(project))
            parts.append(self._render_musics(project))

            # Similar, comments, contributors
            parts.append(self._render_comments_block())

            md = "".join(parts)

            # Write one file per category (first is canonical, others hidden from search)
            effective_json_name = json_file
            categories = self._categories_for(project)

            first = True
            for c in categories:
                final_md = (
                    md if first else f"---\nsearch:\n    exclude: true\n---\n\n{md}"
                )
                c_slug = slugify(c)
                output_path = (
                    piece_dir
                    / c_slug
                    / slugify(effective_json_name.replace(".json", ".md"))
                )
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(final_md, encoding="utf-8")
                first = False

    def create_objects_markdowns(self) -> None:
        """
        Iterate over docs/objects_raw/*.json and produce corresponding .md files.
        """
        obj_dir = self.paths.objects
        json_dir = self.paths.objects_raw
        json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]

        libraries: Dict[str, Dict[str, str]] = {}
        print("")
        for json_file in json_files:
            print(f"Creating markdown for {json_file.replace('.json', '')}")
            path = json_dir / json_file
            with open(path, "r", encoding="utf-8") as f:
                project = json.load(f)

            if project["part_of_library"]:
                libraries[project["library_name"]] = {
                    "description": "",
                    "issues": project["bug_reports"],
                    "link": "",
                }

            title = project.get("title", "")
            lib = project.get("library_name", "")

            file_title = lib + "_" + title if title == "index" else title
            description = project.get("description", "")

            parts: List[str] = []
            parts.append(f"# {file_title}\n\n{description}\n\n---\n")

            if project.get("ai", False):
                parts.append(AI_GENERATED_ADMONITION)

            # Info lines inside grid
            lines = self._build_info_lines(project)
            if lines:
                parts.append('<div class="grid cards" markdown>\n')
                parts.append("\n".join(lines))
                parts.append("\n</div>")

            # Articles / Videos / Music
            parts.append(self._render_articles(project))
            parts.append(self._render_videos(project))
            parts.append(self._render_musics(project))

            # Simlar block
            parts.append(self._render_similar_block(project))

            # Comments block
            parts.append(self._render_comments_block())

            # Contributors block
            contributors: List[str] = project["contributors"]
            parts.append(self._render_contributors(contributors))

            md = "".join(parts)

            effective_json_name = (
                f"{lib}_{json_file}"
                if json_file.replace(".json", "") == "index"
                else json_file
            )

            first = True
            for c in self._categories_for(project):
                final_md = md
                if not first:
                    final_md = f"---\nsearch:\n    exclude: true\n---\n\n{md}"

                c_slug = slugify(c)
                output_path = (
                    obj_dir / c_slug / effective_json_name.replace(".json", ".md")
                )
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(final_md, encoding="utf-8")
                first = False

        # Library metadata files
        for lib in libraries:
            thislib = libraries[lib]
            file = self.paths.libraries / f"{lib}.json"
            if not file.exists():
                thislib["link"] = thislib["issues"].replace("issues", "")
                file.write_text(json.dumps(thislib, indent=4), encoding="utf-8")

    # --------------------------
    # Issue Payload Ingestion
    # --------------------------
    def extract_full_json_block(self, text: str) -> str | None:
        start = text.find("```json")
        if start == -1:
            return None
        # Começa depois do \n
        start_content = text.find("\n", start) + 1
        if start_content == 0:
            return None

        brace_count = 0
        in_string = False
        escape = False
        end_pos = start_content

        while end_pos < len(text):
            c = text[end_pos]

            if c == '"' and not escape:
                in_string = not in_string

            if not in_string:
                if c == "{":
                    brace_count += 1
                elif c == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        # fechou o JSON
                        return text[start_content : end_pos + 1]

            escape = c == "\\" and not escape
            end_pos += 1

        return None

    def check_new_issues(self, issue: dict) -> None:
        """
        Parse the JSON fenced code block in the issue body, ensure the creator is
        in contributors, save the JSON under docs/objects/{title}.json.
        """
        text = issue["body"]
        creator = issue["user"]["login"]
        json_blocks = self.extract_full_json_block(text)
        if not json_blocks:
            return
        json_file = json.loads(json_blocks)

        if creator not in json_file["contributors"]:
            json_file["contributors"].append(creator)

        whatiam = json_file["whatiam"]
        if whatiam == "object":
            lib = json_file["library_name"]
            obj_name = json_file["title"]
            if obj_name == "index":
                obj_name = json_file["library_name"] + "_" + obj_name
            output_dir = self.paths.objects_raw
            output_dir.mkdir(parents=True, exist_ok=True)

            if obj_name == "index":
                obj_name = f"{lib}_{obj_name}"

            (output_dir / f"{obj_name}.json").write_text(
                json.dumps(json_file, indent=4), encoding="utf-8"
            )

        elif whatiam == "piece":
            output_dir = self.paths.pieces_raw
            output_dir.mkdir(parents=True, exist_ok=True)
            obj_name = json_file["title"]
            (output_dir / f"{obj_name}.json").write_text(
                json.dumps(json_file, indent=4, ensure_ascii=False), encoding="utf-8"
            )

    # --------------------------
    # Navigation Helpers
    # --------------------------
    def update_main_json_of_objects(self):
        """
        (Opcional) Se você quiser parar de inserir 'pieces/<obj>.md', comente a chamada de found_category.
        """
        pass

    def build_piece_abs_nav(self, d: dict) -> dict:
        piecedir = self.paths.pieces_raw
        categories: Dict[str, List[List[str]]] = {}
        for file in os.listdir(piecedir):
            if not file.endswith(".json"):
                continue
            with open(piecedir / file, "r", encoding="utf-8") as f:
                data = json.load(f)

            name = data["title"]
            description = data["description"].split(". ")[0] + "."
            for category in self._categories_for(data):
                categories.setdefault(category, []).append([name, description])
        return categories

    def build_obj_abs_nav(self, d: dict) -> dict:
        objdir = self.paths.objects_raw
        categories: Dict[str, List[List[str]]] = {}
        for file in os.listdir(objdir):
            if not file.endswith(".json"):
                continue
            with open(objdir / file, "r", encoding="utf-8") as f:
                data = json.load(f)
            name = data["title"]
            if name == "index":
                name = data["library_name"] + "_" + name
            description = data["description"].split(". ")[0] + "."
            for category in self._categories_for(data):
                categories.setdefault(category, []).append([name, description])
        return categories

    def pieces_add_md_to_category(
        self, d: dict, piecename: str, category: str, value: str
    ):
        """
        Procura recursivamente a categoria e adiciona o value na lista correspondente,
        evitando duplicações do mesmo objeto.
        """
        for k, v in d.items():
            if k == category and isinstance(v, list):
                if len(v) == 0:
                    c = slugify(category)
                    v.append(f"pieces/{c}/index.md")
                for item in v:
                    if isinstance(item, dict) and piecename in item:
                        return True
                v.append({piecename: value})
                return True
            elif isinstance(v, dict):
                if self.pieces_add_md_to_category(v, piecename, category, value):
                    return True
        return False

    def objects_add_md_to_category(
        self, d: dict, objname: str, category: str, value: str
    ):
        """
        Procura recursivamente a categoria e adiciona o value na lista correspondente,
        evitando duplicações do mesmo objeto.
        """
        for k, v in d.items():
            if k == category and isinstance(v, list):
                if len(v) == 0:
                    c = slugify(category)
                    v.append(f"objects/{c}/index.md")
                for item in v:
                    if isinstance(item, dict) and objname in item:
                        return True
                v.append({objname: value})
                return True
            elif isinstance(v, dict):
                if self.objects_add_md_to_category(v, objname, category, value):
                    return True
        return False

    def sort_section(self, section):
        if isinstance(section, str):
            return section

        if isinstance(section, dict):
            for key, value in section.items():
                index_file = value[0]  # sempre o primeiro (index.md)
                others = value[1:]  # o resto
                # Ordena pelas chaves dos dicionários
                others_sorted = sorted(others, key=lambda x: list(x.keys())[0])
                section[key] = [index_file] + others_sorted
            return section

        return section  # fallback

    def piece_dict_to_nav(self, d: dict) -> list:
        """
        Constrói a nav SEM mutar self.objects.
        Lê os JSONs em docs/objects_raw e monta uma estrutura temporária.
        """
        temp = copy.deepcopy(d)
        temp.setdefault(self.UNCATEGORIZED_CATEGORY, [])
        for j in os.listdir(self.paths.pieces_raw):
            if not j.endswith(".json"):
                continue
            with open(self.paths.pieces_raw / j, "r", encoding="utf-8") as f:
                obj = json.load(f)
            piecename = obj["title"]
            for c in self._categories_for(obj):
                c_key = slugify(c)
                value = f"pieces/{c_key}/{slugify(piecename)}.md"
                piecename = f"{obj["title"]} ({obj["year"]})"
                self.pieces_add_md_to_category(temp, piecename, c, value)

        def recurse(x):
            nav_list = []
            for key, value in sorted(x.items()):
                if isinstance(value, dict):
                    nav_list.append({key: recurse(value)})
                else:
                    if len(value) != 0:
                        nav_list.append({key: value})
            return nav_list

        data = ["pieces/index.md"] + recurse(temp)
        return [self.sort_section(sec) for sec in data]

    def obj_dict_to_nav(self, d: dict) -> list:
        """
        Build compact object navigation without mutating ``self.objects``.

        Object pages are already linked from their category indexes and found
        through search. Adding every object to the global navigation duplicates
        thousands of links in every generated HTML page, so only populated
        category indexes belong in the sidebar.
        """
        temp = copy.deepcopy(d)
        temp.setdefault(self.UNCATEGORIZED_CATEGORY, [])

        def add_category_index(x: dict, category: str) -> bool:
            for key, value in x.items():
                if key == category and isinstance(value, list):
                    if not value:
                        value.append(f"objects/{slugify(category)}/index.md")
                    return True
                if isinstance(value, dict) and add_category_index(value, category):
                    return True
            return False

        for j in os.listdir(self.paths.objects_raw):
            if not j.endswith(".json"):
                continue
            with open(self.paths.objects_raw / j, "r", encoding="utf-8") as f:
                obj = json.load(f)
            for c in self._categories_for(obj):
                add_category_index(temp, c)

        def recurse(x):
            nav_list = []
            for key, value in sorted(x.items()):
                if isinstance(value, dict):
                    nav_list.append({key: recurse(value)})
                else:
                    if len(value) != 0:
                        nav_list.append({key: value})
            return nav_list

        data = ["objects/index.md"] + recurse(temp)
        return data

    def dict_to_nav(self, d: dict) -> list:
        """
        Convert a nested dict to a Zensical `nav` list structure.
        """
        nav_list = []
        for key, value in sorted(d.items()):
            if isinstance(value, dict):
                nav_list.append({key: self.dict_to_nav(value)})
            else:
                nav_list.append({key: value})
        return nav_list

    def found_category(
        self, target_key: str, new_data: dict, obj: Optional[dict] = None
    ) -> bool:
        """
        Procura target_key dentro de obj (dict aninhado) e insere new_data
        apenas dentro da lista correspondente a target_key.
        """
        if obj is None:
            obj = self.objects

        for key, value in obj.items():
            if key == target_key:
                if isinstance(value, list):
                    if new_data not in value:
                        value.append(new_data)
                    return True
                else:
                    raise ValueError(
                        f"Categoria '{target_key}' não é uma lista em categories.json"
                    )
            elif isinstance(value, dict):
                if self.found_category(target_key, new_data, value):
                    return True

        return False

    # --------------------------
    # Full Site Update
    # --------------------------
    def render_libraries_md(self, libraries) -> Dict[str, str]:
        nav_libs: Dict[str, str] = {}
        md = '# Libraries\n\n<div class="grid cards" markdown>\n'
        for lib in libraries:
            print(f"Update Library page: {lib}")
            lib_json_path = self.paths.libraries / f"{lib}.json"
            with open(lib_json_path, "r", encoding="utf-8") as f:
                lib_data = json.load(f)
            libmarkdownfile = self.render_library_markdown(
                lib, lib_data, libraries[lib]
            )
            lib_md_path = self.paths.libraries / f"{lib}.md"
            lib_md_path.write_text(libmarkdownfile, encoding="utf-8")
            nav_libs[lib] = f"libraries/{lib}.md"
            des = lib_data["description"].split(". ")[0]
            md += f"- :material-tune: [__{lib}__]({lib}.md) {des}.\n"

        md += "</div>\n"
        with open(os.path.join(self.paths.libraries, "index.md"), "w") as f:
            f.write(md)

        return nav_libs

    def render_library_markdown(
        self,
        libname: str,
        lib_data: dict,
        objects_list: List[List[str]],
    ) -> str:
        """
        Build a library page markdown with contributors grid and objects list.
        """
        parts: List[str] = []
        parts.append("---\nsearch:\n    exclude: true\n---\n\n")
        parts.append(f"# {libname}\n")
        parts.append(lib_data.get("description", ""))

        repository_url = str(lib_data.get("link", "")).strip()
        issues_url = str(lib_data.get("issues", "")).strip()
        if repository_url or issues_url:
            parts.append('\n\n<div class="grid cards" markdown>\n')
            if repository_url:
                parts.append(
                    f"- :material-source-repository: __Repository__ "
                    f"[Source code]({repository_url})\n"
                )
            if issues_url:
                parts.append(
                    f"- :material-bug: __Issues__ [Report or browse issues]({issues_url})\n"
                )
            parts.append("</div>\n")
        parts.append(LIB_CONTRIBUTORS_HEADER)

        url = repository_url
        match = re.fullmatch(
            r"https?://github\.com/([^/]+)/([^/]+)/?", url, flags=re.IGNORECASE
        )
        if match:
            repo_owner, repo_name = match.groups()
            parts.append(
                LIB_CONTRIBUTORS_SCRIPT_TEMPLATE.format(
                    repo_owner=repo_owner, repo_name=repo_name
                )
            )
        parts.append("\n")

        parts.append('<h2>Objects</h2>\n\n<div class="grid cards" markdown>\n')
        for obj in sorted(objects_list):
            text = strip_md_links(obj[1])
            parts.append(f"- :material-tune: [__{obj[0]}__]({obj[2]}) {text}\n")
        parts.append("</div>")
        return "".join(parts)

    def home_update(self) -> None:
        """
        End-to-end update flow:
        - Refresh issues and save new object JSONs.
        - Generate all markdowns for objects.
        - Build library pages and Zensical navigation.
        """
        print("Updating all")

        if self.objects is None or self.config is None:
            raise Exception("Error to open objects or config")

        # Process open issues
        issues = self._get_open_issues()
        for issue in issues:
            self.check_new_issues(issue)

        # Similarity is derived from the raw object data and must be refreshed
        # before rendering Markdown so pages never contain stale recommendations.
        self.update_similarity()

        # Regenerate Markdown pages
        self.create_pieces_markdowns()

        # Regenerate Markdown pages
        self.create_objects_markdowns()

        # update main json (noop)
        self.update_main_json_of_objects()

        # Build Libraries pages + map
        libraries: Dict[str, List[List[str]]] = {}

        # Update all pieces json
        all_pieces: List[str] = []
        for root, _, files in os.walk(self.paths.pieces_raw):
            for filename in files:
                filepath = Path(root) / filename
                if not filepath.suffix == ".json":
                    continue
                all_pieces.append(filename.replace(".json", ""))

        (self.paths.docs / "all_pieces.json").write_text(
            json.dumps(all_pieces, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

        # Update all objects json
        all_objects: List[str] = []
        for root, _, files in os.walk(self.paths.objects_raw):
            for filename in files:
                filepath = Path(root) / filename
                if not filepath.suffix == ".json":
                    continue
                all_objects.append(filename.replace(".json", ""))
                with open(filepath, "r", encoding="utf-8") as f:
                    object_json = json.load(f)
                    if object_json["part_of_library"] is True:
                        libname = object_json["library_name"]
                        if libname != "":
                            objname = object_json["title"]
                            if objname == "index":
                                objname = f"{libname}_{objname}"

                            description = (
                                object_json["description"].split(". ")[0] + "."
                            )
                            c = slugify(self._categories_for(object_json)[0])

                            libraries.setdefault(libname, []).append(
                                [objname, description, f"../objects/{c}/{objname}.md"]
                            )

        (self.paths.docs / "all_objects.json").write_text(
            json.dumps(all_objects, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

        # update libraries
        nav_libs: Dict[str, str] = self.render_libraries_md(libraries)

        # Build site nav
        nav: List[NavItem] = [{"Home": "index.md"}]
        nav.append({"Submit": "submit.md"})
        nav.append({"Objects & Abstractions": self.obj_dict_to_nav(self.objects)})
        nav.append({"Libraries": ["libraries/index.md"] + self.dict_to_nav(nav_libs)})
        nav.append({"Pieces": self.piece_dict_to_nav(self.pieces)})
        nav.append({"Web": self.dict_to_nav(self.WEB_TOOLS)})
        nav.append({"Tools": self.dict_to_nav(self.TOOLS)})

        # pieces
        categories = self.build_piece_abs_nav(self.objects)
        print()
        for c, descriptions in categories.items():
            print(f"Category being created: {c}")
            c_name = slugify(c)
            parts = [
                f"---\nsearch:\n    exclude: true\n---\n\n# {c}\n\n",
                '<div class="grid cards" markdown>\n\n',
            ]
            for d in descriptions:
                obj = d[0]
                des = d[1]
                parts.append(
                    f"- :material-tune: [__{obj}__]({slugify(obj)}.md) {des}\n"
                )
            parts.append("\n</div>")
            (self.paths.pieces / c_name / "index.md").write_text(
                "".join(parts), encoding="utf-8"
            )

        # build category index pages
        categories = self.build_obj_abs_nav(self.objects)
        print()
        for c, descriptions in categories.items():
            print(f"Category being created: {c}")
            c_name = slugify(c)
            parts = [
                f"---\nsearch:\n    exclude: true\n---\n\n# {c}\n\n",
                '<div class="grid cards" markdown>\n\n',
            ]
            for d in descriptions:
                obj = d[0]
                des = d[1]
                parts.append(f"- :material-tune: [__{obj}__]({obj}.md) {des}\n")
            parts.append("\n</div>")
            (self.paths.objects / c_name / "index.md").write_text(
                "".join(parts), encoding="utf-8"
            )

        # Update Zensical config
        self.config["project"]["nav"] = nav
        with Path("zensical.toml").open("wb") as f:
            tomli_w.dump(self.config, f, multiline_strings=True)

    # --------------------------
    # Full Similarity Update
    # --------------------------
    @staticmethod
    def _cosine_or_zeros(vectorizer, documents, size: int) -> np.ndarray:
        """Vectorize documents and return a safe pairwise cosine matrix."""
        try:
            matrix = vectorizer.fit_transform(documents)
        except ValueError as exc:
            if "empty vocabulary" not in str(exc):
                raise
            return np.zeros((size, size), dtype=np.float32)
        return cosine_similarity(matrix, dense_output=True)

    def similarity_recommendations(
        self, objects: List[dict], limit: int = 4
    ) -> List[List[str]]:
        """Rank related Pd objects with text, name, category, and library signals.

        Descriptions use word unigrams and bigrams, while titles use character
        n-grams to recognize Pd naming families such as ``glide~`` and
        ``glide2~``. Categories are treated as IDF-weighted tokens so a match in
        a rare, specific category matters more than a match in a broad category.
        """
        size = len(objects)
        if size < 2:
            return [[] for _ in objects]

        titles = [str(obj.get("title", "")).strip() for obj in objects]
        descriptions = [str(obj.get("description", "")).strip() for obj in objects]
        text_documents = [
            f"{title} {title} {description}"
            for title, description in zip(titles, descriptions)
        ]

        text_similarity = self._cosine_or_zeros(
            TfidfVectorizer(
                strip_accents="unicode",
                stop_words="english",
                ngram_range=(1, 2),
                min_df=2,
                max_df=0.98,
                sublinear_tf=True,
            ),
            text_documents,
            size,
        )
        title_similarity = self._cosine_or_zeros(
            TfidfVectorizer(
                analyzer="char_wb",
                ngram_range=(2, 5),
                lowercase=True,
                sublinear_tf=True,
            ),
            titles,
            size,
        )

        category_documents = [
            [str(category) for category in obj.get("categories", []) if category]
            for obj in objects
        ]
        category_similarity = self._cosine_or_zeros(
            TfidfVectorizer(
                analyzer=lambda categories: categories,
                lowercase=False,
                use_idf=True,
                sublinear_tf=True,
            ),
            category_documents,
            size,
        )

        libraries = np.asarray(
            [str(obj.get("library_name", "")).strip().casefold() for obj in objects]
        )
        same_library = (
            (libraries[:, None] == libraries[None, :])
            & (libraries[:, None] != "")
        ).astype(np.float32)

        combined = (
            0.45 * text_similarity
            + 0.32 * category_similarity
            + 0.22 * title_similarity
            + 0.01 * same_library
        )

        recommendations: List[List[str]] = []
        for index, scores in enumerate(combined):
            candidates = [candidate for candidate in range(size) if candidate != index]
            candidates.sort(
                key=lambda candidate: (
                    -float(scores[candidate]),
                    titles[candidate].casefold(),
                )
            )
            recommendations.append(
                [titles[candidate] for candidate in candidates[:limit]]
            )
        return recommendations

    def update_similarity(self):
        print("Updating similarity...")
        objects = []
        files = sorted(
            file
            for file in os.listdir(self.paths.objects_raw)
            if file.endswith(".json")
        )
        for filename in files:
            json_file = self.paths.objects_raw / filename
            with json_file.open("r", encoding="utf-8") as handle:
                objects.append(json.load(handle))

        if not objects:
            print("No JSON found.")
            return

        recommendations = self.similarity_recommendations(objects)
        for filename, obj, similar in zip(files, objects, recommendations):
            obj["similar"] = similar
            out_file = self.paths.objects_raw / filename
            with out_file.open("w", encoding="utf-8") as handle:
                json.dump(obj, handle, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print("Running...")
    update = "--update" in sys.argv
    instance = AwesomePd(update)
