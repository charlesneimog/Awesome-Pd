import os
import requests
import re
import json
import yaml
from typing import Union
from html import escape
from urllib.parse import urlparse, parse_qs

# Change this to update the categories (just on local device)
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

MARKDOWN_TEMPLATE = '''

'''

PAPER_TEMPLATE = '''
'''
VIDEO_TEMPLATE = '''
'''
MUSIC_TEMPLATE = '''
'''

THIS_DIR = os.path.dirname(__file__)
OS_ICON_MAP = {
    "Windows": ":fontawesome-brands-windows:",
    "Mac": ":fontawesome-brands-apple:",
    "Linux": ":fontawesome-brands-linux:",
}


def youtube_embed(url):
    """Return a YouTube iframe embed for any YouTube watch URL."""
    query = parse_qs(urlparse(url).query)
    video_id = query.get("v", [""])[0]  # get the first 'v' parameter
    if not video_id:
        raise Exception(f"Not possible parse the video {video_id}")
    return f'''<iframe style="border-radius: 8px" width="560" height="315"
    src="https://www.youtube.com/embed/{video_id}"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'''

def create_markdowns():
    json_files = os.listdir(os.path.join(THIS_DIR, "docs/objects"))
    for json_file in json_files:
        if not json_file.endswith(".json"):
            continue
        path = os.path.join(THIS_DIR, "docs/objects", json_file)
        with open(path) as f:
            project = json.load(f)

        # Build OS icons string
        os_icons = " ".join(OS_ICON_MAP.get(os, os) for os in project.get("runs_on", []))

        # Start Markdown
        md = f"# {project.get('title', '')}\n\n{project.get('description', '')}\n\n---\n"

        # Info lines
        lines = []

        if project.get("download_link") or project.get("available_on_deken"):
            deken_text = " or use [Deken](../deken.md)." if project.get("available_on_deken") else ""
            dl_text = f"[here]({project['download_link']})" if project.get("download_link") else ""
            if project.get("download_link"):
                download_line = f":octicons-download-16: __Download__ {dl_text}{deken_text}."
            else:
                download_line = f":octicons-download-16: __Download__ Use [Deken](../deken.md)."
            if project.get("library_name"):
                download_line += f"  <p>_Found inside <code>{project['library_name']}</code> library._</p>"
            lines.append(f"- {download_line}")

        if project.get("developers"):
            lines.append(f"- :fontawesome-brands-dev: Developed by **{', '.join(project['developers'])}**.")

        if project.get("bug_reports"):
            lines.append(f"- :fontawesome-brands-github: __Report Bugs/Errors__ [here]({project['bug_reports']})!")

        if project.get("runs_on"):
            lines.append(f"- :fontawesome-solid-computer: __Available__ for {os_icons}.")

        if lines:
            md += f'<div class="grid cards" markdown>\n' + "\n".join(lines) + "\n</div>\n\n"

        # Articles
        if project.get("articles"):
            md += "<h3>Articles</h3>\n\n<div class=\"grid cards\" markdown>\n"
            for a in project["articles"]:
                md += f"- :octicons-book-24: \n    <h4>{escape(a['title'])}</h4>\n    *by {', '.join(map(escape, a['authors']))}*\n\n    [Link]({a['link']})\n"
            md += "</div>\n\n"

        # Videos
        if project.get("videos"):
            md += "---\n<h3>Videos</h3>\n\n<div style=\"display: flex; justify-content: center; gap: 20px;\">\n"
            for v in project["videos"]:
                md += f"    {youtube_embed(v['link'])}\n"
            md += "</div>\n\n"

        # Music
        if project.get("musics"):
            md += "---\n<h3>Music</h3>\n\n<div style=\"display: flex; justify-content: center; gap: 20px;\">\n"
            for m in project["musics"]:
                md += f"    {youtube_embed(m['link'])}\n"
            md += "</div>\n\n---\n"

        # Comment system
        md += '''\n
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
'''
        # list
        contributors = project["contributors"]
        js_array = json.dumps(contributors)  # Converts Python list to JS array
        md += f'''
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
'''
        # Optionally, save to file
        output_path = os.path.join(THIS_DIR, "docs/objects", json_file.replace(".json", ".md"))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as out_file:
            out_file.write(md)
    


def check_new_issues(issue_body):
    # Replace these with your own values
    owner = "charlesneimog"
    repo = "Awesome-Pd"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    issues = response.json()
    for issue in issues:
        text = issue["body"]
        creator = issue["user"]["login"]  # GitHub username of the issue creator

        # json
        pattern = re.compile(r"```json(?:\w+)?\n(.*?)```", re.DOTALL)
        matches = re.findall(pattern, text)
        if len(matches) < 1:
            continue
        json_file = json.loads(matches[0])
        if creator not in json_file["contributors"]:
            json_file["contributors"].append(creator)

        # save json file
        for category in json_file["categories"]:
            obj_name = json_file["title"]
            output_dir = os.path.join(THIS_DIR, "docs", "objects")
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            # save json files
            with open(os.path.join(output_dir, obj_name + ".json"), "w") as f:
                json.dump(json_file, f, indent=4)

            if UPDATE_CATEGORIES_AND_MKDOCS:
                if found_category(category, {obj_name: f"objects/{obj_name}.md"}):
                    print("Adding object", obj_name)
                    with open("docs/submit-external/categories.json", "w") as f:
                        json.dump(objects, f, indent=4, ensure_ascii=False)
                else:
                    raise Exception(f"Categoria '{category}' não encontrada")




def dict_to_nav(d: dict) -> list:
    nav_list = []
    for key, value in d.items():
        if isinstance(value, dict):
            nav_list.append({key: dict_to_nav(value)})  # recurse
        else:
            nav_list.append({key: value})  # leaf (file path or [])
    return nav_list


def found_category(target_key: str, new_data: dict, obj=None) -> bool:
    """
    Procura target_key dentro de obj (dict aninhado) e insere new_data
    apenas dentro da lista correspondente a target_key.
    """
    if obj is None:
        obj = objects

    for key, value in obj.items():
        # Só adiciona se for exatamente a key que queremos
        if key == target_key:
            if isinstance(value, list):
                if new_data not in value:
                    value.append(new_data)
                return True
            else:
                raise ValueError(
                    f"Categoria '{target_key}' não é uma lista em categories.json"
                )

        # Se o valor for dict, desce um nível
        elif isinstance(value, dict):
            if found_category(target_key, new_data, value):
                return True

    return False

create_markdowns()

# ╭──────────────────────────────────────╮
# │        Search for Open Issues        │
# ╰──────────────────────────────────────╯
if not UPDATE_CATEGORIES_AND_MKDOCS:
    print("Just checking new issues")
    # Replace these with your own values
    owner = "charlesneimog"
    repo = "Awesome-Pd"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    issues = response.json()
    for issue in issues:
        check_new_issues(issue)
        create_markdowns()


else:
    print("Updating all")
    objects = None
    config = None

    with open("docs/submit-external/categories.json", "r") as f:
        objects = json.load(f)
    with open("mkdocs.yml", "r") as f:
        config = yaml.load(f, Loader=yaml.UnsafeLoader)

    if objects is None or config is None:
        raise Exception("Error to open objects or config")

    NavItem = Union[str, dict[str, object]]
    nav: list[NavItem] = ["index.md"]
    nav.append({"Submit Missing Externals": "submit.md"})

    # SAVING JSON
    owner = "charlesneimog"
    repo = "Awesome-Pd"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    issues = response.json()
    for issue in issues:
        check_new_issues(issue)

    create_markdowns()

    # Save abs
    nav.append({"Objects & Abstractions": dict_to_nav(objects)})
    libraries = {}

    all_objects = []
    for root, dirs, files in os.walk(os.path.join(THIS_DIR, "docs", "objects")):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.endswith(".json"):
                all_objects.append(filename.replace(".json", ""))
                with open(filepath, "r") as f:
                    object_json = json.load(f)
                    if object_json["part_of_library"] == True:
                        libname = object_json["library_name"]
                        if libname != "":
                            objname = object_json["title"]
                            description = (
                                object_json["description"].split(". ")[0] + "."
                            )
                            if libname not in libraries:
                                libraries[libname] = []
                            libraries[libname].append([objname, description])

    with open("docs/all_objects.json", "w") as f:
        json.dump(all_objects, f, indent=4, ensure_ascii=False)

    nav_libs = {}
    for lib in libraries:
        libmarkdownfile = f'# {lib} \n\n<div class="grid cards" markdown>\n'
        objects_list = libraries[lib]
        for obj in objects_list:
            libmarkdownfile += (
                f"- :material-tune: [__{obj[0]}__](../objects/{obj[0]}.md) {obj[1]}\n"
            )
        libmarkdownfile += "</div>"
        with open(os.path.join(THIS_DIR, "docs", "libraries", lib + ".md"), "w") as f:
            f.write(libmarkdownfile)
            nav_libs[lib] = f"libraries/{lib}.md"

    nav.append({"Libraries": dict_to_nav(nav_libs)})
    nav.append({"Web": dict_to_nav(WEB_TOOLS)})
    nav.append({"Tools": dict_to_nav(TOOLS)})
    nav.append({"Developers": dict_to_nav(DEV_TOOLS)})

    config["nav"] = nav

    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
