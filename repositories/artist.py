from typing import List
from sqlalchemy.orm import Session
from models.artist import Artist
from exceptions.not_found import ArtistNotFoundError
from schemas.artist import ArtistSchema


class ArtistRepository:
    """
    The Artist Repository Class. It contains all methods
    for the db context use.
    """

    def get_all(
        self,
        db: Session
    ) -> List[ArtistSchema]:
        """
        Get All Artists

        :param db: The db Session

        :return: List of Artists
        """
        artists_list: List[ArtistSchema] = db.query(Artist).all()
        return artists_list

    def get_by_id(
            self,
            db: Session,
            artist_id: int
    ) -> ArtistSchema:
        """
        Get Artist by Id

        :param db: The db Session
        :param artist_id: The Artist Id

        :return: Artist
        """

        artist: ArtistSchema = db.query(Artist).get(artist_id)
        if not artist:
            raise ArtistNotFoundError(artist_id)
        return artist
