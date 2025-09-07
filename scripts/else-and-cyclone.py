import os
import re
import json


dir = os.listdir("/home/neimog/Documents/plugdata/Documentation/9.else/")


objects_that_were_not_added = []
for file in dir:
    if file.endswith("-help.pd"):
        print("===================")
        path = "/home/neimog/Documents/plugdata/Documentation/9.else/" + file
        with open(path, "r") as f:
            lines = f.readlines()

        for line in lines:
            tokens = line.split()
            if tokens[0] == "#X" and tokens[1] == "text":
                name = file.replace("-help.pd", "")
                name_len = len(name)
                if "[" + name + "]" == tokens[4][: name_len + 2]:
                    line = re.sub(
                        r"^#X\s+text\s+-?\d+(?:\.\d+)?\s+-?\d+(?:\.\d+)?\s*", "", line
                    )
                    line = re.sub(r",\s*f\s*-?\d+;$", "", line)
                    line = re.sub(r"\[([^\]]+)\]", r"`\1`", line)
                    line = line.replace(" \\,", ",")
                    test = line.replace(" ", "").replace("\n", "")
                    if test[-1] == ".":
                        description = line
                        object = {
                            "title": name,
                            "description": description,
                            "runs_on": ["Mac", "Linux", "Windows"],
                            "download_link": "",
                            "available_on_deken": True,
                            "bug_reports": "https://github.com/porres/pd-else/issues",
                            "developers": ["Alexandre Porres"],
                            "part_of_library": True,
                            "library_name": "else",
                            "categories": [],
                            "category_groups": [],
                            "articles": [],
                            "videos": [],
                            "musics": [],
                            "contributors": ["charlesneimog"],
                        }
                        with open(f"{name}.json", "w") as f:
                            json.dump(object, f, indent=4)

                    else:
                        objects_that_were_not_added.append(name)


print(objects_that_were_not_added)
