from fastapi import FastAPI,APIRouter
from dotenv import load_dotenv
import os
load_dotenv(".env")

router = APIRouter(
    prefix="/base",
    tags=["base"],
    responses={404: {"description": "Not found"}},

)
@router.get("/")

async def read_root():
    app_name = os.getenv("APP_NAME", "Unknown App")
    return {"Hello": "all", "app_name": app_name}

