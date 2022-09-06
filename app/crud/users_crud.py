from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import user_schema


def create_user(db: Session, user_create: user_schema.UserCreate):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
