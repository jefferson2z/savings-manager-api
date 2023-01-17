from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.schemas import portfolio_schema, user_schema
from app.api import dependencies

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
    cache=Depends(dependencies.get_cache),
    current_user: user_schema.User = Depends(dependencies.get_current_user),
):
    cache_key = f"portfolios_{current_user.id}"
    portfolios = cache.get_or_set(
        cache_key,
        lambda: crud.portfolio.list_by_user(
            db,
            user_id=current_user.id,
            skip=skip,
            limit=limit,
        ),
    )

    return portfolios


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=portfolio_schema.Portfolio
)
def create_portfolio(
    portfolio: portfolio_schema.PortfolioCreate,
    db: Session = Depends(dependencies.get_db),
    current_user: user_schema.User = Depends(dependencies.get_current_user),
):
    db_portfolio = crud.portfolio.create_with_user(
        db, portfolio, user_id=current_user.id
    )
    return db_portfolio


@router.get("/{portfolio_id}", response_model=portfolio_schema.Portfolio)
def get_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = crud.portfolio.get(db, id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio


@router.put("/{portfolio_id}", response_model=portfolio_schema.Portfolio)
def update_portfolio(
    portfolio_id: int,
    portfolio: portfolio_schema.PortfolioUpdate,
    db: Session = Depends(dependencies.get_db),
):
    db_portfolio = crud.portfolio.get(db, id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.portfolio.update(
        db, db_item=db_portfolio, item_update=portfolio
    )
    return db_portfolio


@router.delete("/{portfolio_id}", response_model=portfolio_schema.Portfolio)
def delete_portfolio(portfolio_id: int, db: Session = Depends(dependencies.get_db)):
    db_portfolio = crud.portfolio.get(db, id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.portfolio.delete(db, id=portfolio_id)
    return db_portfolio
