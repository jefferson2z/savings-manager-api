from pydantic import BaseModel

from app.schemas import portfolio_schema


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: str
    password_hash: str

    class Config:
        orm_mode = True


class UserOutput(UserBase):
    id: str
    portfolios: list[portfolio_schema.Portfolio]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
