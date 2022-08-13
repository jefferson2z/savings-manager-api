from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

db_uri = os.getenv("DATABASE_URI")

# TODO - remove connect_args after moving to postgreSQL
engine = create_engine(db_uri, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
