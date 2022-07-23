from typing import List
from sqlalchemy.orm import Session
from models.artist import Artist
from exceptions.not_found import ArtistNotFoundError
from schemas.artist import ArtistSchema


class ArtistRepository:

    def get_all(
        self,
        db: Session
    ) -> List[ArtistSchema]:
        artists_list: List[ArtistSchema] = db.query(Artist).all()
        return artists_list

    def get_by_id(
            self,
            db: Session,
            artist_id: int
    ) -> ArtistSchema:
        artist: ArtistSchema = db.query(Artist).get(artist_id)
        if not artist:
            raise ArtistNotFoundError(artist_id)
        return artist
