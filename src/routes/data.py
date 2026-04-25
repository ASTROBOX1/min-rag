import os
from fastapi import FastAPI,APIRouter,Depends,UploadFile,File,HTTPException
from src.helper.config import get_settings,Settings
from src.controllers import DataController, ProcessController
from .schemes.data import ProcessRequest




data_router = APIRouter(
    prefix="/v1/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)

def get_data_controller() -> DataController:
    return DataController()

def get_process_controller() -> ProcessController:
    return ProcessController()

@data_router.post("/upload")
async def read_data(file: UploadFile = File(...), data_controller: DataController = Depends(get_data_controller)):
    return await data_controller.upload_data(file)

@data_router.post("/process/{project_id}")
async def process_data(project_id: str, request: ProcessRequest, process_controller: ProcessController = Depends(get_process_controller)):
    file_id = request.file_id 
    chunk_size = request.chunk_size
    overlap = request.overlap

    try:
        file_content = process_controller.get_content(project_id, file_id)
        file_chunks = process_controller.split_content(file_content, chunk_size, overlap)

        if not file_chunks:
            return {"message": "No content to process"}
            
        return {"message": "Processed successfully", "chunks_count": len(file_chunks), "chunks": file_chunks} 
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    