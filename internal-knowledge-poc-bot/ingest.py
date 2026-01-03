from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import os

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

loader = TextLoader("docs/sample.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

db = FAISS.from_documents(chunks, OpenAIEmbeddings())
db.save_local("vector_store")

print("✅ Documents ingested successfully")