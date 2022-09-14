from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import dependencies
from app.security import create_access_token
from app.crud import users_crud
from app.config import settings


router = APIRouter(tags=["login"])


@router.post("/token")
async def login_get_access_token(
    db: Session = Depends(dependencies.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    db_user = users_crud.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expires_delta = timedelta(minutes=int(settings.access_token_expire_minutes))
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=expires_delta
    )

    return {"access_token": access_token, "token_type": "bearer"}
