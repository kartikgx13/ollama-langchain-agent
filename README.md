# Ollama LangChain agent

Small CLI that answers questions about a pizza restaurant using **LangChain**, **Ollama**, and **Chroma**. Reviews are loaded from `realistic_restaurant_reviews.csv`, embedded with Ollama, and stored locally; the chat model answers using the top matching review snippets.

## Prerequisites

- Python 3.12+ (3.14 works)
- [Ollama](https://ollama.com/) running locally with these models pulled:

  ```bash
  ollama pull llama3.2
  ollama pull mxbai-embed-large
  ```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run from the project root so the CSV and Chroma paths resolve correctly.

## Run

```bash
python main.py
```

Type a question at the prompt; enter `q` to quit.

On first run, embeddings are written to `chrome_langchain_db/` (ignored by git). Delete that folder to rebuild the index from the CSV.

## Files

| File | Role |
|------|------|
| `main.py` | Interactive Q&A using `llama3.2` |
| `vector.py` | Builds Chroma store + retriever (`mxbai-embed-large`) |
| `realistic_restaurant_reviews.csv` | Source reviews |
