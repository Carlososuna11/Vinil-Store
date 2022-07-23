from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_db import (
    Base,
    engine
)
from controllers.artist import router as artist_router
from controllers.album import router as album_router
from controllers.track import router as track_router


def get_application() -> FastAPI:
    """
    Returns a FastAPI application.

    :return: FastAPI application
    """

    # automap the database tables
    Base.metadata.create_all(bind=engine)

    # create a FastAPI application
    app = FastAPI(
        title="FastAPI - Vinyl Store",
        description="Proyecto desarrollado por Carlos Osuna"
        " para la materia de Python como parte de entrega de"
        " parte Práctica del Parcial II",
        version="0.1.0",
        openapi_url="/api/openapi.json",
        docs_url="/docs/",
        redoc_url="/redoc/",
    )

    # add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add the artist routes
    app.include_router(
        artist_router,
        prefix="/music-store/api/v1",
    )

    # add the album routes
    app.include_router(
        album_router,
        prefix="/music-store/api/v1/albums",
    )

    # add the track routes
    app.include_router(
        track_router,
        prefix="/music-store/api/v1/song",
    )

    return app


app = get_application()
