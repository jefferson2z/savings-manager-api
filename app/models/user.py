from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.declarative_base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    portfolios = relationship(
        "Portfolio", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"
