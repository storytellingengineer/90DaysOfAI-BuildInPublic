# Day 01: Basic NLP Preprocessing in Python

### 🔍 What I did:
- Explored core text preprocessing steps using `nltk` and `spacy`
- Handled tokenization, stopword removal, stemming, lemmatization, and POS tagging

### 💡 Key Learnings:
- Realized how essential clean data is for any NLP pipeline
- Faced environment-specific issues with `nltk` on my remote setup
- Fixed it by manually setting `NLTK_DATA` path and downloading required corpora

### ⚙️ How to run:
```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
