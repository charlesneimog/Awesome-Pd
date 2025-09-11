import json

# --- Carregar modelo (estrutura esperada) ---
with open("../json.json", "r", encoding="utf-8") as f:
    model = json.load(f)

# --- Carregar JSON migrado ---
with open(
    "/home/neimog/Documents/Git/Awesome-PD/new_structure.json",
    "r",
    encoding="utf-8",
) as f:
    migrated = json.load(f)


def fill_missing(model_part, migrated_part):
    """
    Preenche categorias/subcategorias ausentes no migrated usando model como referência.
    """
    if isinstance(model_part, dict):
        if not isinstance(migrated_part, dict):
            migrated_part = {}
        for key, value in model_part.items():
            if key not in migrated_part:
                # Se for dict, chama recursivamente
                migrated_part[key] = fill_missing(
                    value, {} if isinstance(value, dict) else []
                )
            else:
                migrated_part[key] = fill_missing(value, migrated_part[key])
    elif isinstance(model_part, list):
        if not isinstance(migrated_part, list):
            migrated_part = []
    return migrated_part


# --- Executar preenchimento ---
corrected = fill_missing(model, migrated)

# --- Salvar JSON corrigido ---
with open("../new_structure_corrected.json", "w", encoding="utf-8") as f:
    json.dump(corrected, f, indent=4, ensure_ascii=False)

print("✅ Verificação concluída! Arquivo salvo como 'new_structure_corrected.json'")
