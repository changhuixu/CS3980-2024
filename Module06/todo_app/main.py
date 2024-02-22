from enum import Enum
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from todo import todo_router

app = FastAPI()


# @app.get("/")
# async def welcome() -> dict:
#     return {"mgs": "hello"}


@app.get("/")
async def view_index():
    return FileResponse("./frontend/index.html")


app.include_router(todo_router, tags=["Todo"])

app.mount("/", StaticFiles(directory="frontend"), name="static")
