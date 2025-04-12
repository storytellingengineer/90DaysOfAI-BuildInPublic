# 📊 Day 3 – Visualizing NLP with Streamlit

On Day 3 of my 90 Days of AI challenge, I built a simple yet interactive NLP visualization app using **Streamlit**.

After preprocessing text (Day 1) and exploring Named Entity Recognition with spaCy (Day 2), I wanted a way to **visually explore the results** — and Streamlit made it super easy to spin up a lightweight web app!

---

## 💻 What It Does

The app allows you to enter any text and instantly returns:

- Tokenization
- Part-of-Speech (POS) Tags
- Named Entities
- Lemmatized Tokens
- Visualized NER using `displacy`

You can run it locally and play with your own input — it's a fun way to *see* what's happening under the hood in NLP!

---

## ⚠️ Challenges I Faced

Let me tell you — it wasn’t a straight path 😅

I faced a bunch of compatibility issues, mainly:

- `numpy` version errors conflicting with `thinc`, `scipy`, and `gensim`
- spaCy model download errors
- An environment setup that kept breaking things in strange ways

**What worked for me:**

- Creating a fresh conda environment
- Downgrading `numpy` to `1.23.5`
- Installing packages manually in order

```bash
conda create -n ai_env python=3.10
conda activate ai_env

pip install numpy==1.23.5
pip install spacy==3.5.4
pip install streamlit nltk gensim

python -m spacy download en_core_web_sm
```

## Running the app

- `streamlit run app.py`
