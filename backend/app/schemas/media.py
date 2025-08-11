from pydantic import BaseModel

class MediaItemOut(BaseModel):
    id: int
    path: str
    media_type: str
    title: str
    rating: float
    thumbnail_256: str
    thumbnail_512: str
    thumbnail_1024: str
    poster_1280: str

    class Config:
        from_attributes = True
