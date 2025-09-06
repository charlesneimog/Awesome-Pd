"""
This will retrieve all texts from a Pd patch
"""

import os

DIR = "/home/neimog/Documents/Pd/externals/else"

# garante que a pasta existe
os.makedirs("to-do", exist_ok=True)

# percorre todos os arquivos na pasta
for file in os.listdir(DIR):
    if not file.endswith("-help.pd"):
        continue

    file_path = os.path.join(DIR, file)
    print("Processing:", file_path)

    # tenta ler como UTF-8, se falhar usa latin-1
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as f:
            data = f.readlines()

    # coleta as linhas de texto do patch
    lines = []

    collecting = False
    current_text = []

    for line in data:
        token = line.split()
        if not token:
            continue

        # início de um objeto #X text
        if token[0] == "#X" and token[1] == "text":
            collecting = True
            # ignora os dois tokens de coordenadas
            current_text = token[4:]
            # verifica se já termina aqui
            last = current_text[-1] if current_text else ""
            if last.endswith(",") or last.endswith(";"):
                if not last.endswith("\\,") and not last.endswith("\\;"):
                    lines.append(" ".join(current_text))
                    collecting = False
                    current_text = []
            continue

        # se estamos coletando, continua adicionando tokens
        if collecting:
            current_text.extend(token)
            last = current_text[-1]
            if last.endswith(",") or last.endswith(";"):
                if not last.endswith("\\,") and not last.endswith("\\;"):
                    lines.append(" ".join(current_text))
                    collecting = False
                    current_text = []

    # escreve o resultado no .md
    out_file = os.path.join("to-do", file.replace("-help.pd", ".md"))
    with open(
        out_file,
        "w",
    ) as f:
        f.write("\n".join(lines))
