import json
import os
import re
from html import escape
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlparse
import sys

import requests
import yaml

# use this to add object using IA + help processor
# https://chatgpt.com/c/68bc1a52-7f84-8328-8dbb-13b4c294b3a0


class AwesomePd:
    """
    Orchestrates:
    - Reading open issues to ingest JSON payloads describing objects/externals.
    - Generating Markdown pages for each object in docs/objects/*.md.
    - Optionally updating categories.json and mkdocs.yml navigation.
    """

    UPDATE_CATEGORIES_AND_MKDOCS = False

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

        self.videos = []
        self.music = []
        self.articles = []

        self.UPDATE_CATEGORIES_AND_MKDOCS = update_docs
        if update_docs:
            self.home_update()
        else:
            self.github_actions()

        self.videos = list({item["link"]: item for item in self.videos}.values())
        self.music = list({item["link"]: item for item in self.music}.values())
        self.articles = list({item["link"]: item for item in self.articles}.values())
        with open("docs/all_videos.json", "w") as f:
            json.dump(self.videos, f, indent=4)
        with open("docs/all_music.json", "w") as f:
            json.dump(self.music, f, indent=4)
        with open("docs/all_articles.json", "w") as f:
            json.dump(self.articles, f, indent=4)

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
        obj_name = project["title"]
        if obj_name == "index":
            obj_name = project["library_name"] + "_" + obj_name

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
                    f":octicons-download-16: __Download__ via [Deken](../deken.md)."
                )
            if project.get("library_name"):
                download_line += f'  <p style="font-size: 14px">_Open `Pd` and go to `Tools`:material-arrow-right:`Find Externals`. Search for <code>{project["library_name"]}</code> and install it. Then create an object with `declare -lib {project["library_name"]} -path {project["library_name"]}`. Finally, use `{obj_name}` or any other object from `{project["library_name"]}`._</p>'

            lines.append(f"- {download_line}")

        if project.get("developers"):
            lines.append(
                f"- :fontawesome-brands-dev: Library developed mainly by **{', '.join(project['developers'])}**."
            )

        if project.get("bug_reports"):
            lines.append(
                f"- :fontawesome-solid-bug-slash: __Report Bugs/Errors__ [here]({project['bug_reports']})!"
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
            self.articles.append(a)
        md += "</div>\n\n"
        return md

    def _render_videos(self, project: dict) -> str:
        if not project.get("videos"):
            return ""
        md = '---\n<h3>Videos</h3>\n\n<div style="display: flex; justify-content: center; gap: 20px;">\n'
        for v in project["videos"]:
            self.videos.append(v)
            md += f"    {self.youtube_embed(v['link'])}\n"
        md += "</div>\n\n"
        return md

    def _render_musics(self, project: dict) -> str:
        if not project.get("musics"):
            return ""
        md = '---\n<h3>Music</h3>\n\n<div style="display: flex; justify-content: center; gap: 20px;">\n'

        for m in project["musics"]:
            self.music.append(m)
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

    # This create the markdown for each object
    def create_markdowns(self) -> None:
        """
        Iterate over docs/objects/*.json and produce corresponding .md files.
        Output must be identical to the original implementation.
        """
        json_dir = os.path.join(self.THIS_DIR, "docs/objects")
        json_files = os.listdir(json_dir)

        libraries = {}
        print("")
        for json_file in json_files:
            if not json_file.endswith(".json"):
                continue

            print(f"Creating markdown for {json_file.replace('.json', "")}")
            path = os.path.join(json_dir, json_file)
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

            if title == "index":
                title = lib + "_" + title

            description = project.get("description", "")

            md = f"# {title}\n\n{description}\n\n---\n"
            if project.get("ai", False):
                md += """
!!! info "AI Generated"
    This content was generated with the assistance of AI. If you notice any errors, please report them or submit a fix using [Submit](../submit.md). Check the prompt used [here](../prompts/helppatchai.md).\n\n---\n
"""

            # Info lines inside grid
            lines = self._build_info_lines(project)
            if lines:
                md += (
                    f'<div class="grid cards" markdown>\n'
                    + "\n".join(lines)
                    + "\n</div>"
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
            if json_file.replace(".json", "") == "index":
                json_file = f"{lib}_{json_file}"

            output_path = os.path.join(
                self.THIS_DIR, "docs/objects", json_file.replace(".json", ".md")
            )

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as out_file:
                out_file.write(md)

        # TODO: Put this in another function
        for lib in libraries:
            thislib = libraries[lib]
            file = f"docs/libraries/{lib}.json"
            if not os.path.exists(file):
                thislib["link"] = thislib["issues"].replace("issues", "")
                with open(file, "w") as f:
                    json.dump(thislib, f, indent=4)

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
        lib = json_file["library_name"]
        obj_name = json_file["title"]
        if obj_name == "index":
            obj_name = json_file["library_name"] + "_" + obj_name

        output_dir = os.path.join(self.THIS_DIR, "docs", "objects")
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        if obj_name == "index":
            obj_name = f"{lib}_{obj_name}"

        with open(
            os.path.join(output_dir, obj_name + ".json"), "w", encoding="utf-8"
        ) as f:
            json.dump(json_file, f, indent=4)

    # --------------------------
    # Navigation Helpers
    # --------------------------
    def update_main_json_of_objects(self):
        all_files = os.listdir(self.THIS_DIR + "/docs/objects")
        print()
        print("Updating main object json")
        print()
        for file in all_files:
            json_path = self.THIS_DIR + f"/docs/objects/{file}"
            if file.endswith(".json"):
                with open(json_path, "r") as f:
                    object_data = json.load(f)

                obj_name = object_data["title"]
                if obj_name == "index":
                    obj_name = object_data["library_name"] + "_" + obj_name

                categories = object_data["categories"]
                print(f"Updating json : {obj_name}")
                for category in categories:
                    if self.found_category(
                        category, {obj_name: f"objects/{obj_name}.md"}
                    ):
                        with open(
                            "docs/submit-external/categories.json",
                            "w",
                            encoding="utf-8",
                        ) as f:
                            json.dump(self.objects, f, indent=4, ensure_ascii=False)
                    else:
                        raise Exception(f"Categoria '{category}' não encontrada")

    def build_obj_abs_nav(self, d: dict) -> dict:
        """ """
        objdir = "docs/objects/"
        files = os.listdir(objdir)
        categories = {}

        for file in files:
            if file.endswith(".json"):
                with open(f"{objdir}{file}", "r") as f:
                    data = json.load(f)

                # TODO: replace by get
                name = data["title"]
                if name == "index":
                    name = data["library_name"] + "_" + name

                description = data["description"].split(". ")[0] + "."
                for category in data["categories"]:
                    if category not in categories:
                        categories[category] = []
                    categories[category].append([name, description])

        return categories

    def obj_dict_to_nav(self, d: dict) -> list:
        """
        Convert a nested dict to a mkdocs 'nav' list structure for Objects & Abstractions.
        - "Object of day" always comes first if present.
        - Dicts recurse into obj_dict_to_nav.
        - Lists collapse into a single .md entry under categories/.
        """
        nav_list = []
        if "Object of day" in d:
            value = d["Object of day"]
            if isinstance(value, dict):
                nav_list.append({"Object of day": self.obj_dict_to_nav(value)})
            else:
                nav_list.append({"Object of day": value})

        # Process the rest in sorted order, skipping the special key
        for key, value in sorted(d.items()):
            if key == "Object of day":
                continue
            if isinstance(value, dict):
                nav_list.append({key: self.obj_dict_to_nav(value)})
            elif isinstance(value, list):
                # Collapse into categories/<snake_case>.md, then append list items
                slug = key.lower().replace(" ", "_").replace("/", "_")
                category_entry = [f"categories/{slug}/index.md"] + value
                nav_list.append({key: category_entry})
            else:
                nav_list.append({key: value})

        return nav_list

    def dict_to_nav(self, d: dict) -> list:
        """
        Convert a nested dict to a mkdocs 'nav' list structure,
        ensuring "Object of day" is always first if present.
        """
        nav_list = []

        # Force "Object of day" to the front if present
        if "Object of day" in d:
            value = d["Object of day"]
            if isinstance(value, dict):
                nav_list.append({"Object of day": self.dict_to_nav(value)})
            else:
                nav_list.append({"Object of day": value})

        # Process the rest in sorted order, skipping the special key
        for key, value in sorted(d.items()):
            if key == "Object of day":
                continue
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

        # Process open issues (same as original)
        issues = self._get_open_issues()
        for issue in issues:
            self.check_new_issues(issue)

        # Regenerate Markdown pages
        self.create_markdowns()

        # update main json
        self.update_main_json_of_objects()

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
                                if objname == "index":
                                    objname = f"{libname}_{objname}"

                                description = (
                                    object_json["description"].split(". ")[0] + "."
                                )
                                if libname not in libraries:
                                    libraries[libname] = []
                                libraries[libname].append([objname, description])

        with open("docs/all_objects.json", "w", encoding="utf-8") as f:
            json.dump(all_objects, f, indent=4, ensure_ascii=False)

        # create libraries markdown files
        # update libraries
        nav_libs: Dict[str, str] = {}
        print("")
        for lib in libraries:
            print(f"Update Library page: {lib}")
            libmarkdownfile = f"---\nsearch:\n    exclude: true\n---\n\n# {lib}\n"
            with open(f"docs/libraries/{lib}.json", "r") as f:
                lib_data = json.load(f)
            libmarkdownfile += lib_data["description"]
            libmarkdownfile += """
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>\n\n"""

            url = lib_data["link"]
            parts = url.rstrip("/").split("/")

            repo_owner = parts[-2]  # "porres"
            repo_name = parts[-1]  # "pd-else"

            libmarkdownfile += f"""
<script>
async function updateList() {{
    const repoOwner = '{repo_owner}';
    const repoName = '{repo_name}';
    try {{
        const res = await fetch(`https://api.github.com/repos/${{repoOwner}}/${{repoName}}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {{
            const link = document.createElement('a');
            link.href = `https://github.com/${{user.login}}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `https://github.com/${{user.login}}.png?size=100`;
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
</script>\n\n
"""
            libmarkdownfile += '<h2>Objects</h2>\n\n<div class="grid cards" markdown>\n'
            objects_list = libraries[lib]
            for obj in sorted(objects_list):
                text = obj[1]
                # remove links
                text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
                libmarkdownfile += (
                    f"- :material-tune: [__{obj[0]}__](../objects/{obj[0]}.md) {text}\n"
                )
            libmarkdownfile += "</div>"
            with open(
                os.path.join(self.THIS_DIR, "docs", "libraries", lib + ".md"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write(libmarkdownfile)
                nav_libs[lib] = f"libraries/{lib}.md"

        # Append remaining nav sections (same ordering)
        NavItem = Union[str, Dict[str, object]]
        nav: List[NavItem] = [{"Home": "index.md"}]
        nav.append({"Submit": "submit.md"})
        nav.append({"Objects & Abstractions": self.obj_dict_to_nav(self.objects)})
        nav.append({"Libraries": self.dict_to_nav(nav_libs)})
        nav.append({"Pieces": "pieces.md"})
        nav.append({"Web": self.dict_to_nav(self.WEB_TOOLS)})
        nav.append({"Tools": self.dict_to_nav(self.TOOLS)})

        # build categories
        categories = self.build_obj_abs_nav(self.objects)
        print()
        for c in categories:
            print(f"Category being created: {c}")
            c_name = c.replace(" ", "_").replace("/", "_").lower()
            c_md = f"# {c}\n\n"
            descriptions = categories[c]
            c_md += '<div class="grid cards" markdown>\n\n'
            for d in descriptions:
                obj = d[0]
                des = d[1]
                c_md += f"- :material-tune: [__{obj}__](../../objects/{obj}.md) {des}\n"
            c_md += "\n</div>"
            os.makedirs(f"docs/categories/{c_name}/", exist_ok=True)
            with open(f"docs/categories/{c_name}/index.md", "w") as f:
                f.write(c_md)

        # Update mkdocs config
        self.config["nav"] = nav
        with open("mkdocs.yml", "w", encoding="utf-8") as f:
            yaml.dump(
                self.config, f, default_flow_style=False, sort_keys=False, indent=4
            )


if __name__ == "__main__":

    print("Running...")
    update = "--update" in sys.argv
    instance = AwesomePd(update)
