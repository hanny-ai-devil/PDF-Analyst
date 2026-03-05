from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import (
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    CHROMA_DB_PATH,
    COLLECTION_NAME
)
import os

def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages

def split_into_chunks(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(pages)
    return chunks

def get_embedding_model():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    return embeddings

def store_in_chromadb(chunks):
    embeddings = get_embedding_model()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DB_PATH
    )
    return vectorstore

def process_pdf(file_path: str):
    print("📄 PDF parh raha hun...")
    pages = load_pdf(file_path)
    print(f"✅ {len(pages)} pages mili!")
    
    print("✂️ Chunks bana raha hun...")
    chunks = split_into_chunks(pages)
    print(f"✅ {len(chunks)} chunks bane!")
    
    print("🧠 Vectors bana ke ChromaDB mein save kar raha hun...")
    vectorstore = store_in_chromadb(chunks)
    print("✅ PDF process complete!")
    return vectorstore