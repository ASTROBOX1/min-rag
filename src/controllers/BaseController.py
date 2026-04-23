from src.helper.config import get_settings
import os,random,string

class BaseController:
    def __init__(self):
        self.settings = get_settings()
        self.base_dir = self.settings.BASE_DIR
        self.files_dir = os.path.join(self.base_dir, "assets", "files")
        os.makedirs(self.files_dir, exist_ok=True)

    def generate_project_id(self) -> str:
        existing_ids = []
        for item in os.listdir(self.files_dir):
            item_path = os.path.join(self.files_dir, item)
            if os.path.isdir(item_path) and item.startswith("project_"):
                try:
                    num = int(item.split("_")[1])
                    existing_ids.append(num)
                except ValueError:
                    pass
        
        next_id = max(existing_ids) + 1 if existing_ids else 1
        return f"project_{next_id}"

    def get_file_path(self, project_id: str, file_name: str) -> str:
        project_dir = os.path.join(self.files_dir, project_id)
        os.makedirs(project_dir, exist_ok=True)
        return os.path.join(project_dir, file_name)

    def save_file(self, project_id: str, file_name: str, file_content: bytes) -> str:
        file_path = self.get_file_path(project_id, file_name)
        with open(file_path, "wb") as f:
            f.write(file_content)
        return file_path
    