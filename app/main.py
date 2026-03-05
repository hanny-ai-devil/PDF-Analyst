from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
from app.pdf_processor import process_pdf
from app.rag_engine import ask_question

# ================================
# FASTAPI APP BANAO
# ================================
app = FastAPI(
    title="PDF Analyst API",
    description="PDF upload karo aur sawaal poochho!",
    version="1.0.0"
)

# ================================
# CORS — Frontend Se Baat Karne Do
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ================================
# TEMPORARY FOLDER — PDF SAVE HOGI
# ================================
UPLOAD_FOLDER = "./uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================================
# REQUEST MODEL
# ================================
class QuestionRequest(BaseModel):
    question: str

# ================================
# ROUTE 1 — Health Check
# ================================
@app.get("/")
def home():
    return {"status": "✅ PDF Analyst API Running!"}

# ================================
# ROUTE 2 — PDF Upload
# ================================
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Sirf PDF allow karo
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="❌ Sirf PDF files allowed hain!"
        )
    
    # PDF save karo
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # PDF process karo
    try:
        process_pdf(file_path)
        return {
            "status": "✅ PDF successfully upload aur process ho gayi!",
            "filename": file.filename
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"❌ Error: {str(e)}"
        )

# ================================
# ROUTE 3 — Question Poochho
# ================================
@app.post("/ask")
async def ask(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="❌ Sawaal khali nahi hona chahiye!"
        )
    
    try:
        result = ask_question(request.question)
        return {
            "status": "✅ Jawab mila!",
            "answer": result["answer"],
            "sources": result["sources"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"❌ Error: {str(e)}"
        )
