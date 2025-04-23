# MCP Router Server - Product Requirements Document (PRD)

## Title
**MCP Router Server for LLM Provider Abstraction**

## Purpose
To build an **MCP-compliant server** that serves as a unified context and request router to multiple LLM providers (e.g., OpenAI, LM Studio, OpenRouter, Ollama, Claude, etc.). This will allow any external application (e.g., a Python-based chatbot, CLI tool, or web app) to interact with the LLMs using a standardized interface without needing to know or handle the provider-specific logic.

## Goals
- Build an **MCP-compliant REST API** that accepts context and chat requests.
- Support multiple LLM providers via environment config.
- Allow easy switching between providers without changes to consuming applications.
- Expose a simple and consistent API to external apps (e.g., Python clients).
- Add support for memory, identity, and tool schema blocks as part of MCP context.

## Target Users
- Developers building AI applications who want to abstract LLM routing logic.
- Backend services and agent frameworks that consume structured context.
- Internal tools requiring dynamic LLM access without hardcoding providers.

## Requirements

### Functional Requirements
1. **LLM Provider Abstraction Layer**
   - Load model/provider settings from `.env`
   - Route request to the correct backend (OpenAI, LM Studio, OpenRouter, etc.)

2. **MCP-Compliant Context Handling**
   - Accept JSON payloads matching MCP schema:
     ```json
     {
       "context": {
         "memory": {},
         "identity": {},
         "tools": [],
         "docs": []
       },
       "message": "User's prompt here"
     }
     ```

3. **MCP Endpoint Design**
   - `POST /ask` → Accepts full context + user message, returns response
   - `GET /context/{user_id}` → Optional user-level context retrieval
   - `POST /context/{user_id}` → Optional user-level context storage

4. **Provider Integration (Phase 1)**
   - ✅ OpenAI API (GPT-4, GPT-3.5)
   - ✅ LM Studio (local inference endpoint)
   - ✅ OpenRouter (proxy to multiple providers)
   - ✅ Ollama (local LLM host)
   - ✅ Anthropic Claude
   - ✅ Azure Foundry AI

5. **Provider Integration (Phase 2)**
   - Together.ai
   - Other custom providers as plugins

6. **Environment Config (.env)**
   ```env
   LLM_PROVIDER=openai
   MODEL=gpt-4
   OPENAI_API_KEY=...
   LMSTUDIO_URL=http://localhost:1234
   OPENROUTER_API_KEY=...
   OLLAMA_MODEL=llama3
   ANTHROPIC_API_KEY=...
   AZURE_FOUNDY_API_KEY=...
   AZURE_FOUNDY_DEPLOYMENT=...
   ```

7. **Python Client Library (optional)**
   - Lightweight wrapper to simplify requests from other apps
   - Example:
     ```python
     from mcp_client import ask
     response = ask(message="What's the weather?", identity={"username": "Arturo"})
     ```

### Non-Functional Requirements
- Must be stateless (context is passed per request unless memory is persisted)
- Fast response time (<500ms latency for non-local providers)
- Secure API access (optional API key-based auth)
- Easily deployable via Docker

## Out of Scope (for v1)
- Fine-tuned models or vector DB integration
- Multi-turn dialogue memory across sessions
- Rate-limiting, analytics, or billing features

## Tech Stack
- **Backend:** Python + FastAPI
- **Runtime:** Dockerized service
- **Storage (optional):** SQLite or Redis (for context/memory)
- **LLM SDKs:** openai, requests/httpx, local inference wrappers

## Deliverables
- MCP-compliant FastAPI server
- .env-based provider configuration
- Sample `.http` and `curl` requests
- README with setup instructions
- Optional: Python client library

## Timeline
| Milestone                        | ETA         |
|----------------------------------|-------------|
| Project scaffold + routing logic| Day 1       |
| OpenAI + LM Studio support      | Day 2       |
| OpenRouter + Ollama support     | Day 3       |
| Context schema + validation     | Day 4       |
| Testing + Docker packaging      | Day 5       |
| README + Python client          | Day 6       |

## Success Criteria
- Can hot-swap LLM providers by editing `.env`
- External apps can send context and receive meaningful responses
- Response times and output match expectations per provider
- Compliant with MCP structure (context, tools, identity blocks)

## Future Considerations
- Add streaming (`/ask/stream`) support
- Plug into LangGraph, CrewAI, or LangChain
- Support dynamic tool registration (via plugin system)
- Embed memory or RAG retrieval layer

---

This PRD sets the foundation for an extensible, portable, and provider-agnostic LLM routing server using MCP. Ideal for use in multi-agent architectures, custom chat UIs, or as an abstraction layer in DevOps and AI workflows.
