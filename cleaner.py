CLEAN_PROMPT = """
You are a careful text cleaner. Clean the following page:
- remove page numbers
- fix OCR errors
- preserve paragraphs
- output clean text only

Text:
'''{text}'''
"""

class PageCleaner:
    def __init__(self, client):
        self.client = client

    def clean(self, page_text: str) -> str:
        if not page_text.strip():
            return ""

        prompt = CLEAN_PROMPT.format(text=page_text)
        return self.client.call(prompt, max_output_tokens=768)
