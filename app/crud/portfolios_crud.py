from sqlalchemy.orm import Session

from app import models
from app.crud.base_crud import BaseCRUD
from app.schemas import portfolio_schema


class PortfoliosCRUD(BaseCRUD):
    def create_with_user(
        self,
        db: Session,
        portfolio_create: portfolio_schema.PortfolioCreate,
        *,
        user_id: int
    ):
        db_portfolio = self.model(**portfolio_create.dict(), user_id=user_id)
        db.add(db_portfolio)
        db.commit()
        db.refresh(db_portfolio)
        return db_portfolio

    def list_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ):
        db_portfolio_list = (
            db.query(self.model)
            .where(self.model.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return db_portfolio_list


portfolio = PortfoliosCRUD(models.Portfolio)


def delete_portfolio(db: Session, portfolio_id: int):
    db_portfolio = db.query(models.Portfolio).get(portfolio_id)
    db.delete(db_portfolio)
    db.commit()
    return db_portfolio


def update_portfolio(
    db: Session,
    db_portfolio: portfolio_schema.Portfolio,
    portfolio_update: portfolio_schema.PortfolioUpdate,
):
    portfolio_data = portfolio_update.dict(exclude_unset=True)
    for key, value in portfolio_data.items():
        setattr(db_portfolio, key, value)
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio
