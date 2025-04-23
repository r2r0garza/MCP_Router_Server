from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_ask_valid(monkeypatch):
    # Mock provider to avoid real LLM call
    class DummyProvider:
        async def chat(self, messages):
            return {"choices": [{"message": {"role": "assistant", "content": "Hello, world!"}}]}
    from providers import get_provider
    monkeypatch.setattr("providers.get_provider", lambda: DummyProvider())

    payload = {
        "identity": {"user_id": "u1"},
        "memory": {"history": [{"role": "user", "content": "hi"}]},
        "tools": [],
        "docs": [],
        "extra": {}
    }
    resp = client.post("/ask", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "choices" in data
    assert data["choices"][0]["message"]["content"] == "Hello, world!"

def test_ask_invalid():
    # Missing required 'identity'
    payload = {}
    resp = client.post("/ask", json=payload)
    assert resp.status_code == 422

def test_ask_provider_error(monkeypatch):
    class FailingProvider:
        async def chat(self, messages):
            raise Exception("LLM failure")
    from providers import get_provider
    monkeypatch.setattr("providers.get_provider", lambda: FailingProvider())

    payload = {
        "identity": {"user_id": "u1"},
        "memory": {"history": [{"role": "user", "content": "hi"}]},
        "tools": [],
        "docs": [],
        "extra": {}
    }
    resp = client.post("/ask", json=payload)
    assert resp.status_code == 502
    assert "error" in resp.json()
