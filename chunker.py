class Chunker:
    def __init__(self, pages_per_chunk: int = 10):
        self.pages_per_chunk = pages_per_chunk

    def chunk(self, pages: list[str]) -> list[str]:
        chunks = []
        for i in range(0, len(pages), self.pages_per_chunk):
            group = pages[i:i+self.pages_per_chunk]
            chunks.append("\n\n".join(group).strip())
        return chunks
