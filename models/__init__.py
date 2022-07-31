"""
Import the models because SQL Alchemy can't found
the relationship when use sqlalchemy.orm.relationship
"""

from models.album import Album  # noqa: F401
from models.artist import Artist    # noqa: F401
from models.track import Track  # noqa: F401
from models.genre import Genre  # noqa: F401
from models.media_type import MediaType  # noqa: F401
