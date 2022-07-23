from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_db import Base
from controllers.artist_routes import router as artist_router


def get_application() -> FastAPI:
    """
    Returns a FastAPI application.

    :return: FastAPI application
    """

    # automap the database tables
    Base.prepare()

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
        prefix="/music-store/api/v1/artists",
    )

    return app


app = get_application()
