import os
import requests
import re
import json
import yaml
from typing import Union

# Replace these with your own values
owner = "charlesneimog"
repo = "Awesome-Pd"
issue_number = 16

THIS_DIR = os.path.dirname(__file__)

LIBRARIES = {
    "cyclone": "libraries/cyclone.md",
    "else": "libraries/else.md",
    "neimog": "libraries/neimog.md",
}

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


with open("docs/submit/categories.json", "r") as f:
    objects = json.load(f)


# ╭──────────────────────────────────────╮
# │        Search for Open Issues        │
# ╰──────────────────────────────────────╯

url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
headers = {"Accept": "application/vnd.github+json"}
response = requests.get(url, headers=headers)
response.raise_for_status()
issues = response.json()

for issue in issues:
    text = issue["body"]

    # json + markdown
    pattern = re.compile(r"```(?:\w+)?\n(.*?)```", re.DOTALL)
    matches = re.findall(pattern, text)

    if len(matches) < 2:
        exit(0)

    json_file = json.loads(matches[0])
    md = matches[1]
    required_keys = [
        "title",
        "description",
        "runs_on",
        "download_link",
        "available_on_deken",
        "categories",
        "bug_reports",
        "developers",
        "part_of_library",
        "library_name",
        "articles",
        "videos",
        "musics",
    ]

    #
    for k in required_keys:
        if k not in json_file:
            exit(0)

    OUTPUT_DIR = ""

    library = json_file["library_name"]
    LIB_OUTPUT = OUTPUT_DIR = os.path.join(
        THIS_DIR, "docs", "libraries", library + ".json"
    )

    if os.path.exists("mkdocs.yml"):
        objects = ""

        with open("docs/submit/categories.json", "r") as f:
            objects = json.load(f)
        with open("mkdocs.yml", "r") as f:
            config = yaml.load(f, Loader=yaml.UnsafeLoader)

        NavItem = Union[str, dict[str, object]]
        nav: list[NavItem] = ["index.md"]

        nav.append({"Objects": dict_to_nav(objects)})
        nav.append({"Libraries": dict_to_nav(LIBRARIES)})
        nav.append({"Developers": dict_to_nav(DEV_TOOLS)})
        nav.append({"Web": dict_to_nav(WEB_TOOLS)})
        nav.append({"Tools": dict_to_nav(TOOLS)})

        for category in json_file["categories"]:
            obj_name = json_file["title"]
            index_text = f"# {category}\n\n"
            index_text += '<div class="grid cards" markdown>\n'
            OUTPUT_DIR = os.path.join(THIS_DIR, "docs", "objects")
            if not os.path.exists(OUTPUT_DIR):
                os.mkdir(OUTPUT_DIR)
            with open(os.path.join(OUTPUT_DIR, obj_name + ".md"), "w") as f:
                f.write(md + "\n" + COMMENT_SYSTEM)

            if found_category(category, {obj_name: f"objects/{obj_name}.md"}):
                print("Adding object", obj_name)
                with open("docs/submit/categories.json", "w") as f:
                    json.dump(objects, f, indent=4, ensure_ascii=False)
            else:
                raise Exception(f"Categoria '{category}' não encontrada")

        config["nav"] = nav

        with open("mkdocs.yml", "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
