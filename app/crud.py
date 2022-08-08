from sqlalchemy.orm import Session

from app import models, schemas


def get_portfolio(db: Session, portfolio_id: int):
    return db.query(models.Portfolio).filter(models.Portfolio.id == portfolio_id).first()


def list_portfolios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Portfolio).offset(skip).limit(limit).all()


def create_portfolio(db: Session, portfolio: schemas.PortfolioCreate):
    db_portfolio = models.Portfolio(**portfolio.dict())
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio
