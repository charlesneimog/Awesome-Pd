#!/usr/bin/env python3
import os
import json
import subprocess
import requests
from typing import Dict, Any, List, Tuple
from pprint import pprint

if not os.path.exists("deken.json"):
    url = "https://deken.puredata.info/search.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("deken.json", "w") as f:
            json.dump(data, f, indent=4)
    else:
        raise Exception(f"Request failed: {response.status_code}")
else:
    with open("deken.json", "r") as f:
        data = json.load(f)

from datetime import datetime

libraries = data["result"]["libraries"]
recent_libraries = {}

for library_name, versions_dict in libraries.items():
    all_releases = []
    for releases_list in versions_dict.values():
        all_releases.extend(releases_list)

    if all_releases:
        try:
            # Encontrar o release mais recente desta biblioteca
            most_recent = max(all_releases, key=lambda x: x.get("timestamp", "0"))

            # Verificar se o timestamp é depois de 2021
            timestamp_str = most_recent.get("timestamp")
            if timestamp_str:
                # Converter string para datetime
                timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

                # Verificar se é depois de 31 de dezembro de 2021
                if timestamp_dt.year > 2021:
                    recent_libraries[library_name] = most_recent
                # Se for 2021, verificar se é depois de 31 de dezembro
                elif (
                    timestamp_dt.year == 2021
                    and timestamp_dt.month == 12
                    and timestamp_dt.day == 31
                ):
                    recent_libraries[library_name] = most_recent

        except (ValueError, TypeError, KeyError):
            pass

# Agora recent_libraries contém apenas bibliotecas atualizadas depois de 2021
print("Bibliotecas atualizadas depois de 2021:")
for library_name, release in recent_libraries.items():
    url = release["url"]
    output_file = library_name + ".zip"
    with open(output_file, "wb") as f:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # fail if request fails
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
