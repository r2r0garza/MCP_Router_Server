from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Tool(BaseModel):
    name: str
    description: Optional[str] = None

class Docs(BaseModel):
    url: str
    summary: Optional[str] = None

class Identity(BaseModel):
    user_id: str
    username: Optional[str] = None

class Memory(BaseModel):
    history: List[Dict[str, Any]] = Field(default_factory=list)

class Context(BaseModel):
    identity: Identity
    memory: Optional[Memory] = None
    tools: Optional[List[Tool]] = None
    docs: Optional[List[Docs]] = None
    extra: Optional[Dict[str, Any]] = None
