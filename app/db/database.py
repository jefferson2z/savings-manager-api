from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings


database_url = settings.get_database_url()
if database_url.startswith("sqlite"):

    engine = create_engine(database_url, connect_args={"check_same_thread": False})
else:
    engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
