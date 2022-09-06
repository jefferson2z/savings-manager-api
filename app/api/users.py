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
