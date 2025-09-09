import os
import json

MAIN_DIR = "../docs/objects/"
files = os.listdir(MAIN_DIR)


categories = {}
for file in files:
    if file.endswith(".json"):
        with open(f"{MAIN_DIR}{file}", "r") as f:
            data = json.load(f)

        # TODO: replace by get
        name = data["title"]
        description = data["description"].split(". ")[0] + "."
        for category in data["categories"]:
            if category not in categories:
                categories[category] = []
            categories[category].append([name, description])

for key in categories.keys():
    objects = categories[key]
    key = key.replace(" ", "_")
    key = key.replace("/", "_")
    key = key.lower()
    lines = []
    for obj in objects:
        lines.append(
            f"- :material-tune: [__{obj[0]}__](../objects/{obj[0]}.md) {obj[1]}\n"
        )

    md = f'<div class="grid cards" markdown>\n' + "\n".join(lines) + "\n</div>"
    with open(f"../docs/categories/{key}.md", "w") as f:
        f.write(md)
