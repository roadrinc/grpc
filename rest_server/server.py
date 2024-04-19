from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path

app = FastAPI()


@app.get("/")
def read_root():
    # Access the environment variable
    return {"Hello": "api-server"}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open("uploaded_file.txt", "wb") as f:
        while chunk := await file.read(1024):
            f.write(chunk)
    return {"success": True}


@app.post("/send_text")
async def send_text(text: str):
    print(text)
    return {"success": True}
