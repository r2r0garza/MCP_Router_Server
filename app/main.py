import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import router

app = FastAPI()

cors_urls = os.getenv("CORS_URLS", "*")
if cors_urls.strip() == "*":
    allow_origins = ["*"]
else:
    allow_origins = [url.strip() for url in cors_urls.split(",") if url.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "ok"}
