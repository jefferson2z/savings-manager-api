from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: str
    password_hash: str

    class Config:
        orm_mode = True


class UserOutput(UserBase):
    id: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
