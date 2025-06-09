import os
import httpx

class OpenAIProvider:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("MODEL", "gpt-4o-mini")
        self.url = os.getenv("OPENAI_URL")
        #"https://api.openai.com/v1/chat/completions"

    async def chat(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.1
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
