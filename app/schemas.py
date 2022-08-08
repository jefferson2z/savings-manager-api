from pydantic import BaseModel


class PortfolioBase(BaseModel):
    name: str


class PortfolioCreate(PortfolioBase):
    pass


class Portfolio(PortfolioBase):
    id: int

    class Config:
        orm_mode = True
