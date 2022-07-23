from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set the database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///chinook.db"

# create a database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

# create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create a object of declarative base
Base = declarative_base()
