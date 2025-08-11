import json, os, hashlib
from pathlib import Path
from typing import Iterable
from PIL import Image
from app.core.config import get_settings
from app.models.db import SessionLocal
from app.models.media import MediaItem

IMAGE_EXTS = {".jpg",".jpeg",".png",".webp",".gif",".bmp",".tiff",".avif"}
VIDEO_EXTS = {".mp4",".mov",".mkv",".avi",".webm",".m4v",".hevc",".heic",".heif"}  # heic/heif as images if decoded later

def file_hash(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def iter_media_files(root: str) -> Iterable[Path]:
    p = Path(root)
    for fp in p.rglob("*"):
        if fp.is_file() and fp.suffix.lower() in IMAGE_EXTS | VIDEO_EXTS:
            yield fp

def load_sidecar(media_path: Path) -> dict:
    sc = media_path.with_suffix(media_path.suffix + ".json")
    if sc.exists():
        try:
            return json.loads(sc.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def inspect_image_dims(path: Path) -> tuple[int,int]:
    try:
        with Image.open(path) as im:
            return int(im.width), int(im.height)
    except Exception:
        return 0, 0

def upsert_media():
    s = get_settings()
    db = SessionLocal()
    try:
        roots = [s.images_root, s.videos_root]
        for root in roots:
            for fp in iter_media_files(root):
                ext = fp.suffix.lower()
                mtype = "image" if ext in IMAGE_EXTS else "video"
                sidecar = load_sidecar(fp)
                title = sidecar.get("title", fp.stem)
                h = sidecar.get("hash") or file_hash(fp)

                width = height = duration_ms = 0
                if mtype == "image":
                    width, height = inspect_image_dims(fp)

                item = db.query(MediaItem).filter_by(path=str(fp)).first()
                if not item:
                    item = MediaItem(path=str(fp))
                item.media_type = mtype
                item.title = title
                item.hash = h
                item.rating = float(sidecar.get("rating", 0.0))
                item.sidecar_path = str(fp.with_suffix(fp.suffix + ".json"))
                item.width = width; item.height = height; item.duration_ms = duration_ms
                db.add(item)
        db.commit()
    finally:
        db.close()
