import os
import httpx

class OllamaProvider:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL", "llama3")
        self.url = "http://localhost:11434/api/chat"

    async def chat(self, messages):
        payload = {
            "model": self.model,
            "messages": messages
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=payload)
            response.raise_for_status()
            return response.json()
