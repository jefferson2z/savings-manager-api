from sqlalchemy.orm import Session

from app.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas import user_schema


def create_user(db: Session, user_create: user_schema.UserCreate):
    user_json = user_create.dict()
    db_user = User(
        username=user_json.get("username"),
        password_hash=get_password_hash(user_json.get("password")),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user


def authenticate(db: Session, username: str, password: str):
    db_user = get_user_by_username(db, username)
    if not db_user:
        return False
    if not verify_password(password, db_user.password_hash):
        return False
    return db_user
