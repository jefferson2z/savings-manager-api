from pydantic import BaseModel


class AssetBase(BaseModel):
    name: str


class AssetCreate(AssetBase):
    portfolio_id: int


class AssetUpdate(AssetBase):
    pass


class Asset(AssetBase):
    id: int
    portfolio_id: int

    class Config:
        orm_mode = True
