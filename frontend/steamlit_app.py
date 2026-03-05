import streamlit as st
import requests

# ================================
# PAGE SETTINGS
# ================================
st.set_page_config(
    page_title="PDF Analyst",
    page_icon="📄",
    layout="centered"
)

# ================================
# API URL
# ================================
API_URL = "http://127.0.0.1:8000"

# ================================
# HEADING
# ================================
st.title("📄 Conversational PDF Analyst")
st.markdown("**PDF upload karo aur sawaal poochho!**")
st.divider()

# ================================
# SECTION 1 — PDF UPLOAD
# ================================
st.subheader("📤 Step 1 — PDF Upload Karo")

uploaded_file = st.file_uploader(
    "PDF file choose karo",
    type=["pdf"]
)

if uploaded_file is not None:
    # Upload button
    if st.button("🚀 PDF Process Karo"):
        with st.spinner("⏳ PDF process ho rahi hai..."):
            # FastAPI ko PDF bhejo
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            response = requests.post(f"{API_URL}/upload-pdf", files=files)

            if response.status_code == 200:
                st.success("✅ PDF successfully process ho gayi!")
                st.session_state["pdf_ready"] = True
            else:
                st.error(f"❌ Error: {response.json()['detail']}")

st.divider()

# ================================
# SECTION 2 — SAWAAL POOCHHO
# ================================
st.subheader("💬 Step 2 — Sawaal Poochho")

# Pehle PDF upload honi chahiye
if not st.session_state.get("pdf_ready"):
    st.warning("⚠️ Pehle PDF upload karo!")
else:
    question = st.text_input(
        "Apna sawaal likho:",
        placeholder="Jaise: Yeh document kis baare mein hai?"
    )

    if st.button("🔍 Jawab Dhoondo"):
        if question.strip() == "":
            st.warning("⚠️ Sawaal khali nahi hona chahiye!")
        else:
            with st.spinner("🤔 Jawab dhoond raha hun..."):
                # FastAPI ko sawaal bhejo
                response = requests.post(
                    f"{API_URL}/ask",
                    json={"question": question}
                )

                if response.status_code == 200:
                    data = response.json()

                    # Answer dikhao
                    st.subheader("✅ Jawab:")
                    st.write(data["answer"])

                    # Sources dikhao
                    st.subheader("📚 Sources:")
                    for source in data["sources"]:
                        with st.expander(f"📄 Page {source['page']}"):
                            st.write(source["content"])
                else:
                    st.error(f"❌ Error: {response.json()['detail']}")