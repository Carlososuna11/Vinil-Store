from typing import Optional
from pydantic import BaseModel


class Artist(BaseModel):
    """
    Artist Schema
    """
    ArtistId: int
    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "ArtistId": 1,
                "Name": "John Doe"
            }
        }
