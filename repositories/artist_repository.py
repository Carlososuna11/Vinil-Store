from typing import List

from sqlalchemy.orm import Session
from config_db import Base

from schemas.artist_schemas import Artist


class ArtistRepo:

    def get_all_artists(
        self,
        db: Session
    ) -> List[Artist]:
        artist_list: List[Artist] = db.query(Base.classes.artists).all()
        return artist_list
