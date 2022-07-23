from typing import Optional
from pydantic import BaseModel


class ArtistSchema(BaseModel):
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


class ArtistNameSchema(BaseModel):
    """
    Artist Name Schema
    """
    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Name": "John Doe"
            }
        }
