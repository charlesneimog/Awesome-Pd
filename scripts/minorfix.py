import os
import json

objects = "/home/neimog/Documents/Git/Awesome-PD/docs/objects"

for file in os.listdir(objects):
    if file.endswith(".json"):
        json_file = objects + f"/{file}"
        with open(json_file, "r") as f:
            data = json.load(f)

        if data["library_name"] == "timbreIDLib":
            data["part_of_library"] = True
            data["articles"] = {
                "title": "A Timbre Analysis And Classification Toolkit For Pure Data",
                "authors": ["William Brent"],
                "link": "http://hdl.handle.net/2027/spo.bbp2372.2010.044",
            }

            with open(json_file, "w") as f:
                json.dump(data, f, indent=4)
