from enum import Enum
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"mgs": "hello"}


class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


app.include_router(todo_router, tags=["Todo"])


class Day(int, Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


@app.get("/days/{day}")
async def get_model(day: Day):
    return {"day": day}
