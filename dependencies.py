from typing import Generator
from sqlalchemy.orm import sessionmaker
from config_db import SessionLocal


def get_db() -> Generator[sessionmaker, None, None]:
    """
    Get Database Session

    :return: Database Session
    """

    session: sessionmaker = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
