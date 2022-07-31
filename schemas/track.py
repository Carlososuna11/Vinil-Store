from typing import Optional
from pydantic import BaseModel
from schemas.album import AlbumSchema
from schemas.media_type import MediaType
from schemas.genre import GenreSchema


class TrackSchema(BaseModel):
    """
    Track Schema
    """

    TrackId: int

    Name: str

    AlbumId: Optional[int]

    Album: Optional[AlbumSchema]

    MediaTypeId: int

    MediaType: Optional[MediaType]

    GenreId: Optional[int]

    Genre: Optional[GenreSchema]

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
                "Album": {
                    "AlbumId": 1,
                    "Title": "The Best Album",
                    "ArtistId": 1,
                    "Artist": {
                        "ArtistId": 1,
                        "Name": "John Doe"
                    }
                },
                "MediaTypeId": 1,
                "MediaType": {
                    "MediaTypeId": 1,
                    "Name": "CD"
                },
                "GenreId": 1,
                "Genre": {
                    "GenreId": 1,
                    "Name": "Jazz"
                },
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

    Name: str

    Composer: Optional[str]

    Milliseconds: int

    Bytes: Optional[int]

    UnitPrice: float

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
