from pydantic import BaseModel

from . import deposit_schema


class AssetBase(BaseModel):
    name: str


class AssetCreate(AssetBase):
    portfolio_id: int


class AssetUpdate(AssetBase):
    pass


class Asset(AssetBase):
    id: int
    portfolio_id: int

    deposits: list[deposit_schema.Deposit]

    class Config:
        orm_mode = True
