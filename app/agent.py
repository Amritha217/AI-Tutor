from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_index", embeddings)
retriever = vector_store.as_retriever()

# Load model locally
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)  # CPU

# Define a LangChain-compatible LLM wrapper
from langchain.llms import HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=pipe)

# Build RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

query = "Explain Newton's first law."
answer = qa_chain.run(query)

print("Question:", query)
print("Answer:", answer)
