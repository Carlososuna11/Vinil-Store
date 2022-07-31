from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship
from config_db import Base


class Artist(Base):
    """
    Artist Model
    """

    __tablename__ = 'artists'

    ArtistId = Column(
        Integer,
        primary_key=True
    )

    Name = Column(
        String(120)
    )

    Albums = relationship(
        'Album',
        back_populates='Artist',
        lazy='joined',
    )
