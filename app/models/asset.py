from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.declarative_base import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    portfolio_id = Column(Integer, ForeignKey("portfolios.id"), nullable=False)
    portfolio = relationship("Portfolio", back_populates="assets")

    def __repr__(self):
        return (
            f"Asset(id={self.id}, name={self.name}, portfolio_id={self.portfolio_id})"
        )
