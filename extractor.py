import fitz

class PDFExtractor:
    def extract_pages(self, pdf_bytes: bytes) -> list[str]:
        pages = []
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text = page.get_text("text") or ""
                pages.append(text.strip())
        return pages
