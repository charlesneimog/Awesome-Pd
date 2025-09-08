#!/usr/bin/env python3
import os
import json
import subprocess
from typing import Dict, Any, List, Tuple


LIBRARY_HELP_FILES = "/home/neimog/Documents/Pd/externals/timbreIDLib/"

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
    # Note: "Partial Tracking" appeared twice in the original list; kept only once.
]
_seen = set()
CATEGORIES: List[str] = []
for c in CATEGORIES_RAW:
    if c not in _seen:
        _seen.add(c)
        CATEGORIES.append(c)

PROMPT_TEMPLATE = """You are both a technical writer and a classifier.

Task:
1) Produce a concise, clear English description (2–3 sentences max) of the Pure Data object described by the following help patch. Focus on what the object does, its purpose, and key usage hints if they are evident. Keep it simple and practical.
2) Score ALL categories (listed below) with a confidence between 0.0 and 1.0 for how well the object's functionality fits each category.

Very important output rules:
- Return ONLY a valid JSON object (no markdown and no extra text).
- The JSON must have exactly these top-level keys:
  - "description": string
  - "scores": object mapping each category name to a float (0.0–1.0)
- The "scores" object MUST include EVERY category key exactly as provided (same spelling).
- Values in "scores" MUST be numbers (floats). If a category does not apply, use 0.0.
- Do not add or remove keys. Do not include comments.
- No trailing commas.

Categories (use as keys in "scores", exactly):
{CATEGORIES_JSON}

Object title:
{TITLE}

Help Patch (.pd text):
```pd
{PATCH_TEXT}
```
"""


def _build_prompt(title: str, patch_text: str) -> str:
    return PROMPT_TEMPLATE.format(
        CATEGORIES_JSON=json.dumps(CATEGORIES, ensure_ascii=False),
        TITLE=title.strip(),
        PATCH_TEXT=patch_text.strip(),
    )


def _run_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Runs Gemini CLI in non-interactive mode and returns stdout only.
    Assumes Gemini CLI is installed and already authenticated.
    """
    env = os.environ.copy()
    env["NODE_NO_WARNINGS"] = "1"  # silence Node warnings
    env["NO_COLOR"] = "1"  # plain output

    cmd = [
        "gemini",
        "-m",
        model,
        "--approval-mode",
        "yolo",
        "-p",
        prompt,
    ]
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,  # drop warnings/info
        text=True,
        env=env,
        check=False,
    )
    return result.stdout.strip()


def _extract_json(text: str) -> Dict[str, Any]:
    """
    Try direct json.loads; if it fails, extract the first {...} block.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        snippet = text[start : end + 1]
        return json.loads(snippet)
    raise ValueError("Could not extract valid JSON from Gemini output.")


def _coerce_score(v: Any) -> float:
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
    if val < 0.0:
        val = 0.0
    if val > 1.0:
        val = 1.0
    return val


def _select_top_categories(
    score_map: Dict[str, Any], limit: int = 3, threshold: float = 0.0
) -> List[str]:
    """
    Select up to 'limit' categories with highest scores, applying a minimum threshold.
    Stable tie-breaking by original CATEGORIES order.
    """
    scored: List[Tuple[str, float, int]] = []
    for idx, cat in enumerate(CATEGORIES):
        score = _coerce_score(score_map.get(cat, 0.0))
        if score >= threshold:
            scored.append((cat, score, idx))
    scored.sort(key=lambda t: (-t[1], t[2]))
    return [cat for cat, _s, _i in scored[:limit]]


def build_description_and_categories(
    title: str,
    help_patch_path: str,
    base_json: Dict[str, Any],
    *,
    model: str = "gemini-2.5-flash",
    top_n: int = 3,
    threshold: float = 0.0,
) -> Dict[str, Any]:
    """
    Build a concise English description and top-3 categories for a PD object using a .pd help patch.

    Parameters:
      - title: object name (e.g., "nn~").
      - help_patch_path: filesystem path to the .pd help patch (text).
      - base_json: your base JSON (fields you already have). This function sets/overwrites:
           base_json["title"], base_json["description"], base_json["categories"]
      - model: Gemini model name (default: gemini-2.5-flash).
      - top_n: maximum number of categories to store (default: 3).
      - threshold: minimum score to consider (default: 0.0).

    Returns:
      - The merged JSON dict with title, description, and categories filled in.
    """
    with open(help_patch_path, "r", encoding="utf-8") as f:
        patch_text = f.read()

    prompt = _build_prompt(title, patch_text)
    stdout = _run_gemini(prompt, model=model)
    payload = _extract_json(stdout)

    # Validate structure
    if (
        "description" not in payload
        or "scores" not in payload
        or not isinstance(payload["scores"], dict)
    ):
        raise ValueError(
            'Gemini output must contain keys: "description" (string) and "scores" (object).'
        )

    # Ensure all categories present in scores
    missing = [c for c in CATEGORIES if c not in payload["scores"]]
    extras = [k for k in payload["scores"].keys() if k not in CATEGORIES]
    if missing or extras:
        raise ValueError(f'Unexpected "scores" keys. Missing={missing} extras={extras}')

    selected = _select_top_categories(
        payload["scores"], limit=top_n, threshold=threshold
    )

    # Merge into base JSON
    out = dict(base_json)  # shallow copy
    out["title"] = title
    out["description"] = payload["description"]
    # out["categories"] = selected
    return out


# Example usage (commented):
base = {
    "runs_on": ["Mac", "Linux", "Windows"],
    "download_link": "",
    "available_on_deken": True,
    "bug_reports": "https://github.com/wbrent/timbreIDLib/issues",
    "developers": ["William Brent"],
    "part_of_library": False,
    "library_name": "timbreIDLib",
    "articles": [],
    "videos": [],
    "musics": [],
    "categories": ["Descriptors"],
    "contributors": ["charlesneimog"],
    "ai": True,
}

for help in os.listdir(LIBRARY_HELP_FILES):
    if help.endswith("-help.pd"):
        file = os.path.join(LIBRARY_HELP_FILES, help)
        print(f"Processing {help}...")
        name = help.replace("-help.pd", "")
        json_name = f"{name}.json"
        result = build_description_and_categories(
            title=name,
            help_patch_path=file,
            base_json=base,
            model="gemini-2.5-flash",
            top_n=3,
            threshold=0.9,
        )
        with open(json_name, "w") as f:
            json.dump(result, f, indent=4)
