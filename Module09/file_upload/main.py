import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.post("/upload")
def upload_file(uploaded_file: UploadFile = File(...)):
    path = f"files/{uploaded_file.filename}"
    with open(path, "w+b") as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return {
        "file": uploaded_file.filename,
        "content": uploaded_file.content_type,
        "path": path,
    }


app.mount("/files", StaticFiles(directory="files"), "files")
