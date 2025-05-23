# Day 15 of #90DaysOfAI — Tokenization & Semantic Embedding Visualization using BERT

In this project, I explored how a pretrained transformer model like BERT tokenizes text and encodes the meaning of words into high-dimensional vectors. I visualized the hidden semantic relationships between tokens using PCA and observed how context shapes the meaning of identical words (like "bank").

---

## 🔍 What This Project Covers

- WordPiece tokenization using BERT's tokenizer
- Extraction of 768-dimensional token embeddings from BERT
- PCA-based dimensionality reduction to 2D for visualization
- Visual inspection of semantic similarity and contextual meaning

---

## 💡 Key Learnings

1. **Tokenization is not just splitting words:**  
   Even a simple sentence like _"The bank was flooded after the storm."_ breaks down into meaningful subword units. BERT understands "bank" refers to a river here, based purely on context.

2. **Embeddings reflect context-aware meaning:**  
   The same word in a different sentence will have a different vector. That’s the real power behind transformers—words learn meaning from their neighbors.

3. **PCA reveals hidden structures:**  
   Projecting embeddings onto a 2D plane shows visually how similar tokens cluster, revealing relationships we don't explicitly code.

---

## 🧠 Challenges Faced

- **Memory issues while visualizing attention maps:**  
  Initially, I tried visualizing self-attention matrices which consumed a lot of memory. I later optimized the project to focus on embeddings, which is both efficient and meaningful.

- **Understanding embedding differences visually:**  
  It’s easy to extract vectors, but interpreting them in low dimensions requires thoughtful design (PCA works well for smaller text inputs).

---

## 🛠️ Tools & Libraries Used

- HuggingFace Transformers (BERT Tokenizer & Model)
- PyTorch for model inference
- Matplotlib & Seaborn for visualizations
- Scikit-learn PCA for dimensionality reduction

---

## 🚀 Applications You Can Build from This

> This simple idea of token-to-vector conversion lays the groundwork for:

- Semantic search engines
- Zero-shot classifiers
- Context-aware chatbots
- Recommender systems based on textual behavior
- Fraud detection with NLP log analysis
- Fine-tuning foundation models for domain-specific tasks


> Follow me on [LinkedIn](https://www.linkedin.com/in/storytellingengineer/) to join the rest of my **#90DaysOfAI** journey, where I dive deeper into the real-world applications of AI.



