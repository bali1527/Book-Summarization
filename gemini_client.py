import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        genai.configure(api_key=api_key)
        self.model = model

    def call(self, prompt: str, max_output_tokens: int = 512) -> str:
        model_obj = genai.GenerativeModel(self.model)
        resp = model_obj.generate_content(prompt)

        try:
            return resp.text or ""
        except:
            try:
                return resp.output[0].content[0].text
            except:
                return str(resp)
