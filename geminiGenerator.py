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
        return response.text  # type: ignore
    
    def generateOnlyTokenUsage(self, prompt: str):
        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )

        usage = getattr(response, "usage_metadata", None)
        if usage:
            tokens = {
                "prompt_tokens + output_tokens": usage.prompt_token_count,
                "output_tokens": usage.candidates_token_count,
                "total_tokens": usage.total_token_count,
            }
        else:
            tokens = {"prompt_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        return tokens
    
if __name__ == "__main__":
    generator = GeminiGenerator("gemini-2.5-flash")
    print(generator.generate("Hello from Python and Gemini"))
