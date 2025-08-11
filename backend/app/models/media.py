from sqlalchemy import Column, Integer, String, Boolean, Float
from .db import Base

class MediaItem(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, unique=True, index=True, nullable=False)
    media_type = Column(String, index=True)  # "image" | "video"
    title = Column(String, default="")
    hash = Column(String, index=True, default="")
    rating = Column(Float, default=0.0)
    favorite = Column(Boolean, default=False)
    width = Column(Integer, default=0)
    height = Column(Integer, default=0)
    duration_ms = Column(Integer, default=0)
    sidecar_path = Column(String, default="")
    thumbnail_256 = Column(String, default="")
    thumbnail_512 = Column(String, default="")
    thumbnail_1024 = Column(String, default="")
    poster_1280 = Column(String, default="")
