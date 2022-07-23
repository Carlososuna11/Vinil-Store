from typing import List
from fastapi import (
    APIRouter,
    Depends,
    status,
    exceptions
)
from sqlalchemy.orm import Session

from dependencies import get_db
from repositories.track import TrackRepository
from repositories.album import AlbumRepository
from schemas.track import (
    TrackInfoSchema,
    TrackSchema
)
from exceptions.not_found import AlbumNotFoundError

router = APIRouter(
    tags=["Albums"],
)


@router.get(
    "/{album_id}",
    response_model=List[TrackInfoSchema],
    status_code=status.HTTP_200_OK
)
# Depends Shortcut
# see: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#shortcut
def get_tracks_by_album(
    album_id: int,
    db: Session = Depends(get_db),
    album_repository: AlbumRepository = Depends(),
    track_repository: TrackRepository = Depends()
) -> List[TrackSchema]:
    """
    Get All Tracks by Album

    :param album_id: Album ID
    :param db: Database Session
    :param album_repository: Album Repository
    :param track_repository: Track Repository

    :return: List of tracks
    """
    try:
        album_repository.get_by_id(db, album_id)
    except AlbumNotFoundError:
        raise exceptions.NotFoundError(detail="Album not found")

    return track_repository.get_by_album_id(db, album_id)
