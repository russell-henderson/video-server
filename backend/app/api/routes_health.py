from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter(prefix="/api/health", tags=["health"])

@router.get("/status")
def status():
    s = get_settings()
    return {
        "ok": True,
        "meilisearch": s.meili_host,
        "cache_root": s.cache_root,
        "quiet_hours": s.quiet_hours,
        "max_workers": s.max_workers,
    }
