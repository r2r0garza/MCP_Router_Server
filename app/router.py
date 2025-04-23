from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas import Context
from providers import get_provider
import logging

router = APIRouter()

@router.post("/ask")
async def ask(context: Context):
    provider = get_provider()
    # Convert MCP Context to provider message format
    messages = context.extra.get("messages") if context.extra and "messages" in context.extra else []
    if not messages and context.memory and context.memory.history:
        messages = context.memory.history
    if not messages:
        # Fallback: try to build a message from context
        if hasattr(context, "message"):
            messages = [{"role": "user", "content": context.message}]
        else:
            raise HTTPException(status_code=400, detail="No messages provided in context.")

    try:
        result = await provider.chat(messages)
        # Standardize response: always return {"choices": [...]}
        if isinstance(result, dict) and "choices" in result:
            return JSONResponse(content={"choices": result["choices"]})
        elif isinstance(result, dict) and "result" in result:
            return JSONResponse(content={"choices": [result["result"]]})
        else:
            return JSONResponse(content={"choices": [result]})
    except Exception as e:
        logging.exception("Provider error")
        return JSONResponse(
            status_code=502,
            content={"error": "Provider error", "detail": str(e)}
        )
