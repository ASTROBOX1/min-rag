from .BaseController import BaseController
from .DataController import DataController
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter



class ProcessController(BaseController):
    def __init__(self):
        super().__init__()

    def get_loader(self, project_id: str, file_id: str):
        project_path = os.path.join(self.files_dir, project_id)
        file_path = os.path.join(project_path, file_id)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_id} not found in {project_id}.")

        _, ext = os.path.splitext(file_id)
        ext = ext.lower()

        if ext == ".txt":
            return TextLoader(file_path, encoding="utf-8")
        elif ext in [".pdf"]:
            return PyMuPDFLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
    def get_content(self, project_id: str, file_id: str):
        loader = self.get_loader(project_id, file_id)
        return loader.load()  

    def split_content(self, file_content: list, chunk_size: int = 100, overlap: int = 20):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap, length_function=lambda x: len(x))
        content_text = [ 
            rec.page_content
            for rec in file_content 
        ]

        content_metadata = [
            rec.metadata
            for rec in file_content 
        ]

        chunks = text_splitter.create_documents(content_text, metadatas=content_metadata)
        return chunks
            
         
