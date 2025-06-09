import os
import httpx

class AnthropicProvider:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model = os.getenv("MODEL", "claude-3-5-sonnet-20241022")
        self.url = os.getenv("ANTRHOPIC_URL")
        #"https://api.anthropic.com/v1/messages"

    async def chat(self, messages):
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        # Ensure messages are in the correct format and add max_tokens
        payload = {
            "model": self.model,
            "max_tokens": 1024,
            "temperature": 0.1,
            "messages": [
                {"role": m.get("role", "user"), "content": m.get("content", "")}
                for m in messages
            ]
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
