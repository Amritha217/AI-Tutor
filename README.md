# AI-Tutor

AI-Tutor is a local web-based Q&A application that leverages **local Large Language Models (LLMs)** and a **FAISS vector store** to answer user questions from educational material.

---

## Features

- Web interface built with **FastAPI** and **Jinja2**.
- Question answering powered by **Hugging Face Flan-T5** LLM.
- Document retrieval using **FAISS** vector store with **Sentence-Transformers** embeddings.
- Easily extendable architecture for adding more documents or models.
- Local deployment — no external API calls needed.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Amritha217/AI-Tutor.git
cd AI-Tutor
