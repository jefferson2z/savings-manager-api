from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

portfolios: list = []


class Portfolio(BaseModel):
    name: str


@app.get("/portfolios")
def list_portfolios():
    return {"portfolios": portfolios}


@app.post("/portfolios")
def create_portfolio(portfolio: Portfolio):
    portfolios.append(portfolio)
    return {"portfolios": portfolios}


@app.get("/")
def hello():
    return {"message": "savings manager api"}
