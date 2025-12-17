# AI-Tutor

AI-Tutor is a **local web-based Q&A application** that leverages **local Large Language Models (LLMs)** and a **FAISS vector store** to answer user questions from educational material.

---

## 🚀 Features

- Web interface built with **FastAPI** and **Jinja2**.
- Question answering powered by **Hugging Face Flan-T5** LLM.
- Document retrieval using **FAISS** vector store with **Sentence-Transformers** embeddings.
- Easily extendable architecture for adding more documents or models.
- Fully local deployment — **no external API calls** needed.

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Amritha217/AI-Tutor.git
   cd AI-Tutor



2. Create a virtual environment and activate it:

   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate



3. Install dependencies:

   pip install -r requirements.txt


4. ⚡ Running the Application

   uvicorn app.main:app --reload

   - Open your browser at http://127.0.0.1:8000
   - Ask questions and see AI-Tutor in action.

---

##  📚 About the Project

I have created this project using a Physics textbook pdf from a sourced site that provides Free, high-quality textbooks.
Since the textbook is too large to include in the repository, I have provided screenshots showing the working of the AI-Tutor with example queries.

Example screenshots:

1. Ask a question about Physics concepts
2. Get an AI-generated answer
3. Full Q&A Example

---

## 🛠 Tech Stack

Backend: FastAPI, Python
Frontend: Jinja2 Templates, HTML
LLM: Hugging Face Flan-T5
Vector Search: FAISS, Sentence-Transformers
Tools: Git, VS Code
