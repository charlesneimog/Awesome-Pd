#!/usr/bin/env python3
import os
import json
import subprocess
from typing import Dict, Any, List, Tuple

# Categorias fornecidas (deduplicadas, preservando a ordem)
CATEGORIES_RAW = [
    "Machine Learning",
    "Deep Learning",
    "Neural Networks",
    "Statical Models",
    "Algorithm Composition",
    "Procedures",
    "Logic",
    "Math",
    "Routing",
    "Envelopes",
    "LFOs",
    "Sequencers",
    "MIDI",
    "Reverb",
    "Delay",
    "Distortion",
    "Chorus/Flanger/Phaser",
    "Filters",
    "Dynamics",
    "Partial Tracking",
    "Descriptors",
    "Score Follower",
    "VST2/VST3",
    "Vamp",
    "LADSPA",
    "AU",
    "Ambisonics",
    "Binaural",
    "Subtractive",
    "Additive",
    "Granular",
    "Oscillators",
    "Physical Modeling",
    "Samplers",
    "Stochastic",
    "Data Structures",
    "File IO",
    "Networking",
    "MultiThreading",
    "Patching",
    "Multichannel",
    # Nota: "Partial Tracking" estava duplicado na lista original; removido aqui
]
_seen = set()
CATEGORIES: List[str] = []
for c in CATEGORIES_RAW:
    if c not in _seen:
        _seen.add(c)
        CATEGORIES.append(c)

PROMPT_TEMPLATE = """You are a classifier. For each category below, assign a confidence score between 0.0 and 1.0 indicating how well the object's description fits that category.

Output rules:
- Return ONLY a valid JSON object (no markdown and no extra text).
- The output must be a single JSON object whose keys are EXACTLY the categories provided (same spelling).
- The values MUST be numbers (floats) between 0.0 and 1.0 (inclusive). If it does not apply, use 0.0.
- Do not add or remove keys. Do not include comments.
- Do not include trailing commas.
- Preference for specificity: distribute confidence so that the 3 most specific and directly related categories receive the highest scores.

Categories (use as keys, exactly):
{CATEGORIES_JSON}

Object description:
\"\"\"{DESCRIPTION}\"\"\"
"""

# Limite máximo de categorias a gravar
TOP_N = int(os.environ.get("TOP_N", "3"))
# Limiar mínimo opcional para considerar categoria (0.0 a 1.0). Padrão 0.0 = sempre pega top-N.
THRESHOLD = float(os.environ.get("SCORE_THRESHOLD", "0.0"))


def build_prompt(description: str) -> str:
    return PROMPT_TEMPLATE.format(
        CATEGORIES_JSON=json.dumps(CATEGORIES, ensure_ascii=False),
        DESCRIPTION=description.strip(),
    )


def run_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Executa o Gemini CLI em modo não interativo e retorna o stdout como string.
    Stderr é suprimido para evitar warnings/logs.
    """
    env = os.environ.copy()
    env["NODE_NO_WARNINGS"] = "1"  # silencia DeprecationWarning do Node
    env["NO_COLOR"] = "1"

    cmd = [
        "gemini",
        "-m",
        model,
        "--approval-mode",
        "yolo",  # evitar travas caso haja ferramentas
        "-p",
        prompt,
    ]
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        env=env,
        check=False,
    )
    return result.stdout.strip()


def extract_json_maybe_messy(text: str) -> Dict[str, Any]:
    """
    Tenta json.loads direto; se falhar, extrai o primeiro bloco {...} contíguo do stdout.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        snippet = text[start : end + 1]
        try:
            return json.loads(snippet)
        except json.JSONDecodeError:
            pass

    raise ValueError("Não foi possível extrair um JSON válido da saída do Gemini.")


def coerce_score(v: Any) -> float:
    """
    Converte o valor retornado pelo modelo em float [0.0, 1.0].
    Aceita bool (True=1.0/False=0.0), int/float, ou string com número.
    """
    if isinstance(v, bool):
        val = 1.0 if v else 0.0
    elif isinstance(v, (int, float)):
        val = float(v)
    elif isinstance(v, str):
        try:
            val = float(v.strip())
        except Exception:
            val = 0.0
    else:
        val = 0.0
    # Clamp para [0.0, 1.0]
    if val < 0.0:
        val = 0.0
    if val > 1.0:
        val = 1.0
    return val


def select_top_categories(
    score_map: Dict[str, Any], limit: int = TOP_N, threshold: float = THRESHOLD
) -> List[str]:
    """
    Seleciona até 'limit' categorias com maior score, aplicando um limiar mínimo.
    Empate é resolvido pela ordem definida em CATEGORIES (estável e determinística).
    """
    scored: List[Tuple[str, float, int]] = []
    for idx, cat in enumerate(CATEGORIES):
        score = coerce_score(score_map.get(cat, 0.0))
        if score >= threshold:
            scored.append((cat, score, idx))

    # Ordena por score desc, e em empate, pela ordem original (idx asc)
    scored.sort(key=lambda t: (-t[1], t[2]))

    top = [cat for cat, _score, _idx in scored[: max(0, limit)]]
    return top


def process_objects(
    dir_path: str = "../docs/objects", model: str = "gemini-2.5-flash"
) -> None:
    try:
        files = os.listdir(dir_path)
    except FileNotFoundError:
        print(f"[ERRO] Diretório não encontrado: {dir_path}")
        return

    for fname in files:
        if not fname.endswith(".json"):
            continue

        json_path = os.path.join(dir_path, fname)
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[ERRO] Falha ao ler {fname}: {e}")
            continue

        # Processar apenas quando categories está vazio (ou ausente)
        cats = data.get("categories", [])
        if isinstance(cats, list) and len(cats) > 0:
            continue

        description = (data.get("description") or "").strip()
        if not description:
            print(f"[AVISO] Sem descrição em {fname}; mantendo categories como [].")
            continue

        # Monta prompt e chama Gemini
        prompt = build_prompt(description)
        stdout = run_gemini(prompt, model=model)

        try:
            score_map = extract_json_maybe_messy(stdout)
        except Exception as e:
            print(f"[ERRO] Falha ao extrair JSON para {fname}: {e}")
            print("Saída recebida:")
            print(stdout)
            continue

        # Verifica chaves
        missing = [c for c in CATEGORIES if c not in score_map]
        extras = [k for k in score_map.keys() if k not in CATEGORIES]
        if missing or extras:
            print(
                f"[ERRO] JSON inválido para {fname}: faltando={missing} extras={extras}"
            )
            print("JSON recebido:")
            print(json.dumps(score_map, ensure_ascii=False, indent=2))
            continue

        # Seleciona top-N (máx 3) acima do threshold
        selected = select_top_categories(score_map, limit=TOP_N, threshold=THRESHOLD)

        data["categories"] = selected
        try:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write("\n")
        except Exception as e:
            print(f"[ERRO] Falha ao salvar {fname}: {e}")
            continue

        resumo = ", ".join(selected) if selected else "nenhuma (abaixo do limiar)"
        print(f"[OK] {fname} -> {resumo}")


if __name__ == "__main__":
    # Ajuste o caminho/modelo/limiar via env vars se quiser:
    #   TOP_N=3 SCORE_THRESHOLD=0.0 python3 classify_objects.py
    process_objects("../docs/objects", model="gemini-2.5-flash")
