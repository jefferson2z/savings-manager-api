from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import dependencies


router = APIRouter()


@router.get("/portfolios")
def list_portfolios(
    skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)
):
    db_portfolios = crud.list_portfolios(db, skip=skip, limit=limit)
    return {"portfolios": db_portfolios}


@router.post("/portfolios")
def create_portfolio(
    portfolio: schemas.PortfolioCreate, db: Session = Depends(dependencies.get_db)
):
    db_portfolio = crud.create_portfolio(db, portfolio)
    return {"portfolio": db_portfolio}


@router.get("/portfolios/{portfolio_id}")
def get_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"portfolio": db_portfolio}


@router.put("/portfolios/{portfolio_id}")
def update_portfolio(
    portfolio_id: int,
    portfolio: schemas.PortfolioUpdate,
    db: Session = Depends(dependencies.get_db),
):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.update_portfolio(
        db, db_portfolio=db_portfolio, portfolio_update=portfolio
    )
    return {"portfolio": db_portfolio}


@router.delete("/portfolios/{portfolio_id}")
def delete_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.delete_portfolio(db, portfolio_id=portfolio_id)
    return {"portfolio": db_portfolio}
