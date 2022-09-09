from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.schemas import user_schema
from app.api import dependencies
from app.crud import users_crud


router = APIRouter(prefix="/users")


@router.get("/me", response_model=user_schema.UserOutput)
async def read_user_me(current_user: user_schema.User = Depends(get_current_user)):
    return current_user


@router.post(
    "/", response_model=user_schema.UserOutput, status_code=status.HTTP_201_CREATED
)
def create_user(
    user: user_schema.UserCreate,
    db: Session = Depends(dependencies.get_db),
):
    db_user = users_crud.create_user(db, user)
    return db_user


@router.get("/{user_id}", response_model=user_schema.UserOutput)
def get_user(
    user_id: int,
    db: Session = Depends(dependencies.get_db),
):
    db_user = users_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}")
def delete_portfolio(user_id: int, db: Session = Depends(dependencies.get_db)):
    db_user = users_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user = users_crud.delete_user(db, user_id=user_id)
    return {"user": db_user}
