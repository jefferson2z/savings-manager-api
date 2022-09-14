from sqlalchemy import Column, Integer, String
from app.db.declarative_base import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
