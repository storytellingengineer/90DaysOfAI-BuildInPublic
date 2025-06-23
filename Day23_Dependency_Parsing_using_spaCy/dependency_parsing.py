import spacy
from spacy import displacy
import streamlit as st

# Load English tokenizer and dependency parser
nlp = spacy.load("en_core_web_sm")

# Streamlit UI
st.title("🧠 Dependency Parser")
sentence = st.text_input("Enter an English sentence:", "The quick brown fox jumps over the lazy dog.")

if sentence:
    doc = nlp(sentence)
    
    st.subheader("📌 Token Dependencies")
    for token in doc:
        st.write(f"{token.text:10} → {token.dep_:15} ({token.head.text})")
    
    st.subheader("🔗 Dependency Tree Visualization")
    html = displacy.render(doc, style="dep", jupyter=False)
    st.components.v1.html(html, height=300, scrolling=True)
