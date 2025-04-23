from typing import Dict, Any

# In-memory context store (for demo; replace with Redis or DB in production)
_context_store: Dict[str, Any] = {}

def get_context(user_id: str):
    return _context_store.get(user_id)

def set_context(user_id: str, context: Any):
    _context_store[user_id] = context
