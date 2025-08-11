from fastapi import APIRouter
from app.services.indexer import upsert_media
from app.models.db import Base, engine

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.post("/init-db")
def init_db():
    Base.metadata.create_all(bind=engine)
    return {"ok": True}

@router.post("/index")
def index_now():
    upsert_media()
    return {"ok": True, "message": "Index updated"}
