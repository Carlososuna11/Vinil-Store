from typing import Optional
from pydantic import BaseModel
from schemas.album import AlbumSchema


class TrackSchema(BaseModel):
    """
    Track Schema
    """
    TrackId: int
    Name: str
    AlbumId: Optional[int]
    Album: Optional[AlbumSchema]
    MediaTypeId: int
    GenreId: Optional[int]
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "TrackId": 1,
                "Name": "Track 1",
                "AlbumId": 1,
                "MediaTypeId": 1,
                "GenreId": 1,
                "Composer": "John Doe",
                "Milliseconds": 1000,
                "Bytes": 1000,
                "UnitPrice": 1.00
            }
        }


class TrackInfoSchema(BaseModel):
    """
    Track Info Schema
    """

    Name: Optional[str]
    Composer: Optional[str]
    Milliseconds: Optional[int]
    Bytes: Optional[int]
    UnitPrice: Optional[float]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Name": "Track 1",
                "Composer": "John Doe",
                "Milliseconds": 1000,
                "Bytes": 1000,
                "UnitPrice": 1.00
            }
        }
