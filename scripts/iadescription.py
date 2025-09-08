#!/usr/bin/env python3
import os
import json
import subprocess
from typing import Dict, Any, List, Tuple

LIBRARY_HELP_FILES = "/home/neimog/Documents/Pd/externals/else/"

CATEGORIES_DESCRIPTIONS = {
    "Machine Learning": "General machine learning algorithms or tools.",
    "Deep Learning": "Neural networks and deep learning models.",
    "Neural Networks": "Artificial neural network structures.",
    "Statical Models": "Statistical modeling tools.",
    "Algorithm Composition": "Tools for composing or chaining algorithms.",
    "Procedures": "Procedural logic or control.",
    "Logic": "Boolean logic or logical operations.",
    "Math": "Mathematical functions and calculations.",
    "Routing": "Signal or data routing objects.",
    "Envelopes": "Envelope generators or shapers.",
    "LFOs": "Low frequency oscillators.",
    "Sequencers": "Step or pattern sequencers.",
    "MIDI": "For MIDI input, output, and MIDI parsing (not objects that just accept or output MIDI).",
    "Reverb": "Audio effect for simulating reverberation.",
    "Delay": "Audio effect for delaying signals.",
    "Distortion": "Audio effect for distorting signals.",
    "Chorus/Flanger/Phaser": "Modulation effects: chorus, flanger, phaser.",
    "Filters": "Audio filters for modifying frequency response.",
    "Dynamics": "Compression, expansion, or other dynamic range processing.",
    "Partial Tracking": "Analysis, tracking or Synthesis of partials in audio.",
    "Descriptors": "Audio descriptors or feature extraction. FFT, Pitch, chroma, cepstrum, etc...",
    "Score Follower": "Follows musical score in real-time.",
    "VST2/VST3": "VST plugin support.",
    "Vamp": "Vamp plugin support.",
    "LADSPA": "LADSPA plugin support.",
    "AU": "Audio Unit plugin support.",
    "Ambisonics": "Ambisonic audio tools.",
    "Binaural": "Binaural audio tools.",
    "VBAP": "VBAP audio toools.",
    "Subtractive": "Subtractive synthesis.",
    "Additive": "Additive synthesis.",
    "Granular": "Granular synthesis.",
    "Oscillators": "Signal generators/oscillators.",
    "Physical Modeling": "Physical modeling synthesis.",
    "Samplers": "Sample playback/manipulation.",
    "Stochastic": "Stochastic/random processes.",
    "Data Structures": "Data storage and manipulation.",
    "File IO": "File input/output.",
    "Networking": "Network communication, http, https, websocket, etc.",
    "MultiThreading": "Multi-threaded processing.",
    "Patching": "Patch management, dynamic patching.",
    "Multichannel": "Multichannel audio support.",
    #
    "GUI": "Gui objects, they show something in the patch (keyboards, sliders, knob).",
    "Graphics": "Objects for visual rendering and graphics (e.g., GEM, video, OpenGL).",
    "Audio IO": "Audio input/output objects for interfacing with sound devices (e.g., adc~, dac~).",
    "Control IO": "Objects for receiving input from keyboard, mouse, joystick, and other HID devices.",
    "General Utilities": "Utilities general, system command, and others",
    "Text": "Objects to process text",
    "OSC": "Object that work with Open Sound Control (OSC)",
    "Extensions": "Objects that can be used to write object in another languages other than C (pdlua, py4pd)",
}

_seen = set()
CATEGORIES: List[str] = []
for c in CATEGORIES_RAW:
    if c not in _seen:
        _seen.add(c)
        CATEGORIES.append(c)

PROMPT_TEMPLATE = """You are both a technical writer and a classifier.
Task:
1) Produce a concise, clear English description (2–3 sentences max) of the Pure Data object described by the following help patch. Focus on what the object does, its purpose, and key usage hints if they are evident. Keep it simple and practical. Also put all pd objects as code block using the name between ``.
2) Score ALL categories (listed below) with a confidence between 0.0 and 1.0 for how well the object's functionality fits each category, using the provided category descriptions for guidance.

Important: Use the exact category name as the key for scoring, but use the description to understand what each category means.

Output rules:
- Return ONLY a valid JSON object (no markdown and no extra text).
- The JSON must have exactly these top-level keys:
  - "description": string (can use markdown)
  - "scores": object mapping each category name to a float (0.0–1.0)
- The "scores" object MUST include EVERY category key exactly as provided (same spelling).
- Values in "scores" MUST be numbers (floats). If a category does not apply, use 0.0.
- Do not add or remove keys. Do not include comments.
- No trailing commas.

Categories (as a JSON object: key = category name, value = description):
{CATEGORIES_DESCRIPTIONS_JSON}

Object title:
{TITLE}

Help Patch (.pd text):
```pd
{PATCH_TEXT}```
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
    out["categories"] = selected
    return out


# Example usage (commented):
base = {
    "runs_on": ["Mac", "Linux", "Windows"],
    "download_link": "",
    "available_on_deken": True,
    "bug_reports": "https://github.com/porres/pd-else/issues",
    "developers": ["William Brent"],
    "part_of_library": True,
    "library_name": "else",
    "articles": [],
    "videos": [],
    "musics": [],
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
