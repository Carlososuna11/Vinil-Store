from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship
from config_db import Base


class MediaType(Base):
    """
    Media Type Model
    """

    __tablename__ = 'media_types'

    MediaTypeId = Column(
        Integer,
        primary_key=True
    )

    Name = Column(
        String(120)
    )

    Tracks = relationship(
        'Track',
        back_populates='MediaType',
        lazy='joined',
    )
