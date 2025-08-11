# backend/app/main.py
from __future__ import annotations

from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from .core.config import get_settings

# Routers can be added later (media/search/slideshow/health/admin)
# For now, provide a health endpoint and security middleware.

app = FastAPI(title="Local Premium Media Server", version="0.1.0")

# Minimal CORS so the Vite dev server on localhost can call the API if needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost", "http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IPAllowlistMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        s = get_settings()
        client_ip = request.client.host if request.client else "127.0.0.1"
        if not s.is_ip_allowed(client_ip):
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={"detail": "Forbidden: IP not allowed"},
            )
        return await call_next(request)


app.add_middleware(IPAllowlistMiddleware)


@app.on_event("startup")
async def on_startup():
    s = get_settings()
    s.ensure_runtime_dirs()
    s.init_meili()


@app.get("/")
async def root():
    return {"ok": True, "service": app.title, "version": app.version}


@app.get("/api/health/status")
async def health():
    s = get_settings()
    meili_ok = False
    try:
        meili_ok = bool(s.meili and getattr(s.meili, "health")())
    except Exception:
        meili_ok = False
    return {
        "service": app.title,
        "version": app.version,
        "ui_theme": "Glass & Glow",
        "quiet_hours": s.jobs.quiet_hours,
        "in_quiet_hours": s.in_quiet_hours(),
        "meilisearch": {"host": s.search.meili_host, "ok": meili_ok},
    }