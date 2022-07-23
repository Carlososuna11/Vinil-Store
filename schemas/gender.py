from typing import Optional
from pydantic import BaseModel


class GenderSchema(BaseModel):
    """
    Gender Schema
    """

    GenderId: int

    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "GenderId": 1,
                "Name": "Jazz"
            }
        }
