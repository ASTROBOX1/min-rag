from fastapi import FastAPI
from routes.base import router as base_router
from dotenv import load_dotenv
import os

load_dotenv(".env")
app = FastAPI()
app.include_router(base_router)
