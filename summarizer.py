SUMMARY_PROMPT = """
Summarize the following text concisely and clearly:

Text:
'''{text}'''
"""

class Summarizer:
    def __init__(self, client):
        self.client = client

    def summarize_chunk(self, text: str) -> str:
        prompt = SUMMARY_PROMPT.format(text=text)
        return self.client.call(prompt)

    def recursive_reduce(self, summaries: list[str]) -> str:
        current = summaries[:]

        while len(current) > 1:
            next_level = []
            for i in range(0, len(current), 2):
                pair = current[i:i+2]
                if len(pair) == 1:
                    next_level.append(pair[0])
                else:
                    merged = "\n\n".join(pair)
                    summary = self.summarize_chunk(merged)
                    next_level.append(summary)

            current = next_level

        return current[0]
