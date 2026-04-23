import os

from fastapi import FastAPI,APIRouter,Depends
from src.helper.config import get_settings,Settings
settings = get_settings()

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},

)
@router.get("/")

async def read_root():
    app_name = settings.APP_NAME
    app_version = settings.VERSION
    return {"app_name": app_name, "app_version": app_version}

