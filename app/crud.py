from sqlalchemy.orm import Session

from app import models, schemas


def get_portfolio(db: Session, portfolio_id: int):
    return (
        db.query(models.Portfolio).filter(models.Portfolio.id == portfolio_id).first()
    )


def list_portfolios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Portfolio).offset(skip).limit(limit).all()


def create_portfolio(db: Session, portfolio: schemas.PortfolioCreate):
    db_portfolio = models.Portfolio(**portfolio.dict())
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio


def delete_portfolio(db: Session, portfolio_id: int):
    db_portfolio = db.query(models.Portfolio).get(portfolio_id)
    db.delete(db_portfolio)
    db.commit()
    return db_portfolio


def update_portfolio(
    db: Session,
    db_portfolio: schemas.Portfolio,
    portfolio_update: schemas.PortfolioUpdate,
):
    portfolio_data = portfolio_update.dict(exclude_unset=True)
    for key, value in portfolio_data.items():
        setattr(db_portfolio, key, value)
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio
