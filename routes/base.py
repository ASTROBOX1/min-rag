from fastapi import FastAPI,APIRouter
router = APIRouter()
@router.get("/")
def read_root():
    return {"Hello": "all"}

