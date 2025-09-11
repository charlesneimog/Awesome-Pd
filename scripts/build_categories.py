import json
import os
import platform


# Detectar sistema operacional para limpar terminal
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# --- Carregar estrutura antiga ---
with open("../docs/submit-external/categories.json", "r", encoding="utf-8") as f:
    old_data = json.load(f)

# --- Estrutura nova (esqueleto vazio) ---
new_structure = {
    "AI": {
        "Machine Learning": [],
        "Deep Learning": [],
        "Neural Networks": [],
        "Statistical Models": [],
    },
    "Composition": {
        "Algorithmic": [],
        "Procedural": [],
        "Stochastic / Probabilistic": [],
        "Score-based": [],
    },
    "Control": {
        "Logic": [],
        "Math": [],
        "Routing": [],
        "Envelopes": [],
        "LFOs": [],
        "Sequencers": [],
        "MIDI": [],
    },
    "Effects": {
        "Reverb": [],
        "Delay": [],
        "Distortion": [],
        "Chorus/Flanger/Phaser": [],
        "Filters": [],
        "Dynamics": [],
    },
    "MIR / Analysis": {"Partial Tracking": [], "Descriptors": [], "Score Follower": []},
    "Synthesis": {
        "Subtractive": [],
        "Additive": [],
        "Granular": [],
        "Oscillators": [],
        "Physical Modeling": [],
        "Samplers": [],
        "Stochastic": [],
        "Spectral / Resynthesis": [],
    },
    "Analysis / Transform": {"FFT": [], "Spectral Processing": [], "Wavelets": []},
    "Plugins": {"VST2/VST3": [], "Vamp": [], "LADSPA": [], "AU": []},
    "Spatialization": {"Ambisonics": [], "Binaural": [], "VBAP": []},
    "I/O": {
        "File I/O": [],
        "Audio I/O": [],
        "Control I/O": [],
        "Networking": [],
        "OSC": [],
    },
    "Utilities": {
        "General Utilities": [],
        "Data Structures": [],
        "MultiThreading": [],
        "Patching": [],
        "Multichannel": [],
        "Text": [],
        "Debugging": [],
    },
    "Interfaces": {"GUI": [], "Graphics": []},
    "Scripting": {"Python": [], "Lua": [], "Others": []},
}

# Flatten das categorias novas para facilitar a escolha
available_subcats = []
for cat, subs in new_structure.items():
    if isinstance(subs, dict):
        for sub in subs.keys():
            available_subcats.append((cat, sub))


# Função para perguntar ao usuário
def ask_mapping(old_subcat):
    clear_screen()
    print(f"Categoria antiga encontrada: '{old_subcat}'\n")
    print("Categorias disponíveis no novo JSON:")
    for i, (cat, sub) in enumerate(available_subcats, 1):
        print(f"{i}. {cat} → {sub}")
    print(f"{len(available_subcats)+1}. PULAR (não mapear)")

    while True:
        try:
            choice = int(input("\nEscolha o número correspondente: "))
            if 1 <= choice <= len(available_subcats):
                return available_subcats[choice - 1]
            elif choice == len(available_subcats) + 1:
                return None
            clear_screen()
        except ValueError:
            pass
        print("Entrada inválida, tente novamente.")


# --- Transferência interativa ---
for old_category, subcats in old_data.items():
    if isinstance(subcats, dict):
        for old_subcat, objects in subcats.items():
            mapping = ask_mapping(old_subcat)
            if mapping is not None:
                new_cat, new_subcat = mapping
                new_structure[new_cat][new_subcat].extend(objects)

# --- Salvar resultado ---
with open("new_structure.json", "w", encoding="utf-8") as f:
    json.dump(new_structure, f, indent=4, ensure_ascii=False)

clear_screen()
print("✅ Migração concluída! Arquivo salvo em 'new_structure.json'")
