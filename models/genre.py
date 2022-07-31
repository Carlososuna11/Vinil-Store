from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship
from config_db import Base


class Genre(Base):
    """
    Genre Model
    """

    __tablename__ = 'genres'

    GenreId = Column(
        Integer,
        primary_key=True
    )

    Name = Column(
        String(120)
    )

    Tracks = relationship(
        'Track',
        back_populates='Genre',
        lazy='joined',
    )
