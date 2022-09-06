from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import user_schema


def create_user(db: Session, user_create: user_schema.UserCreate):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user
