from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app import crud, models
from app.config import CLIENT_URL
from app.db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    """Dependency for getting a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Portfolio(BaseModel):
    name: str


@app.get("/portfolios")
def list_portfolios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_portfolios = crud.list_portfolios(db, skip=skip, limit=limit)
    return {"portfolios": db_portfolios}


@app.post("/portfolios")
def create_portfolio(portfolio: Portfolio, db: Session = Depends(get_db)):
    db_portfolio = crud.create_portfolio(db, portfolio)
    return {"portfolio": db_portfolio}


@app.get("/portfolios/{portfolio_id}")
def get_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"portfolio": db_portfolio}


@app.put("/portfolios/{portfolio_id}")
def update_portfolio(
    portfolio_id: int, portfolio: Portfolio, db: Session = Depends(get_db)
):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.update_portfolio(
        db, db_portfolio=db_portfolio, portfolio_update=portfolio
    )
    return {"portfolio": db_portfolio}


@app.delete("/portfolios/{portfolio_id}")
def delete_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    db_portfolio = crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    db_portfolio = crud.delete_portfolio(db, portfolio_id=portfolio_id)
    return {"portfolio": db_portfolio}


@app.get("/")
def hello():
    return {"message": "savings manager api"}
