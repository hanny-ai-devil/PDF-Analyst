from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import (
    GROQ_API_KEY,
    LLM_MODEL,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
    COLLECTION_NAME
)

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_PATH
    )
    return vectorstore

def get_retriever():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    return retriever

def get_prompt():
    template = """
    Tum ek helpful PDF assistant ho.
    Neeche diye gaye context ke basis pe sawal ka jawab do.
    
    Agar jawab context mein nahi hai toh:
    "Mujhe is sawaal ka jawab PDF mein nahi mila." — yeh likho.
    
    Kabhi bhi apni taraf se jawab mat banao.
    
    Context:
    {context}
    
    Sawal: {question}
    
    Jawab (source page number bhi batao):
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

def get_llm():
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0
    )
    return llm

def format_context(docs):
    formatted = []
    for doc in docs:
        page_num = doc.metadata.get("page", "Unknown")
        content = doc.page_content
        formatted.append(f"[Page {page_num + 1}]:\n{content}")
    return "\n\n".join(formatted)

def ask_question(question: str):
    retriever = get_retriever()
    llm = get_llm()
    prompt = get_prompt()
    
    docs = retriever.invoke(question)
    context = format_context(docs)
    
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({
        "context": context,
        "question": question
    })
    
    sources = []
    for doc in docs:
        page_num = doc.metadata.get("page", 0)
        sources.append({
            "page": page_num + 1,
            "content": doc.page_content[:200]
        })
    
    return {
        "answer": answer,
        "sources": sources
    }