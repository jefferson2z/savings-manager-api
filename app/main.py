from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app import models
from app.api import portfolios
from app.config import CLIENT_URL
from app.db.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(portfolios.router)


@app.get("/")
def hello():
    return {"message": "savings manager api"}
