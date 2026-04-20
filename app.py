from fastapi import FastAPI
app = FastAPI()
@app.get("/Hello")
def read_root():
    return {"Hello": "World"}
