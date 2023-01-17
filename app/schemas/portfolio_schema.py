from pydantic import BaseModel
from typing import Optional

from . import asset_schema


class PortfolioBase(BaseModel):
    name: str


class PortfolioCreate(PortfolioBase):
    pass


class PortfolioUpdate(PortfolioBase):
    pass


class Portfolio(PortfolioBase):
    id: int
    user_id: int

    assets: Optional[list[asset_schema.Asset]]

    class Config:
        orm_mode = True
