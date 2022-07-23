from sqlalchemy import (
    create_engine,
    MetaData,
)
from sqlalchemy.ext.automap import automap_base
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


# produce our own MetaData object
metadata = MetaData()
 
# reflect the tables
metadata.reflect(engine)

# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)
