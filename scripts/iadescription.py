#!/usr/bin/env python3
import os
import json
import subprocess
from typing import Dict, Any, List, Tuple

CATEGORIES_DESCRIPTIONS: Dict[str, str] = {
    "Machine Learning": "AI → General machine learning algorithms or tools for data analysis and prediction.",
    "Deep Learning": "AI → Neural networks and deep learning models for complex pattern recognition.",
    "Neural Networks": "AI → Artificial neural network structures used in AI tasks.",
    "Statistical Models": "AI → Statistical modeling techniques for analyzing and predicting data.",
    "Algorithmic Composition": "Composition → Tools for composing or chaining algorithms in a musical context.",
    "Procedural": "Composition → Procedural logic or structured musical processes.",
    "Logic": "Control → Boolean logic or logical operations for controlling signal or data flow.",
    "Math": "Control → Mathematical functions and calculations used in signal processing and control.",
    "Routing": "Control → Signal or data routing objects to direct flow between modules.",
    "Envelopes": "Control → Envelope generators or shapers for controlling amplitude or other parameters.",
    "LFOs": "Control → Low frequency oscillators for modulation purposes.",
    "Sequencers": "Control → Step or pattern sequencers for timing and order of events.",
    "MIDI": "Control → Objects for MIDI input, output, and parsing musical control messages.",
    "Reverb": "Effects → Audio effect for simulating reverberation in signals.",
    "Delay": "Effects → Audio effect for delaying signals with optional feedback.",
    "Distortion": "Effects → Audio effect that alters and distorts the sound signal.",
    "Chorus/Flanger/Phaser": "Effects → Modulation effects: chorus, flanger, or phaser for thickening or movement.",
    "Filters": "Effects → Audio filters to modify frequency content of signals.",
    "Dynamics": "Effects → Compression, expansion, or other dynamic range processing.",
    "Partial Tracking": "MIR/Analysis → Analysis, tracking, or synthesis of partials in audio signals.",
    "Descriptors": "MIR/Analysis → Audio descriptors or feature extraction (e.g., FFT, pitch, chroma).",
    "Score Follower": "MIR/Analysis → Follows a musical score in real-time for synchronization.",
    "VST2/VST3": "Plugins → Support for VST2/VST3 plugin integration.",
    "Vamp": "Plugins → Support for Vamp plugin integration.",
    "LADSPA": "Plugins → Support for LADSPA plugin integration.",
    "AU": "Plugins → Support for Audio Unit plugin integration.",
    "Ambisonics": "Spatialization → Ambisonic audio tools for spatial sound rendering.",
    "Binaural": "Spatialization → Binaural audio tools for 3D sound perception.",
    "VBAP": "Spatialization → Vector-based amplitude panning tools.",
    "Subtractive": "Synthesis → Subtractive synthesis techniques.",
    "Additive": "Synthesis → Additive synthesis techniques.",
    "Granular": "Synthesis → Granular synthesis techniques.",
    "Oscillators": "Synthesis → Signal generators or oscillators for sound creation.",
    "Physical Modeling": "Synthesis → Physical modeling synthesis simulating real-world instruments.",
    "Samplers": "Synthesis → Sample playback and manipulation.",
    "Stochastic": "Synthesis → Stochastic or random process-based synthesis.",
    "Data Structures": "Utilities → Data storage and manipulation objects.",
    "File IO": "I/O → File input/output operations for audio, text, or patches.",
    "Networking": "I/O → Network communication objects (TCP, UDP, WebSocket).",
    "MultiThreading": "Utilities → Multi-threaded processing support.",
    "Patching": "Utilities → Patch management or dynamic patching tools.",
    "Multichannel": "Utilities → Multichannel audio support objects.",
    "GUI": "Interfaces → GUI objects that render widgets in the patch (e.g., sliders, knobs).",
    "Graphics": "Interfaces → Objects for visual rendering (e.g., GEM, video, OpenGL).",
    "Audio IO": "I/O → Audio input/output interfaces for sound devices (e.g., adc~, dac~).",
    "Control IO": "I/O → Objects for input from keyboard, mouse, joystick, or other HID devices.",
    "General Utilities": "Utilities → General utilities for system commands and helper functions.",
    "Text": "Utilities → Objects to parse or manipulate text data.",
    "OSC": "I/O → Objects that work with Open Sound Control (OSC).",
    "Extensions": "Extensions → Enable writing externals in languages other than C (e.g., Lua, Python).",
}


# Stable ordered list of category keys
CATEGORIES: List[str] = list(CATEGORIES_DESCRIPTIONS.keys())

PROMPT_TEMPLATE = """You are both a technical writer and a classifier.
Task:
1) Write a concise, clear English description (2–3 sentences max) of the Pure Data object described by the help patch. Focus on what the object does, its purpose, and any evident usage hints. Keep it simple, practical, and readable. Wrap Pure Data object names in inline code using backticks (e.g., `osc~`, `route`, `nn~`).
2) Score ALL categories (listed below) with a confidence between 0.0 and 1.0 for how well the object's functionality fits each category. Consider the category description carefully, which now includes its parent category. 

Important: Use the exact category name as the key for scoring, but rely on the description (which includes parent context) to understand each category's scope.

Output rules:
- Return ONLY a valid JSON object (no extra text).
- The JSON must have exactly these top-level keys:
  - "description": string (markdown allowed)
  - "scores": object mapping each category name to a float (0.0–1.0)
- The "scores" object MUST include EVERY category key exactly as provided (same spelling).
- Values in "scores" MUST be numbers (floats). If a category does not apply, use 0.0.
- Do not add or remove keys. Do not include comments.
- No trailing commas.

Categories (JSON object where key = category name, value = description):
{CATEGORIES_DESCRIPTIONS_JSON}

Object title:
{TITLE}

Help Patch (.pd text): The content below is delimited by triple pipes. Treat everything between the delimiter lines as the literal .pd help patch text. Do not modify it.
```pd
{PATCH_TEXT}
```
"""


def _build_prompt(title: str, patch_text: str) -> str:
    all_lines = []
    for line in patch_text.splitlines():
        if line.split(" ")[0] == "#X" and line.split(" ")[1] == "text":
            all_lines.append(line)

    filtered_patch = " ".join(all_lines)
    return PROMPT_TEMPLATE.format(
        CATEGORIES_DESCRIPTIONS_JSON=json.dumps(
            CATEGORIES_DESCRIPTIONS, ensure_ascii=False, indent=2
        ),
        TITLE=title.strip(),
        PATCH_TEXT=filtered_patch,
    )


def _run_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Runs Gemini CLI in non-interactive mode and returns stdout only.
    Assumes Gemini CLI is installed and already authenticated.
    """
    env = os.environ.copy()
    env["NODE_NO_WARNINGS"] = "1"  # silence Node warnings
    env["NO_COLOR"] = "1"  # plain output

    cmd = ["gemini", "-m", model, "--approval-mode", "yolo", "-p", prompt]
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
    aider: bool = False,
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
    with open(help_patch_path, "r", encoding="utf-8", errors="replace") as f:
        patch_text = f.read()

    prompt = _build_prompt(title, patch_text)
    if aider:
        stdout = _run_gemini(prompt, model=model)
    else:
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


def build_dict():
    base = {}
    runs_on = input("Enter platforms separated by commas (Mac,Linux,Windows): ")
    base["runs_on"] = [x.strip() for x in runs_on.split(",")]
    available = input("Available on deken? (y/n): ").lower() == "y"
    base["available_on_deken"] = available
    if available:
        base["download_link"] = ""
    else:
        base["download_link"] = input("Enter download link: ")

    base["bug_reports"] = input("Bug reports URL: ")
    devs = input("Enter developer names (comma separated): ")
    base["developers"] = [x.strip() for x in devs.split(",")]
    part_of_lib = input("Part of a library? (y/n): ").lower() == "y"
    base["part_of_library"] = part_of_lib
    if part_of_lib:
        base["library_name"] = input("Library name: ")
    else:
        base["library_name"] = ""

    base["articles"] = []
    base["videos"] = []
    base["musics"] = []

    contributors = input("Contributors (comma separated) for the page: ")
    base["contributors"] = [x.strip() for x in contributors.split(",")]
    base["ai"] = True
    return base


# Example usage
errors_processing = []

if __name__ == "__main__":
    LIBRARY_HELP_FILES = input("Enter library dir where -help.pd are: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    base = build_dict()
    count = 0
    for help_fname in os.listdir(LIBRARY_HELP_FILES):
        if help_fname.endswith("-help.pd"):
            count += 1

    processed_count = 0
    os.makedirs("../docs/objects_raw", exist_ok=True)
    for help_fname in os.listdir(LIBRARY_HELP_FILES):
        if help_fname.endswith("-help.pd"):
            processed_count += 1
            file_path = os.path.join(LIBRARY_HELP_FILES, help_fname)
            name = help_fname.replace("-help.pd", "")
            json_name = f"../docs/objects_raw/{name}.json"
            if os.path.exists(json_name):
                continue

            try:
                print(
                    f"Processing {processed_count:04} of {count:04} | {help_fname}..."
                )
                result = build_description_and_categories(
                    title=name,
                    help_patch_path=file_path,
                    base_json=base,
                    model="gemini-2.5-flash",
                    top_n=3,
                    threshold=0.9,  # consider lowering if you often get 0 categories
                    aider=False,
                )
                with open(json_name, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"[ERROR] {help_fname}: {e}")
                errors_processing.append([help_fname, e])

with open("../errors.json", "w") as f:
    json.dump(errors_processing, f, indent=4)
