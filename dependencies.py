from typing import Generator
from sqlalchemy.orm import sessionmaker
from config_db import SessionLocal
from repositories.artist_repository import ArtistRepo


def get_artist_repo():
    return ArtistRepo()

def get_db() -> Generator[sessionmaker, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
