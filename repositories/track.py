from typing import List
from sqlalchemy.orm import Session, joinedload
from models.track import Track
from models.album import Album
from exceptions.not_found import TrackNotFoundError
from schemas.track import TrackSchema


class TrackRepository:

    def get_all(
        self,
        db: Session
    ) -> List[TrackSchema]:
        artists_list: List[TrackSchema] = db.query(Track).all()
        return artists_list

    def get_by_id(
            self,
            db: Session,
            track_id: int
    ) -> TrackSchema:
        track: TrackSchema = db.query(Track)\
            .join(Track.Album)\
            .options(joinedload(Track.Album))\
            .join(Track.MediaType)\
            .options(joinedload(Track.MediaType))\
            .join(Track.Genre)\
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
