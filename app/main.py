# app/main.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import os

app = FastAPI()

# ---------------------------
# Load VectorStore + Embeddings
# ---------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
index_path = os.path.join(os.path.dirname(__file__), "faiss_index")
vector_store = FAISS.load_local(index_path, embeddings)
retriever = vector_store.as_retriever()

# ---------------------------
# Load Local Hugging Face Model
# ---------------------------
model_name = "google/flan-t5-base"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# ---------------------------
# Build RetrievalQA chain
# ---------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# ---------------------------
# HTML Templates
# ---------------------------
templates = Jinja2Templates(directory="templates")  

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": "", "question": ""})

@app.post("/ask", response_class=HTMLResponse)
def ask(request: Request, question: str = Form(...)):
    try:
        answer = qa_chain.run(question)
    except Exception as e:
        answer = f"Error generating answer: {e}"

    return templates.TemplateResponse("index.html", {"request": request, "answer": answer, "question": question})
