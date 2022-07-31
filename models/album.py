from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from config_db import Base


class Album(Base):
    """
    Album Model
    """

    __tablename__ = 'albums'

    AlbumId = Column(
        Integer,
        primary_key=True
    )

    Title = Column(
        String(160)
    )

    ArtistId = Column(
        Integer,
        ForeignKey('artists.ArtistId')
    )

    Artist = relationship(
        'Artist',
        back_populates='Albums',
        lazy='joined',
    )

    Tracks = relationship(
        'Track',
        back_populates='Album',
        lazy='joined',
    )
