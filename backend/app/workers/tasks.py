from __future__ import annotations

from .celery_app import celery_app, quiet_countdown
from ..core.config import load_config


@celery_app.task(name="index.scan", queue="default")
def index_scan() -> dict:
    cfg = load_config()
    # TODO: walk filesystem, persist to DB, push to Meilisearch, enqueue thumbs
    return {"ok": True, "images_root": cfg.paths.images_root, "videos_root": cfg.paths.videos_root}


@celery_app.task(name="thumbs.generate", queue="thumbs")
def thumbs_generate(media_id: str) -> dict:
    # TODO: generate thumbnails and cache them
    return {"ok": True, "media_id": media_id}


@celery_app.task(name="ai.tag", queue="ai")
def ai_tag(media_id: str) -> dict:
    # TODO: run embeddings / local LMM for labels & captions
    return {"ok": True, "media_id": media_id}


# Convenience enqueue helpers that respect quiet hours

def enqueue_index_scan() -> None:
    cd = quiet_countdown()
    index_scan.apply_async(countdown=cd if cd else None)


def enqueue_thumb(media_id: str) -> None:
    cd = quiet_countdown()
    thumbs_generate.apply_async(kwargs={"media_id": media_id}, countdown=cd if cd else None)


def enqueue_ai_tag(media_id: str) -> None:
    cd = quiet_countdown()
    ai_tag.apply_async(kwargs={"media_id": media_id}, countdown=cd if cd else None)