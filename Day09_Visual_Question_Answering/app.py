import torch
import streamlit as st
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="VQA App", page_icon="📷")

@st.cache_resource
def load_model():
    model_name = "Salesforce/blip-vqa-base"
    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForQuestionAnswering.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return processor, model, device

processor, model, device = load_model()

st.title("📷 Visual Question Answering")
st.write("Ask questions about any image")

image_url = st.text_input("Enter Image URL")
question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if image_url and question:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        st.image(image, caption="Input Image", use_column_width=True)

        prompt = f"Question: {question}. Answer in 100 words."
        inputs = processor(image, prompt, return_tensors="pt").to(device)
        outputs = model.generate(**inputs,
                            max_length=100,
                            num_beams=5,
                            early_stopping=True)
        answer = processor.tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.success(f"Answer: {answer}")
    else:
        st.warning("Please provide both image URL and question")