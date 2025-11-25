📚 Book Summarizer — Gemini + Streamlit .

This project is a complete PDF book summarization system built using:

Google Gemini (Generative AI)

Streamlit UI

Modular OOP architecture

PyMuPDF (fitz) for PDF text extraction

Recursive chunk summarization technique

It extracts pages from a PDF, cleans them using an LLM, chunks the content, and recursively summarizes until a single final summary is produced.

🚀 Features
✅ 1. PDF Extraction

Uses PyMuPDF to extract text from each page.

✅ 2. LLM-Powered Text Cleaning

Each page is cleaned using Gemini:

Removes noise (headers/footers)

Fixes OCR errors

Preserves structure

✅ 3. Smart Chunking

Pages are grouped (default: 10 pages per chunk) to manage long documents efficiently.

✅ 4. Recursive Summarization

Chunk summaries are repeatedly merged and summarized until only one final summary remains.

✅ 5. Streamlit Interface

A clean UI to:

Upload PDFs

Configure chunk settings

View intermediate results

Download final summary

✅ 6. Clean OOP Design

The system is split into reusable components:

PDFExtractor → Cleaner → Chunker → Summarizer → GeminiClient → Pipeline


Each class handles only one responsibility.

🏗 Project Structure
summarizer_oops/
│── app.py                # Streamlit interface
│── pipeline.py           # Orchestrates the entire flow
│── extractor.py          # PDF page extraction
│── cleaner.py            # Page text cleaning (LLM)
│── chunker.py            # Chunk grouping logic
│── summarizer.py         # Recursive summarization
│── gemini_client.py      # Gemini API wrapper
│── requirements.txt      # Dependencies
│── .env                  # Holds GEMINI_API_KEY
