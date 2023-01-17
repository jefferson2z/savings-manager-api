from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.config import settings
from app.db.database import SessionLocal
from app.schemas.login_schema import TokenData
from app.crud import users_crud
from app.cache.cache import Cache

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    """Dependency for getting a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_cache():
    """Dependency for getting cache"""
    cache = Cache()
    return cache


async def get_current_user(db=Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.jwt_algorithm]
        )
        username: str = str(payload.get("sub"))
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    username = str(token_data.username)
    user = users_crud.get_user_by_username(db, username)
    if not user:
        return credentials_exception
    return user
