from http.client import HTTPException
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import crud, models
from app.database import SessionLocal, engine

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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


@app.get("/")
def hello():
    return {"message": "savings manager api"}
