# Multi-Agent Flight Operations Assistant ✈️

A planner-led multi-agent AI system that simulates airline operational decision-making (delay / divert / cancel) using RAG + Small Language Models (SLMs).

This project demonstrates how agentic AI systems can be designed for regulated, safety-critical industries like aviation, inspired by real airline operations (e.g., IndiGo).

## Problem Statement

Flight operations decisions depend on multiple constraints:
- Weather conditions
- Crew legality and regulations
- Aircraft availability
- Cost and business impact

A single LLM is unsafe and unreliable for such problems.

This system demonstrates **agentic system design**, where:
- Problems are decomposed into sub-tasks
- Each agent has a clear responsibility
- RAG is used only where factual grounding is required

## 🧩 Agent Responsibilities

### 1️⃣ Planner Agent
- Converts an unstructured user query into structured sub-tasks
- Acts as the **entry point** for the agentic system

> "Should flight 6E-203 be cancelled due to fog?" → weather check → crew legality check → aircraft availability → cost impact

### 2️⃣ Weather Agent (RAG + SLM)
- Uses **RAG** to retrieve aviation weather operation rules (e.g., fog limits, CAT II/III rules)
- Applies reasoning using a **Small Language Model**

> ❗ Live weather data tells *what the weather is*  
> RAG tells *what operations are allowed given the weather*

### 3️⃣ Crew Rules Agent (Pure RAG)
- Retrieves airline/DGCA-style crew duty and legality rules
- Ensures regulatory compliance
- Crew rules are **static, auditable, and policy-driven** — ideal for RAG

### 4️⃣ Aircraft Availability Agent (Deterministic)
- Handles aircraft state and availability
- No LLM used intentionally
- Demonstrates that **not every component needs AI**

### 5️⃣ Cost Agent (Heuristic)
- Estimates business impact
- Uses rule-based or heuristic logic
- Keeps cost reasoning transparent and controllable

### 6️⃣ Synthesizer Agent
- Aggregates outputs from all agents
- Produces a single recommendation:
  - Delay
  - Cancel
  - Divert
- Provides explainable reasoning

## 📚 RAG Pipeline Design

RAG is implemented **only where knowledge grounding is required**.

```bash
User Query
↓
Embedding Model
↓
Vector Search (FAISS)
↓
Relevant Policy Context
↓
Injected into SLM Prompt
↓
Grounded Response
```

## 🛠️ Tech Stack

| Component | Technology |
|--------|-----------|
LLM | Microsoft Phi-3 Mini |
Embeddings | BGE-small |
Vector Store | FAISS |
API | FastAPI |
Deployment | Docker + Render |

## 🚀 How the Pipeline Works (End-to-End)

1. User sends a natural language query
2. Planner Agent decomposes the task
3. Specialized agents run **in parallel**
4. RAG agents retrieve grounded policy context
5. Synthesizer Agent aggregates results
6. Final decision is returned via API

## ▶️ Running Locally

```bash
pip install -r requirements.txt
python vectorstore/build_index.py
uvicorn app:app --reload
```

```test
http://localhost:8000/decision?query=Should flight 6E-203 be cancelled due to fog at DEL?
```

## 🐳 Docker Deployment

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```


# Built as a part of #90DaysofAI series 






