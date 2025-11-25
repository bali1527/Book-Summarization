import os
from dotenv import load_dotenv
import streamlit as st
from pipeline import SummarizationPipeline

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Book Summarizer", layout="wide")
st.title("📚 Book Summarizer")

uploaded = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded and st.button("Summarize"):
    pipeline = SummarizationPipeline(
        api_key=API_KEY,
        model="gemini-2.0-flash",
        pages_per_chunk=10
    )

    with st.spinner("Summarizing..."):
        pdf_bytes = uploaded.read()
        summary = pipeline.run(pdf_bytes)

    st.subheader("Final Summary")
    st.write(summary)

    st.download_button("Download Summary", summary, "summary.txt")
