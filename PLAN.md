
# MCP Router Server – Implementation Plan (PLAN.md)

This implementation plan breaks the project into **six sequential phases**.  
Each phase is decomposed into **single, achievable tasks** expressed with the **SMART framework** (Specific, Measurable, Achievable, Relevant, Time‑bound).

> **Overall schedule:** The plan follows the 6‑day timeline proposed in the PRD. One “Day” ≈ one focused 6–8‑hour work session.

---

## Phase 1 – Project Scaffold & Core Router (Day 1)

| ID | Task (Specific) | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|-----------------|--------------------|---------------------|---------------|------------|
| P1‑T1 | Initialise Git repository with MIT license, `README`, `.gitignore`, and **FastAPI skeleton** (`app/main.py`, `requirements.txt`). **[COMPLETED]** | `git log` shows initial commit; `uvicorn app.main:app` returns HTTP 200 on `/health`. | Use cookiecutter‑fastapi template. | Provides foundation for all later code. | **End of Day 1** |
| P1‑T2 | Draft `.env.example` containing every variable listed in PRD. **[COMPLETED]** | File committed & reviewed; matches PRD table. | Copy PRD snippet, adjust keys. | Enables provider switching. | End of Day 1 |
| P1‑T3 | Implement **router stub**: `/ask` endpoint passes the body unchanged to a placeholder provider function. **[COMPLETED]** | Unit test returns the same text “echo” response. | 30 LOC in `router.py`. | Validates request/response path. | End of Day 1 |
| P1‑T4 | Configure **pre‑commit** with `ruff` + `black` + `mypy`, and set up GitHub Actions CI to run tests and lint. | CI badge green on first push. | Use provided action templates. | Keeps code quality high. | End of Day 1 |

---

## Phase 2 – Provider Integration (v1) (Day 2)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P2‑T1 | Implement **OpenAI backend** with model & key from `.env`. **[COMPLETED]** | Unit test: prompt “ping” → response contains non‑empty `choices`. | Use `openai>=1.0` SDK. | Mandatory cloud provider. | Mid‑Day 2 |
| P2‑T2 | Implement **LM Studio backend** (local HTTP endpoint). **[COMPLETED]** | Local integration test passes (status 200). | Simple `httpx` POST. | Enables offline dev. | Mid‑Day 2 |
| P2‑T3 | Add **OpenRouter backend** with API key. **[COMPLETED]** | Response status 200 & JSON schema matches expectations. | Same OpenAI schema. | Multi‑provider proxy. | End of Day 2 |
| P2‑T4 | Write **parameterised provider selector**: selects backend based on `LLM_PROVIDER` env. **[COMPLETED]** | Parametrised pytest matrix passes for three providers. | Strategy pattern in `providers/__init__.py`. | Core abstraction layer. | End of Day 2 |

---

## Phase 3 – Provider Integration (v1 continued) (Day 3)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P3‑T1 | Integrate **Ollama** via `/api/chat` endpoint. **[COMPLETED]** | Local llama3 test returns text. | `ollama-python` lib or raw HTTP. | Local LLM support. | Morning Day 3 |
| P3‑T2 | Integrate **Anthropic Claude** via v1 API. **[COMPLETED]** | Prompt‑response round‑trip test passes. | Use `anthropic` SDK. | Additional high‑quality model. | Mid‑Day 3 |
| P3‑T3 | Integrate **Azure Foundry AI** deployment. **[COMPLETED]** | Request returns 200 with text. | Use Azure OpenAI compat layer. | Enterprise clients. | Mid‑Day 3 |
| P3‑T4 | Update selector logic & docs to include all six providers. **[COMPLETED]** | Selector test matrix green (6×). | Extend P2‑T4 code. | Completes Phase 1 provider list. | End of Day 3 |

---

## Phase 4 – Context Schema & Validation (Day 4)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P4‑T1 | Define **Pydantic models** for MCP `Context`, `Memory`, `Identity`, `Tools`, `Docs`. **[COMPLETED]** | `schema.json` auto‑generated; docs build passes. | Use Pydantic v2. | Enforce input correctness. | Morning Day 4 |
| P4‑T2 | Add request validation middleware to `/ask`. **[COMPLETED]** | Invalid sample payload returns 422. | FastAPI dependency injection. | Protects backend. | Mid‑Day 4 |
| P4‑T3 | Implement optional `/context/{user_id}` GET/POST endpoints with in‑memory dict storage. **[COMPLETED]** | Integration tests store & retrieve context. | Simple dict (future Redis). | Completes PRD endpoints. | End of Day 4 |

---

## Phase 5 – Quality Assurance & Packaging (Day 5)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P5‑T1 | Write **pytest** suite covering 80 % lines (routers + providers). **[COMPLETED]** | `pytest --cov` ≥ 0.80. | Parametrised fixtures. | Stability. | Mid‑Day 5 |
| P5‑T2 | Create **Dockerfile** using multi‑stage build (slim Python 3.12). **[COMPLETED]** | `docker run` passes healthcheck in < 2 s. | Follow official FastAPI guide. | Easy deployment. | Mid‑Day 5 |
| P5‑T3 | Publish Docker image to registry `ghcr.io/<org>/mcp-router`. **[COMPLETED]** | Image tag v1.0 appears in GH Packages. | GitHub Actions release job. | Distribution. | End of Day 5 |
| P5‑T4 | Perform load test (Locust) for 100 RPS, latency < 500 ms for cloud providers. **[COMPLETED]** | Locust report meets SLA. | Run on small EC2. | Validate performance. | End of Day 5 |

---

## Phase 6 – Documentation & Python Client (Day 6)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P6‑T1 | Draft **README** with setup, env vars, curl examples, and architecture diagram. **[COMPLETED]** | Markdown lint passes; screenshot added. | MkDocs + Mermaid. | Dev onboarding. | Morning Day 6 |
| P6‑T2 | Generate **`.http` demos** (VS Code REST) and `curl` scripts. **[COMPLETED]** | Files in `/examples`; verified via CI. | Use real requests. | Usability. | Mid‑Day 6 |
| P6‑T3 | Publish **lightweight `mcp_client` PyPI package**. **[COMPLETED]** | `pip install mcp-client` installs; smoke test passes. | `setuptools` + GitHub Action. | Simplifies adoption. | End of Day 6 |
| P6‑T4 | Tag release **v1.0.0** and write changelog. **[COMPLETED]** | GitHub release page published. | `changelog.md` via `cz conventional`. | Marks completion. | End of Day 6 |

---

## Phase 7 – Full LLM Routing & Response Handling (Day 7)

| ID | Task | Measurable Outcome | Achievable Approach | Relevant Goal | Time‑bound |
|----|------|-------------------|---------------------|---------------|------------|
| P7‑T1 | Update `/ask` endpoint to route messages to the selected LLM provider and return the LLM's response. **[COMPLETED]** | `/ask` returns actual LLM completions, not just echo. | Call provider's `chat` method with user message. | Enables real LLM interaction. | Morning Day 7 |
| P7‑T2 | Standardize request/response schema for all providers. **[COMPLETED]** | All providers return consistent output format. | Normalize provider responses in code. | Consistent API for clients. | Mid‑Day 7 |
| P7‑T3 | Add error handling and logging for provider failures. **[COMPLETED]** | `/ask` returns clear error messages on provider errors. | Use try/except and FastAPI error responses. | Robustness and debuggability. | End of Day 7 |
| P7‑T4 | Update tests to cover real LLM routing and error cases. **[COMPLETED]** | Tests verify LLM calls and error handling. | Use pytest and mock providers. | Ensure reliability. | End of Day 7 |

---

## Risk & Mitigation Checklist

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Provider API quota limits during tests | Medium | Medium | Use small prompt; cache responses locally |
| Local model size vs Docker image | Low | Medium | Mount local models; keep image slim |
| Auth/key misconfiguration | Medium | High | Provide `.env.example` & CI env‑var checks |
| Latency variance across providers | Medium | Medium | Add retries & adaptive timeout |

---

## Acceptance Criteria

1. Switching `LLM_PROVIDER` in `.env` routes traffic to the chosen backend with no code changes.  
2. `/ask` returns coherent responses conforming to MCP schema for all six providers.  
3. Test coverage ≥ 80 % and CI pipeline green.  
4. Docker image < 300 MB and starts in < 2 s.  
5. README enables a new developer to run the service in < 10 minutes.  

---

*Last updated: 2025‑04‑22*
