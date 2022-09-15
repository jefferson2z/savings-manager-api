from pydantic import BaseModel


class AssetBase(BaseModel):
    name: str


class AssetCreate(AssetBase):
    portfolio_id: int


class Asset(AssetBase):
    id: int

    class Config:
        orm_mode = True
