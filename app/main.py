from fastapi import FastAPI
from .routes import router
from app.database import engine
from app import models


app=FastAPI()
app.include_router(router)
models.Base.metadata.create_all(bind=engine)

