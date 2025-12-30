# AI-Tutor

**AI-Tutor** is a **local web-based Q&A application** that leverages **local Large Language Models (LLMs)** and a **FAISS vector store** to answer questions from textbooks. It combines a FastAPI backend with a modern React + Vite frontend.

---

## 🚀 Features

- **Web Interface:** Interactive frontend built with React and Vite.
- **Local LLM:** Uses Hugging Face Flan-T5 for generating accurate answers.
- **Semantic Retrieval:** FAISS vector store with Sentence-Transformers embeddings.
- **Modular Architecture:** Easily add new textbooks or models.
- **Fully Local:** No external API calls required.
- **Fast Response:** Sub-second retrieval for relevant passages.

---

## 🛠 Tech Stack

- **Backend:** Python, FastAPI, LangChain, Hugging Face Transformers, FAISS  
- **Frontend:** React, Vite, HTML/JSX  
- **Tools:** Git, VS Code, Jupyter Notebook  

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/Amritha217/AI-Tutor.git
cd AI-Tutor
```


2. Create and activate a Python virtual environment:
   
   ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate

    ```

3. Install backend dependencies:

  ```bash
   pip install -r requirements.txt
  ```

4. Install backend dependencies:

```bash
   uvicorn app.main:app --reload
```

## ⚡ Frontend Setup

1. Navigate to frontend directory:
```bash
   cd ai-tutor-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React frontend:
```bash
npm run dev
```


## 📚 Project Details

- Textbook Used: Physics textbook PDF (too large to upload).

- Workaround: Screenshots included to demonstrate working queries and answers.

- Backend: FastAPI + LangChain + Flan-T5 + FAISS

- Frontend: React + Vite with dynamic question input and answer display

## Example Screenshots

- Ask a question

- Get AI-generated answer

## 🔧 Features Added Recently

- React + Vite frontend consuming FastAPI REST API

- Responsive UI with loading states

- Modular design for easy textbook/model updates

## 📌 Notes

- AI-Tutor is fully local; no API keys or external servers needed.

- FAISS enables sub-second semantic search.

- Flan-T5 generates accurate answers with LLM retrieval pipeline.

## 👩‍💻 Usage

-Start backend server (uvicorn app.main:app --reload).

- Start frontend server (npm run dev).

- Open frontend in browser.

E- nter a question from the textbook and submit.

- Get AI-generated answers instantly.
