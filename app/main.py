from fastapi import FastAPI

from app import models  # noqa: F401 — registra tabelas no metadata
from app.database import Base, engine
from app.routers import items

app = FastAPI(title="FastAPI Portfolio API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(items.router)
