import os
import httpx

class AzureFoundryProvider:
    def __init__(self):
        self.api_key = os.getenv("AZURE_FOUNDY_API_KEY")
        self.deployment = os.getenv("AZURE_FOUNDY_DEPLOYMENT")
        self.model = os.getenv("MODEL")
        self.version = os.getenv("VERSION")
        self.url_template = "https://{deployment}.openai.azure.com/openai/deployments/{model}/chat/completions?api-version={version}"

    async def chat(self, messages, assistant=None):
        """
        Sends a chat message to Azure Foundry AI or a specific assistant if specified.

        :param messages: List of message dictionaries for the conversation.
        :param assistant: Optional assistant deployment name.
        :return: JSON response from the API.
        """
        deployment = assistant if assistant else self.deployment
        url = self.url_template.format(deployment=deployment, model=self.model, version=self.version)

        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "messages": messages
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()