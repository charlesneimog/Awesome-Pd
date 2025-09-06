import os
import json


def update_directories():
    DIR = os.path.dirname(__file__) + "/docs/objects"
    for file in os.listdir(DIR):
        if file.endswith(".json"):
            json_file = DIR + f"/{file}"
            with open(json_file, "r") as f:
                print(f)
                data = json.load(f)
            data["contributors"] = ["charlesneimog"]
            with open(json_file, "w") as f:
                json.dump(data, f, indent=4)


update_directories()
