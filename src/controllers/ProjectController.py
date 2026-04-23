from src.controllers.BaseController import BaseController
import os
import uuid

from fastapi import UploadFile
from src.models.response import ResponseModel

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    async def create_project_dir(self, project_id: str) -> ResponseModel:
        project_path = os.path.join(self.files_dir, project_id)
        if os.path.exists(project_path):
            return ResponseModel(success=True, message="Project directory already exists", data={"project_path": project_path})
        else:
            os.makedirs(project_path, exist_ok=True)
            return ResponseModel(success=True, message="Project directory created successfully", data={"project_path": project_path})
        