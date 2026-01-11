# Build GPT From Scratch (Educational)

This repository demonstrates how a **GPT-style Transformer decoder** can be built **from scratch**, without using high-level abstractions such as `nn.Transformer` or HuggingFace trainers.

The goal is to deeply understand:
- Causal self-attention
- Transformer decoder architecture
- Autoregressive language modeling
- Training and inference dynamics of GPT-like models

This project is part of **Day 53 of my 90 Days of AI** journey.

---

## What is implemented from scratch?

- Character-level tokenizer
- Token & positional embeddings
- Multi-head self-attention with **causal masking**
- Feed-forward networks
- Residual connections + LayerNorm
- End-to-end training loop (teacher forcing)
- Autoregressive text generation

No pretrained weights. No black-box trainers.

---

## Repository Structure

- mini_gpt.py # Minimal GPT implementation + training + generation
- gemini_client.py # Hosted Gemini inference examples (for comparison)
- compare_generate.py # Compare local GPT vs Gemini outputs
- README.md


---

## Model Architecture

The model follows the standard **GPT decoder-only Transformer** architecture:

1. Token Embedding + Positional Embedding
2. Repeated Transformer Blocks:
   - LayerNorm
   - Multi-Head Self-Attention (causal mask)
   - Feed Forward Network
   - Residual connections
3. Linear projection to vocabulary logits

Causal masking ensures each token can attend **only to past tokens**, enforcing autoregressive behavior.

---

## Training Objective

- Language modeling via **next-token prediction**
- Loss: Cross-entropy
- Optimizer: Adam / AdamW
- Training style: Teacher forcing

The dataset is intentionally small to keep training fast and interpretable.

---

## Why Character-Level Tokenization?

Character-level modeling was chosen to:
- Avoid dependency on external tokenizers
- Clearly demonstrate sequence modeling mechanics
- Keep the implementation minimal and transparent

Limitations of this choice are discussed below.

---

## Text Generation

The model generates text autoregressively by:
1. Feeding initial context
2. Sampling next token from model logits
3. Appending token and repeating

Supports temperature-based sampling.

---

## Gemini Comparison (Optional)

For intuition-building, this repo also includes examples of calling a **hosted Gemini model**.

This comparison highlights:
- Scale differences
- Data effects
- Why architecture alone is not enough

Gemini is **not part of the training pipeline**.

---

## Limitations

- Character-level tokenization (inefficient for large corpora)
- Small dataset
- No distributed training
- No mixed precision
- No evaluation metrics like perplexity tracking

---

## Future Improvements

- Implement BPE tokenizer
- Token-level GPT
- Learning rate scheduling + warmup
- Perplexity evaluation
- Modularize model into components
- Add checkpointing & logging
- Scale to WikiText-2

---

## How to Run

```bash
pip install torch google-generative-ai
python mini_gpt.py
```

## Key Learnings
This project helped me deeply understand:
- How causal attention works internally
- Why GPT scales well with data
- Training instability and optimization challenges
- Differences between local models and hosted LLMs
