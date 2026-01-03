from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

db = FAISS.load_local("vector_store", OpenAIEmbeddings())
llm = ChatOpenAI(temperature=0)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

while True:
    query = input("Ask a question (or 'exit'): ")
    if query.lower() == "exit":
        break
    print(qa.run(query))