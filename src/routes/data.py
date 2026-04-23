import os
from fastapi import FastAPI,APIRouter,Depends,UploadFile,File
from src.helper.config import get_settings,Settings
from src.controllers import DataController


data_router = APIRouter(
    prefix="/v1/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)
@data_router.post("/upload")
async def read_data(file: UploadFile = File(...), data_controller: DataController = Depends()):
    return await data_controller.upload_data(file)



                        