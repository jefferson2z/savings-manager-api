from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import portfolio_schema, user_schema
from app.api import dependencies
from app.crud import portfolios_crud


router = APIRouter(
    prefix="/portfolios",
    tags=["portfolios"],
    dependencies=[Depends(dependencies.get_current_user)],
)


@router.get("/", response_model=list[portfolio_schema.Portfolio])
def list_portfolios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db),
    current_user: user_schema.User = Depends(dependencies.get_current_user),
):
    db_portfolios = portfolios_crud.list_portfolios(
        db,
        current_user.id,
        skip=skip,
        limit=limit,
    )
    return db_portfolios


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=portfolio_schema.Portfolio
)
def create_portfolio(
    portfolio: portfolio_schema.PortfolioCreate,
    db: Session = Depends(dependencies.get_db),
    current_user: user_schema.User = Depends(dependencies.get_current_user),
):
    db_portfolio = portfolios_crud.create_portfolio(db, portfolio, current_user.id)
    return db_portfolio


@router.get("/{portfolio_id}", response_model=portfolio_schema.Portfolio)
def get_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = portfolios_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio


@router.put("/{portfolio_id}")
def update_portfolio(
    portfolio_id: int,
    portfolio: portfolio_schema.PortfolioUpdate,
    db: Session = Depends(dependencies.get_db),
):
    db_portfolio = portfolios_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = portfolios_crud.update_portfolio(
        db, db_portfolio=db_portfolio, portfolio_update=portfolio
    )
    return {"portfolio": db_portfolio}


@router.delete("/{portfolio_id}")
def delete_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = portfolios_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = portfolios_crud.delete_portfolio(db, portfolio_id=portfolio_id)
    return {"portfolio": db_portfolio}
