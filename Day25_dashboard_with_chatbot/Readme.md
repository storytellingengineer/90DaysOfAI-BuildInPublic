# 🧠 AI-Powered Student Dashboard (Agentic) 📚

A smart, agentic student dashboard built with **Streamlit**, **Google Classroom API**, and **LLM** integration (OpenAI via your wrapper).  
It supports planner → RAG → LLM orchestration so the dashboard can *act* (produce plans, retrieve relevant context, and execute stepwise answers) instead of only answering single-shot queries.

---

## Features

- **Assignment Tracker** — (via Google Classroom API) shows pending/submitted/upcoming assignments.
- **Agentic Assistant** — Planner creates small stepwise plan; RAG fetches context; LLM executes each subtask and aggregates the final answer.
- **LLM Chatbot** — Ask study-related queries: "What's due today?", "Explain Decision Trees", "Find resources for gradient boosting".
- **Vector Search (RAG)** — ChromaDB / FAISS / Milvus can be used for document retrieval to provide context.
- **Extensible Agent Modules** — `planner_agent.py`, `rag_agent.py`, `chatbot.py` can be replaced with your custom implementations.

---

## Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [OpenAI GPT (via LangChain)](https://openai.com/) – for natural language Q&A
- [Google Classroom API](https://developers.google.com/classroom) – for real-time academic info
- [Chromadb](https://www.trychroma.com/) – for vector-based semantic search
- Python 3.10+

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/storytellingengineer/Day25_dashboard_with_chatbot.git
cd Day25_dashboard_with_chatbot
```

### 2. Set Up Environment

```
python -m venv venv
venv\Scripts\activate         # Windows
# or
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

### 3. Set Up .env File

Create a .env file in the root folder:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
GOOGLE_CLIENT_SECRET_FILE=credentials.json
```

### 4. Add Your Google Credentials
- Go to Google Cloud Console
- Enable **Google Classroom API**
- Create **OAuth 2.0 Client ID**
- Download the `credentials.json` and place it in the project root

---

## Run the App

```streamlit run app.py```

## Project Structure

```
├── app.py # Streamlit app             (this file)
├── agent_orchestrator.py              # Orchestrator that wires planner -> RAG -> LLM
├── chatbot.py # Your LLM wrapper      (LangChain / OpenAI calls)
├── planner_agent.py                   # Optional: produce plans (task decomposition)
├── rag_agent.py                       # Optional: retrieval from vector DB (Chroma/FAISS)
├── classroom_api.py                   # Google Classroom integration
├── prompts.py                         # Prompt templates
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## Example Queries for Chatbot
- "What assignments are pending for me this week?"
- "Explain PCA with an example."
- "What is the latest Leetcode problem I should try?"
- "What are the current ML/NLP topics being studied?"

## 👨‍🔬 Author
Made with ❤️ by [Aayush Saxena](https://www.linkedin.com/in/storytellingengineer/)
