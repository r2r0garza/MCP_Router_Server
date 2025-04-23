#!/bin/sh

# Health check
curl http://localhost:8000/health

# Ask endpoint (valid)
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "identity": { "user_id": "demo" },
    "memory": { "history": [] },
    "tools": [],
    "docs": [],
    "extra": {}
  }'

# Ask endpoint (invalid, missing identity)
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "memory": { "history": [] }
  }'
