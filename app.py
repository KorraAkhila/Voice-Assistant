import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Voice Assistant")

st.title("📄 Voice Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    st.success("PDF uploaded successfully!")

    st.subheader("Extracted Text")

    st.text_area("PDF Content", text, height=300)
