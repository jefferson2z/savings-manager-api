from app.models.portfolio import Base

from alembic.config import Config
from alembic import command


def init_db(engine):
    Base.metadata.create_all(bind=engine)

    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")
