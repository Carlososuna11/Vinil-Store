from typing import List
from sqlalchemy.orm import Session, joinedload
from models.track import Track
from models.album import Album
from exceptions.not_found import TrackNotFoundError
from schemas.track import TrackSchema


class TrackRepository:
    """
    The Track Repository Class. It contains all methods
    for the db context use.
    """

    def get_all(
        self,
        db: Session
    ) -> List[TrackSchema]:
        """
        Get All Tracks

        :param db: The db Session

        :return: List of Tracks
        """
        tracks_list: List[TrackSchema] = db.query(Track).all()
        return tracks_list

    def get_by_id(
            self,
            db: Session,
            track_id: int
    ) -> TrackSchema:
        """
        Get Track by Id

        :param db: The db Session
        :param track_id: The Track Id

        :return: Track
        """
        # join the album, media_type, and genre tables
        track: TrackSchema = db.query(Track)\
            .join(Track.Album, isouter=True)\
            .options(joinedload(Track.Album))\
            .join(Track.MediaType, isouter=True)\
            .options(joinedload(Track.MediaType))\
            .join(Track.Genre, isouter=True)\
            .options(joinedload(Track.Genre))\
            .filter(Track.TrackId == track_id)\
            .first()
        if not track:
            raise TrackNotFoundError(track_id)
        return track

    def get_by_album_id(
            self,
            db: Session,
            album_id: int
    ) -> List[TrackSchema]:
        """
        Get Tracks by Album Id

        :param db: The db Session
        :param album_id: The Album Id

        :return: List of Tracks
        """
        tracks_list: List[TrackSchema] = db.query(
            Track
        ).filter(
            Track.AlbumId == album_id
        ).all()
        return tracks_list

    def get_by_artist_id(
            self,
            db: Session,
            artist_id: int
    ) -> List[TrackSchema]:
        """
        Get Track by Artist Id

        :param db: The db Session
        :param artist_id: The Artist Id

        :return: List of Tracks
        """
        # join the album table
        tracks_list: List[TrackSchema] = db.query(
            Track
        ).join(
            Track.Album
        ).options(
            joinedload(Track.Album)
        ).filter(
            Album.ArtistId == artist_id
        ).all()

        return tracks_list
