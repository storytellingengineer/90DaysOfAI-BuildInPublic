# Visual Question Answering (VQA) - Day 9 Project 🚀

## 🧠 Project Overview

This project demonstrates the power of combining **Computer Vision** (CV) and **Natural Language Processing** (NLP) to create a system that can look at an image and answer a user's question about it.  
This is called **Visual Question Answering (VQA)** — a foundational concept for building smarter AI systems.

We used the **Salesforce BLIP-VQA model**, a powerful pre-trained model capable of understanding both image features and language queries.

---

## 🌟 Why This Project is Important

- **Bridges Vision and Language:**  
  VQA is not just about detecting objects, but truly *understanding* scenes and answering based on context.

- **Foundation for Advanced AI Applications:**  
  - AI Assistants that "see and answer" (for visually impaired).
  - Smart surveillance systems.
  - Search engines that take "image + text" queries.
  - Customer service bots that can analyze uploaded images.

- **Future Development:**  
  This technology is crucial for areas like:
  - **Autonomous vehicles** (interpreting the environment).
  - **Medical Imaging AI** (analyzing X-rays, MRIs).
  - **Augmented Reality (AR)** applications.
  - **Interactive shopping** (asking questions about product images).

---

## 🛠️ Tools and Libraries Used

- Python
- Huggingface `transformers`
- PyTorch
- BLIP (Bootstrapped Language Image Pretraining) Model
- PIL (Python Imaging Library)
- Requests, BeautifulSoup (for handling URLs and images)

---

## ⚡ How It Works

1. User provides an image URL.
2. User asks a natural language question about the image.
3. The model processes the image and question together.
4. AI outputs the most relevant answer based on both visual and textual understanding.

---

## ❌ Hurdles Faced

1. **Handling non-direct image URLs:**  
   Initially, when I gave a normal Unsplash link (e.g., webpage link), the code failed because it needed a **direct image** URL (.jpg, .png).

2. **PIL UnidentifiedImageError:**  
   PIL threw an error because it received an HTML webpage, not a real image.

3. **Attention Mask Warning:**  
   Huggingface gave a warning about not using an attention mask, though it didn't critically affect the output.

---

## 🔥 How I Solved Them

- Instead of expecting only direct links, I modified the code:
  - Scrape the page using **BeautifulSoup**.
  - Extract the real image URL dynamically.

- Alternatively, I used **direct links from Google Images**, which already end with `.jpg` or `.png`, making it super smooth.

- I ignored the warning related to the attention mask for now, since the results were accurate. However, for production-grade apps, explicitly setting attention masks would be important.

---

## 🖼️ Sample Output

```bash
Enter Image URL: https://upload.wikimedia.org/wikipedia/commons/4/47/Football_iu_1996.jpg
Enter Question: What is the man doing?

Thinking...

Your Question: What is the man doing?
Predicted Answer: playing soccer
