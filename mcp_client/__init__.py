import requests

class MCPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def health(self):
        resp = requests.get(f"{self.base_url}/health")
        resp.raise_for_status()
        return resp.json()

    def ask(self, context: dict):
        resp = requests.post(f"{self.base_url}/ask", json=context)
        resp.raise_for_status()
        return resp.json()
