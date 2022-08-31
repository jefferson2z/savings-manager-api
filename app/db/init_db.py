from app.models.portfolio import Base
from app.db.database import engine


from alembic.config import Config
from alembic import command


def init_db():
    Base.metadata.create_all(bind=engine)

    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")
