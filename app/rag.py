from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#  Load vectorstore 
vector_store = FAISS.load_local(
    "faiss_index",
    embeddings
)

#  Create retriever
retriever = vector_store.as_retriever()

# Load LLM from Hugging Face

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_length=200,
    temperature=0
)

llm = HuggingFacePipeline(pipeline=pipe)


# Build RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

#  Ask question
query = "Explain Newton's first law."
answer = qa_chain.run(query)

print("Question:", query)
print("Answer:", answer)
