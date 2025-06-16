from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

def load_documents_from_folder(folder_path="data/source_docs"):
    """
    Load and split all .md/.txt files from the specified folder into chunks.
    """
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".md") or file.endswith(".txt"):
            loader = TextLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())
    return docs

def create_vector_store(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    return db

def retrieve_relevant_chunks(prompt, db, k=3):
    return db.similarity_search(prompt, k=k)
