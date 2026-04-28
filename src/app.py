from fastapi import FastAPI
from src.routes.base import router as base_router
from src.routes.data import data_router
from motor.motor_asyncio import AsyncIOMotorClient
from src.helper.config import get_settings


app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)
    app.mongodb = app.mongodb_client[settings.MONGODB_DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

    
app.include_router(base_router)
app.include_router(data_router)
