from typing import List
from sqlalchemy.orm import Session
from models.album import Album
from exceptions.not_found import AlbumNotFoundError
from schemas.album import AlbumSchema


class AlbumRepository:

    def get_all(
        self,
        db: Session
    ) -> List[AlbumSchema]:
        albums_list: List[AlbumSchema] = db.query(Album).all()
        return albums_list

    def get_by_artist_id(
            self,
            db: Session,
            artist_id: int
    ) -> List[AlbumSchema]:
        albums_list: List[AlbumSchema] = db.query(
            Album
        ).filter(
            Album.ArtistId == artist_id
        ).all()
        return albums_list

    def get_by_id(
            self,
            db: Session,
            album_id: int
    ) -> AlbumSchema:
        album: AlbumSchema = db.query(Album).get(album_id)
        if not album:
            raise AlbumNotFoundError(album_id)
        return album
