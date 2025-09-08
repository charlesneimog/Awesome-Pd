## Objects from Help Patches


```
You are both a technical writer and a classifier.

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
`
{PATCH_TEXT}
`
```

