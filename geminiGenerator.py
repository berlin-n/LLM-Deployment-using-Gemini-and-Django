from google import genai

class GeminiGenerator:
    def __init__(self, model: str):
        self.client = genai.Client()
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )
        return response.text 
    
    def generateOnlyTokenUsage(self, prompt: str):
        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )
        return response.usage_metadata
    
if __name__ == "__main__":
    generator = GeminiGenerator("gemini-2.5-flash")
    print(generator.generate("Hello from Python and Gemini"))
