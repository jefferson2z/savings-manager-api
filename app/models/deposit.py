from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Date, DECIMAL
from sqlalchemy.orm import relationship

from app.db.declarative_base import Base


class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL(19, 4), index=True, nullable=False)
    date = Column(Date, index=True, nullable=False)
    description = Column(String, nullable=True)

    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    asset = relationship("Asset", back_populates="deposits")

    def __repr__(self):
        return f"Deposit(id={self.id}, asset_id={self.asset_id})"
