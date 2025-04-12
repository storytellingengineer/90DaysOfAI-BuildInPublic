# 📍 Day 03 – Visualizing NLP with Streamlit

On Day 3 of my 90 Days of AI journey, I took my NLP experiments from static code to **interactive web apps** using **Streamlit**! 🚀

Today’s app allows you to:
- Input custom text
- View tokens and POS tags
- See Named Entity Recognition (NER) output
- Visualize entities beautifully using `displacy`

---

## 🧠 Why Streamlit?

Streamlit is amazing for:
- Rapidly prototyping ML/NLP apps
- Creating demo interfaces without worrying about frontend code
- Showcasing projects to recruiters, teammates, or collaborators

---

## 💡 How to Use This App

1. Paste any text into the input box  
2. Click **Analyze**  
3. Explore tokens, tags, entities — and enjoy the clean UI!

---

## 🛠 Installation & Setup

```bash
pip install streamlit spacy
python -m spacy download en_core_web_sm
streamlit run app.py
