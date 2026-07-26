import ollama

from app.core.config import settings


class LLMService:

    def __init__(self):
        self.model = settings.OLLAMA_MODEL

    def chat(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]