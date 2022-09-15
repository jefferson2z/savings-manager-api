from pydantic import BaseModel

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

    assets: list[asset_schema.Asset]

    class Config:
        orm_mode = True
