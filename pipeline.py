from extractor import PDFExtractor
from cleaner import PageCleaner
from chunker import Chunker
from summarizer import Summarizer
from gemini_client import GeminiClient


class SummarizationPipeline:
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash", pages_per_chunk: int = 10):
        # initialize components
        self.client = GeminiClient(api_key, model)
        self.extractor = PDFExtractor()
        self.cleaner = PageCleaner(self.client)
        self.chunker = Chunker(pages_per_chunk)
        self.summarizer = Summarizer(self.client)

    def run(self, pdf_bytes: bytes) -> str:
        # 1. Extract
        pages = self.extractor.extract_pages(pdf_bytes)

        # 2. Clean
        cleaned = [self.cleaner.clean(p) for p in pages]

        # 3. Chunk
        chunks = self.chunker.chunk(cleaned)

        # 4. Summarize each chunk
        chunk_summaries = [self.summarizer.summarize_chunk(ch) for ch in chunks]

        # 5. Recursive final summary
        final_summary = self.summarizer.recursive_reduce(chunk_summaries)

        return final_summary
