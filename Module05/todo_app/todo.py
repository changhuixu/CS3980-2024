from fastapi import APIRouter

from model import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todos")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"msg": "new todo added"}


@todo_router.get("/todos")
async def get_todos() -> dict:
    return {"todos": todo_list}
