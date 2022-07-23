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
from schemas.track import (
    TrackInfoSchema,
    TrackSchema
)
from exceptions.not_found import TrackNotFoundError

router = APIRouter(
    tags=["Song"],
)


@router.get(
    "/{track_id}",
    response_model=TrackSchema,
    status_code=status.HTTP_200_OK
)
# Depends Shortcut
# see: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#shortcut
def get_track_by_id(
    track_id: int,
    db: Session = Depends(get_db),
    track_repository: TrackRepository = Depends()
) -> TrackSchema:
    """
    Get Track

    :param track_id: Track ID
    :param db: Database Session
    :param track_repository: Track Repository

    :return: Track
    """
    try:
        track = track_repository.get_by_id(db, track_id)
    except TrackNotFoundError as e:
        raise exceptions.NotFoundError(e.detail)
    return track
