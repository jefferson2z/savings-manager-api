from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.schemas import user_schema
from app.api import dependencies
from app.crud import users_crud


router = APIRouter(prefix="/users")


@router.post("/", response_model=user_schema.User)
def create_user(
    user: user_schema.UserCreate,
    db: Session = Depends(dependencies.get_db),
):
    db_user = users_crud.create_user(db, user)
    return db_user


@router.get("/{user_id}", response_model=user_schema.User)
def get_user(
    user_id: int,
    db: Session = Depends(dependencies.get_db),
):
    db_user = users_crud.get_user(db, user_id=user_id)
    return db_user
