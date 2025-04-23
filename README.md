# MCP Router Server

A FastAPI-based MCP-compliant server that routes requests to multiple LLM providers (OpenAI, LM Studio, OpenRouter, Ollama, Claude, Azure, etc.) via a unified REST API.

## Features

- Switch LLM providers by editing `.env`
- `/ask` endpoint for context-aware chat requests
- Health check at `/health`
- Provider abstraction for OpenAI, LM Studio, OpenRouter, Ollama, Anthropic Claude, Azure Foundry AI
- Easy deployment and configuration

## Quickstart

1. **Install dependencies**  
   (Python 3.8+ required, only pure Python packages supported in this environment)
   ```
   pip install -r requirements.txt
   ```

2. **Copy and edit environment variables**
   ```
   cp .env.example .env
   # Edit .env to set your provider keys and options
   ```

3. **Run the server**
   ```
   uvicorn app.main:app --reload
   ```

4. **Test health check**
   ```
   curl http://localhost:8000/health
   ```

5. **Test /ask endpoint**
   ```
   curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "identity": { "user_id": "demo" },
    "memory": { "history": [] },
    "tools": [],
    "docs": [],
    "extra": {}
  }'
   ```

## Environment Variables

See `.env.example` for all supported variables.

## Project Structure

```
app/
  __init__.py
  main.py
  router.py
.env.example
requirements.txt
.gitignore
LICENSE
README.md
```

## License

MIT License
