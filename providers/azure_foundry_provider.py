import os
import httpx

class AzureFoundryProvider:
    def __init__(self):
        self.api_key = os.getenv("AZURE_FOUNDY_API_KEY")
        self.deployment = os.getenv("AZURE_FOUNDY_DEPLOYMENT")
        self.model = os.getenv("MODEL")
        self.version = os.getenv("VERSION")
        self.url = f"https://{self.deployment}.openai.azure.com/openai/deployments/{self.model}/chat/completions?api-version={self.version}"

    async def chat(self, messages):
        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "messages": messages
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(self.url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
