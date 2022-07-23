from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from dependencies import get_artist_repo, get_db
from repositories.artist_repository import ArtistRepo
from schemas.artist_schemas import Artist

router = APIRouter(
    tags=["Singers"],
)


@router.get("/", response_model=List[Artist], status_code=status.HTTP_200_OK)
def get_all_artists(
    db: Session = Depends(get_db),
    artist_repo: ArtistRepo = Depends(get_artist_repo)
) -> List[Artist]:
    return artist_repo.get_all_artists(db=db)
