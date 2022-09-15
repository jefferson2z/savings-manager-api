from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

from app.api import portfolios, login, users, assets


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.client_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(portfolios.router)
app.include_router(users.router)
app.include_router(assets.router)


@app.get("/")
def hello():
    return {"message": "savings manager api"}
