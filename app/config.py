from dotenv import load_dotenv
import os

# .env file se saari keys load karo
load_dotenv()

# ================================
# API KEYS
# ================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ================================
# MODEL SETTINGS
# ================================
LLM_MODEL = "llama-3.3-70b-versatile" # Groq ka free model
EMBEDDING_MODEL = "all-MiniLM-L6-v2" # Free local embedding

# ================================
# PDF SETTINGS
# ================================
CHUNK_SIZE = 1000      # Ek chunk mein kitne characters
CHUNK_OVERLAP = 200    # Chunks ke beech overlap

# ================================
# VECTOR STORE SETTINGS
# ================================
CHROMA_DB_PATH = "./chroma_db"   # ChromaDB kahaan save hogi
COLLECTION_NAME = "pdf_documents" # Collection ka naam