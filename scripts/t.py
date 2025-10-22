import os
import json

all_json = os.listdir("./../docs/objects_raw")

for filename in all_json:
    filepath = f"./../docs/objects_raw/{filename}"
    with open(filepath, "r") as file:
        data = json.load(file)

    # Update condition
    if data.get("library_name") == "flucoma" and "porres" in data.get("download_link", ""):
        data["library_name"] = "pd-psycho"

        print("update "+filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)



