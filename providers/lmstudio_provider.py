import os
import httpx

class LMStudioProvider:
    def __init__(self):
        self.url = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1/chat/completions")
        self.api_key = os.getenv("LMSTUDIO_API_KEY")

    async def chat(self, messages):
        payload = {
            "messages": messages
        }
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
