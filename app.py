import streamlit as st

st.set_page_config(page_title="Voice Assistant")

st.title("📄 Voice Assistant")

st.write("Welcome to my Voice Assistant!")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully!")
