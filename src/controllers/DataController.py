import os
import uuid
import aiofiles
from fastapi import UploadFile, HTTPException, status
from .BaseController import BaseController
from src.models.response import ResponseModel

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        
    async def upload_data(self, file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="File type not allowed")
        
        if file.size > self.settings.FILE_MAX_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File size exceeds limit")

        # Generate auto-increment project ID and unique file name
        project_id = self.generate_project_id()
        unique_file_name = self.generate_unique_file_name(file.filename)
        
        file_path = self.get_file_path(project_id=project_id, file_name=unique_file_name)
        
        # Read and write the file in chunks using aiofiles
        chunk_size = self.settings.FILE_DEFAULT_CHUNK_SIZE
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(chunk_size):
                await f.write(chunk)

        return ResponseModel(
            success=True,
            message="File uploaded successfully",
            data={"project_id": project_id, "file_name": unique_file_name, "file_path": file_path}
        )

    def generate_unique_file_name(self, original_name: str) -> str:
        name, ext = os.path.splitext(original_name)
        unique_name = f"{name}_{uuid.uuid4().hex}{ext}"
        return unique_name