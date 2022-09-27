from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class DepositBase(BaseModel):
    amount: Optional[Decimal]
    date: Optional[date]
    description: Optional[str]


class DepositCreate(DepositBase):
    amount: Decimal
    date: date
    description: str
    asset_id: int


class DepositUpdate(DepositBase):
    pass


class Deposit(DepositBase):
    id: int
    asset_id: int

    amount: Decimal
    date: date
    description: str

    class Config:
        orm_mode = True
