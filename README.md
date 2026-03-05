# 📄 Conversational PDF Analyst

> Upload any PDF and ask questions in natural language — get accurate answers with **source citations and page numbers**. Powered by **RAG (Retrieval Augmented Generation)**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-Latest-yellow)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Live Demo

> Coming Soon — Deployed on Streamlit Cloud

---

## 📌 What is This?

A production-ready AI app that lets you **chat with any PDF document**:

- 📤 Upload a PDF (any size)
- 💬 Ask questions in plain English
- ✅ Get answers with **exact page numbers**
- 🚫 No hallucination — if answer isn't in PDF, it says so!

---

## 🧠 How It Works — RAG Architecture

```
User uploads PDF
      ↓
PDF split into chunks (LangChain)
      ↓
Chunks converted to vectors (HuggingFace Embeddings)
      ↓
Vectors stored in ChromaDB
      ↓
User asks a question
      ↓
Similar chunks retrieved from ChromaDB
      ↓
Chunks + Question sent to Groq LLM
      ↓
Accurate Answer + Page Numbers returned ✅
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| 🎨 Frontend | Streamlit |
| ⚙️ Backend | FastAPI |
| 🤖 AI Pipeline | LangChain |
| 🧠 LLM | Groq (llama-3.3-70b-versatile) |
| 📐 Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| 🗄️ Vector DB | ChromaDB |
| 📄 PDF Reader | PyPDF |

---

## 📁 Project Structure

```
pdf-analyst/
├── .env                    ← API Keys (never commit this!)
├── requirements.txt        ← All dependencies
├── app/
│   ├── main.py             ← FastAPI routes
│   ├── pdf_processor.py    ← PDF chunking + embedding
│   ├── rag_engine.py       ← RAG pipeline + querying
│   └── config.py           ← Settings & constants
└── frontend/
    └── streamlit_app.py    ← Streamlit UI
```

---

## ⚡ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/hanny-ai-devil/PDF-Analyst.git
cd pdf-analyst
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in root folder:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your FREE Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the App

**Terminal 1 — Start Backend:**
```bash
uvicorn app.main:app --reload
```

**Terminal 2 — Start Frontend:**
```bash
streamlit run frontend/streamlit_app.py
```

### 6. Open in Browser

```
http://localhost:8501
```

---

## 🖥️ Screenshots

> Coming Soon

---

## 📦 Requirements

```txt
fastapi
uvicorn
langchain
langchain-groq
langchain-community
langchain-core
langchain-text-splitters
langchain-huggingface
langchain-chroma
chromadb
pypdf
python-multipart
streamlit
openai
python-dotenv
sentence-transformers
```

---

## 🔑 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/upload-pdf` | Upload & process PDF |
| POST | `/ask` | Ask a question |

### Example Request — Ask Question:
```json
POST /ask
{
  "question": "What is this document about?"
}
```

### Example Response:
```json
{
  "status": "✅ Jawab mila!",
  "answer": "This document is about...",
  "sources": [
    {
      "page": 3,
      "content": "Relevant text from page 3..."
    }
  ]
}
```

---

## 🌟 Features

- ✅ Upload any PDF — no size limit
- ✅ Accurate answers with page citations
- ✅ No hallucination — honest "I don't know"
- ✅ Fast responses via Groq LLM
- ✅ Free to run — no OpenAI costs
- ✅ Simple and clean UI

---

## 🔮 Roadmap

- [ ] Multi-PDF support
- [ ] Chat history
- [ ] Deploy on Streamlit Cloud
- [ ] Support for OpenAI / Gemini
- [ ] Docker support

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License — feel free to use this project!

---

## 👨‍💻 Author

**Your Name**
- GitHub: [hanny-ai-devil](https://github.com/hanny-ai-devil)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/hanuman-das-agrawal-780b8618b/)

---

⭐ **Agar yeh project helpful laga toh star karo!** ⭐
