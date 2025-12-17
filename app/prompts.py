# app/prompts.py
from langchain.prompts import PromptTemplate

# Example template
qa_template = PromptTemplate(
    input_variables=["context", "question"],
    template="Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}\nAnswer:"
)
