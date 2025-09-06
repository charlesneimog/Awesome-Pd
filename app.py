import json
import os
import re
from html import escape
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlparse
import sys

import requests
import yaml


class AwesomePd:
    """
    Orchestrates:
    - Reading open issues to ingest JSON payloads describing objects/externals.
    - Generating Markdown pages for each object in docs/objects/*.md.
    - Optionally updating categories.json and mkdocs.yml navigation.
    """

    UPDATE_CATEGORIES_AND_MKDOCS = False

    DEV_TOOLS = {
        "pd.cmake": "devs/pd.cmake.md",
        "pd-lib-builder": "devs/pdlibbuilder.md",
    }
    WEB_TOOLS = {
        "pd4web": "web/pd4web.md",
        "pdwebparty": "web/pdwebparty.md",
    }
    TOOLS = {
        "deken": "deken.md",
    }
    OS_ICON_MAP = {
        "Windows": ":fontawesome-brands-windows:",
        "Mac": ":fontawesome-brands-apple:",
        "Linux": ":fontawesome-brands-linux:",
    }

    # This is intentionally not reused in create_markdowns to preserve the exact
    # original Markdown output including whitespace and indentation.
    COMMENT_SYSTEM = """
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

    THIS_DIR = os.path.dirname(__file__)

    def __init__(self, update_docs: bool = False) -> None:
        with open("docs/submit-external/categories.json", "r", encoding="utf-8") as f:
            self.objects: Dict[str, Union[dict, list]] = json.load(f)
        with open("mkdocs.yml", "r", encoding="utf-8") as f:
            self.config = yaml.load(f, Loader=yaml.UnsafeLoader)

        self.UPDATE_CATEGORIES_AND_MKDOCS = update_docs
        if update_docs:
            self.home_update()
        else:
            self.github_actions()

    # --------------------------
    # GitHub Issues Integration
    # --------------------------

    def _get_open_issues(self) -> List[dict]:
        owner = "charlesneimog"
        repo = "Awesome-Pd"
        url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
        headers = {"Accept": "application/vnd.github+json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def github_actions(self) -> None:
        """
        Runs in CI mode: fetch open issues, ingest new JSON object definitions,
        and regenerate Markdown after each issue processing. The sequence/order
        is preserved to ensure identical side effects as the original script.
        """
        issues = self._get_open_issues()
        for issue in issues:
            self.check_new_issues(issue)
            self.create_markdowns()

    # --------------------------
    # Rendering Helpers
    # --------------------------

    def youtube_embed(self, url: str) -> str:
        """Return a YouTube iframe embed for any YouTube watch URL."""
        query = parse_qs(urlparse(url).query)
        video_id = query.get("v", [""])[0]
        if not video_id:
            raise Exception(f"Not possible parse the video {video_id}")
        return f"""<iframe style="border-radius: 8px" width="560" height="315"
        src="https://www.youtube.com/embed/{video_id}"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""

    # --------------------------
    # Markdown Generation
    # --------------------------

    def _build_info_lines(self, project: dict) -> List[str]:
        """
        Builds the bullet lines for the info grid. The output must be bit-for-bit
        identical to the original implementation.
        """
        lines: List[str] = []

        if project.get("download_link") or project.get("available_on_deken"):
            deken_text = (
                " or use [Deken](../deken.md)."
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
                    f":octicons-download-16: __Download__ Use [Deken](../deken.md)."
                )
            if project.get("library_name"):
                download_line += f"  <p>_Found inside <code>{project['library_name']}</code> library._</p>"
            lines.append(f"- {download_line}")

        if project.get("developers"):
            lines.append(
                f"- :fontawesome-brands-dev: Developed by **{', '.join(project['developers'])}**."
            )

        if project.get("bug_reports"):
            lines.append(
                f"- :fontawesome-brands-github: __Report Bugs/Errors__ [here]({project['bug_reports']})!"
            )

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
        md = '<h3>Articles</h3>\n\n<div class="grid cards" markdown>\n'
        for a in project["articles"]:
            md += (
                f"- :octicons-book-24: \n"
                f"    <h4>{escape(a['title'])}</h4>\n"
                f"    *by {', '.join(map(escape, a['authors']))}*\n\n"
                f"    [Link]({a['link']})\n"
            )
        md += "</div>\n\n"
        return md

    def _render_videos(self, project: dict) -> str:
        if not project.get("videos"):
            return ""
        md = '---\n<h3>Videos</h3>\n\n<div style="display: flex; justify-content: center; gap: 20px;">\n'
        for v in project["videos"]:
            md += f"    {self.youtube_embed(v['link'])}\n"
        md += "</div>\n\n"
        return md

    def _render_musics(self, project: dict) -> str:
        if not project.get("musics"):
            return ""
        md = '---\n<h3>Music</h3>\n\n<div style="display: flex; justify-content: center; gap: 20px;">\n'
        for m in project["musics"]:
            md += f"    {self.youtube_embed(m['link'])}\n"
        md += "</div>\n\n---\n"
        return md

    def _render_comments_block(self) -> str:
        """
        Returns the comments block string exactly as in the original code.
        Do not alter whitespace to preserve identical output.
        """
        return """\n
---

<h3>Comments</h3>

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

    def _render_contributors(self, contributors: List[str]) -> str:
        """
        Returns the contributors block exactly matching the original.
        """
        js_array = json.dumps(contributors)
        return f"""
<h3>Contributors</h3>

<div id="avatars"></div>

<script>
const nicknames = {js_array};
const container = document.getElementById('avatars');
nicknames.forEach(nick => {{
  const link = document.createElement('a');
  link.href = `https://github.com/${{nick}}`;
  link.target = '_blank'; // opens in new tab
  const img = document.createElement('img');
  img.src = `https://github.com/${{nick}}.png`;
  img.alt = nick;
  img.className = 'avatar';
  link.appendChild(img);
  container.appendChild(link);
}});
</script>
    """

    def create_markdowns(self) -> None:
        """
        Iterate over docs/objects/*.json and produce corresponding .md files.
        Output must be identical to the original implementation.
        """
        json_dir = os.path.join(self.THIS_DIR, "docs/objects")
        json_files = os.listdir(json_dir)

        for json_file in json_files:
            if not json_file.endswith(".json"):
                continue

            path = os.path.join(json_dir, json_file)
            with open(path, "r", encoding="utf-8") as f:
                project = json.load(f)

            title = project.get("title", "")
            description = project.get("description", "")

            md = f"# {title}\n\n{description}\n\n---\n"

            # Info lines inside grid
            lines = self._build_info_lines(project)
            if lines:
                md += (
                    f'<div class="grid cards" markdown>\n'
                    + "\n".join(lines)
                    + "\n</div>\n\n"
                )

            # Articles / Videos / Music
            md += self._render_articles(project)
            md += self._render_videos(project)
            md += self._render_musics(project)

            # Comments block (exact copy)
            md += self._render_comments_block()

            # Contributors block (exact copy)
            contributors: List[str] = project["contributors"]
            md += self._render_contributors(contributors)

            # Save to file (same path/behavior)
            output_path = os.path.join(
                self.THIS_DIR, "docs/objects", json_file.replace(".json", ".md")
            )
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as out_file:
                out_file.write(md)

    # --------------------------
    # Issue Payload Ingestion
    # --------------------------

    def check_new_issues(self, issue: dict) -> None:
        """
        Parse the JSON fenced code block in the issue body, ensure the creator is
        in contributors, save the JSON under docs/objects/{title}.json, and
        optionally add the object to categories/mkdocs navigation.
        """
        text = issue["body"]
        creator = issue["user"]["login"]

        pattern = re.compile(r"```json(?:\w+)?\n(.*?)```", re.DOTALL)
        matches = re.findall(pattern, text)
        if len(matches) < 1:
            return

        json_file = json.loads(matches[0])
        if creator not in json_file["contributors"]:
            json_file["contributors"].append(creator)

        # Save JSON file once per category (matches original behavior)
        for category in json_file["categories"]:
            obj_name = json_file["title"]
            output_dir = os.path.join(self.THIS_DIR, "docs", "objects")
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            with open(
                os.path.join(output_dir, obj_name + ".json"), "w", encoding="utf-8"
            ) as f:
                json.dump(json_file, f, indent=4)

            if self.UPDATE_CATEGORIES_AND_MKDOCS:
                if self.found_category(category, {obj_name: f"objects/{obj_name}.md"}):
                    print("Adding object", obj_name)
                    with open(
                        "docs/submit-external/categories.json", "w", encoding="utf-8"
                    ) as f:
                        json.dump(self.objects, f, indent=4, ensure_ascii=False)
                else:
                    raise Exception(f"Categoria '{category}' não encontrada")

    # --------------------------
    # Navigation Helpers
    # --------------------------

    def dict_to_nav(self, d: dict) -> list:
        """
        Convert a nested dict to a mkdocs 'nav' list structure, preserving
        the same shape as the original implementation.
        """
        nav_list = []
        for key, value in d.items():
            if isinstance(value, dict):
                nav_list.append({key: self.dict_to_nav(value)})
            else:
                nav_list.append({key: value})
        return nav_list

    def found_category(self, target_key: str, new_data: dict, obj: dict = None) -> bool:
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

    def home_update(self) -> None:
        """
        End-to-end update flow:
        - Refresh issues and save new object JSONs.
        - Generate all markdowns for objects.
        - Build library pages and mkdocs navigation.
        """
        print("Updating all")

        if self.objects is None or self.config is None:
            raise Exception("Error to open objects or config")

        NavItem = Union[str, Dict[str, object]]
        nav: List[NavItem] = ["index.md"]
        nav.append({"Submit Missing Externals": "submit.md"})

        # Process open issues (same as original)
        issues = self._get_open_issues()
        for issue in issues:
            self.check_new_issues(issue)

        # Regenerate Markdown pages
        self.create_markdowns()

        # Build "Objects & Abstractions" navigation
        nav.append({"Objects & Abstractions": self.dict_to_nav(self.objects)})

        # Build Libraries pages + map
        libraries: Dict[str, List[List[str]]] = {}
        all_objects: List[str] = []

        for root, _, files in os.walk(os.path.join(self.THIS_DIR, "docs", "objects")):
            for filename in files:
                filepath = os.path.join(root, filename)
                if filepath.endswith(".json"):
                    all_objects.append(filename.replace(".json", ""))
                    with open(filepath, "r", encoding="utf-8") as f:
                        object_json = json.load(f)
                        if object_json["part_of_library"] is True:
                            libname = object_json["library_name"]
                            if libname != "":
                                objname = object_json["title"]
                                description = (
                                    object_json["description"].split(". ")[0] + "."
                                )
                                if libname not in libraries:
                                    libraries[libname] = []
                                libraries[libname].append([objname, description])

        with open("docs/all_objects.json", "w", encoding="utf-8") as f:
            json.dump(all_objects, f, indent=4, ensure_ascii=False)

        nav_libs: Dict[str, str] = {}
        for lib in libraries:
            libmarkdownfile = f'# {lib} \n\n<div class="grid cards" markdown>\n'
            objects_list = libraries[lib]
            for obj in objects_list:
                libmarkdownfile += f"- :material-tune: [__{obj[0]}__](../objects/{obj[0]}.md) {obj[1]}\n"
            libmarkdownfile += "</div>"
            with open(
                os.path.join(self.THIS_DIR, "docs", "libraries", lib + ".md"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(libmarkdownfile)
                nav_libs[lib] = f"libraries/{lib}.md"

        # Append remaining nav sections (same ordering)
        nav.append({"Libraries": self.dict_to_nav(nav_libs)})
        nav.append({"Web": self.dict_to_nav(self.WEB_TOOLS)})
        nav.append({"Tools": self.dict_to_nav(self.TOOLS)})
        nav.append({"Developers": self.dict_to_nav(self.DEV_TOOLS)})

        # Update mkdocs config
        self.config["nav"] = nav
        with open("mkdocs.yml", "w", encoding="utf-8") as f:
            yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":

    print("Running...")
    update = "--update" in sys.argv
    instance = AwesomePd(update)
