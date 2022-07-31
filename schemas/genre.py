from typing import Optional
from pydantic import BaseModel


class GenreSchema(BaseModel):
    """
    Genre Schema
    """

    GenreId: int

    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "GenreId": 1,
                "Name": "Jazz"
            }
        }
