# app/ingest.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

import os

# Path to PDF
pdf_path = "data/textbooks/physics.pdf"


# Load PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector store
vector_store = FAISS.from_documents(docs, embeddings)

# Save vector store locally
vector_store.save_local("faiss_index")

print("PDF ingested and vector store created successfully ✅")
