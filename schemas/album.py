from typing import Optional
from pydantic import BaseModel
from schemas.artist import ArtistSchema


class AlbumSchema(BaseModel):
    """
    Album Schema
    """

    AlbumId: int

    Title: Optional[str]

    ArtistId: Optional[int]

    Artist: Optional[ArtistSchema]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "AlbumId": 1,
                "Title": "The Best Album",
                "ArtistId": 1,
                "Artist": {
                    "ArtistId": 1,
                    "Name": "John Doe"
                }
            }
        }


class AlbumTitleSchema(BaseModel):
    """
    Album Title Schema
    """

    Title: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Title": "The Best Album"
            }
        }
