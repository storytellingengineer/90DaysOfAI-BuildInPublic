# Day 53 — Build GPT From Scratch

Repository for **Day 53** of my "90 Days of AI" series: building a small GPT-like model from scratch and demonstrating how to call a hosted Gemini model for comparison.

This repo is educational: it shows the core Transformer decoder components and an end-to-end minimal training loop (toy dataset, char-level). It also includes example code to call Gemini / Google Generative AI for inference.

---

## Contents

- `mini_gpt.py` — Minimal, single-file GPT-like model (char-level). Train locally and run generation.
- `gemini_client.py` — Example Gemini API clients:
  - Option A: `google.generativeai`-style client (easy).
  - Option B: Vertex AI `PredictionServiceClient` example (for Google Cloud users).
- `compare_generate.py` — Generate text from both the local model and Gemini to compare results.
- `README.md` — this file.

---

## Quick start

### 1) Clone repo
```bash
git clone https://github.com/<your-username>/day53-build-gpt-from-scratch.git
cd day53-build-gpt-from-scratch
```

### 2) (Optional) Create a virtualenv
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### 3) Install required packages
```
pip install torch
pip install google-generative-ai
```

