from typing import List
from sqlalchemy.orm import Session
from models.album import Album
from exceptions.not_found import AlbumNotFoundError
from schemas.album import AlbumSchema


class AlbumRepository:
    """
    The Album Repository Class. It contains all methods
    for the db context use.
    """

    def get_all(
        self,
        db: Session
    ) -> List[AlbumSchema]:
        """
        Get All Albums

        :param db: The db Session

        :return: List of Albums
        """
        albums_list: List[AlbumSchema] = db.query(Album).all()
        return albums_list

    def get_by_artist_id(
            self,
            db: Session,
            artist_id: int
    ) -> List[AlbumSchema]:
        """
        Get Albums by Artist Id

        :param db: The db Session
        :param artist_id: The Artist Id

        :return: List of Albums
        """
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
        """
        Get Album by Id

        :param db: The db Session
        :param album_id: The Album Id

        :return: Album
        """
        album: AlbumSchema = db.query(Album).get(album_id)
        if not album:
            raise AlbumNotFoundError(album_id)
        return album
