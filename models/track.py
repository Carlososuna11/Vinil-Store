
from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from config_db import Base


class Track(Base):
    __tablename__ = 'tracks'

    TrackId = Column(
        Integer,
        primary_key=True
    )

    Name = Column(
        String(200),
        nullable=False
    )

    AlbumId = Column(
        Integer,
        ForeignKey('albums.AlbumId'),
        index=True,
    )

    Album = relationship(
        'Album',
        back_populates='Tracks',
        lazy='joined',
    )

    MediaTypeId = Column(
        Integer,
        ForeignKey('media_types.MediaTypeId'),
        nullable=False,
        index=True,
    )

    MediaType = relationship(
        'MediaType',
        back_populates='Tracks',
        lazy='joined',
    )

    GenreId = Column(
        Integer,
        ForeignKey('genres.GenreId'),
        index=True,
    )

    Genre = relationship(
        'Genre',
        back_populates='Tracks',
        lazy='joined',
    )

    Composer = Column(
        String(200)
    )

    Milliseconds = Column(
        Integer,
        nullable=False
    )

    Bytes = Column(
        Integer,
    )

    UnitPrice = Column(
        Numeric(10, 2),
        nullable=False
    )
