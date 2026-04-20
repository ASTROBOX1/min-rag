from fastapi import FastAPI
from src.routes.base import router as base_router

app = FastAPI()

app.include_router(base_router)
