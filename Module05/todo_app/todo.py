from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from fastapi.responses import JSONResponse

from model import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post(
    "/todos",
    status_code=status.HTTP_201_CREATED,
)
async def add_todo(todo: Todo) -> Todo:
    todo_list.append(todo)
    json_obj = todo.model_dump()
    return JSONResponse(json_obj, status_code=status.HTTP_201_CREATED)


@todo_router.get("/todos")
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todos/{id}")
async def get_todo_by_id(
    id: Annotated[int, Path(title="The ID  to get", ge=0, le=1000)]
) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo": todo}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The todo with ID={id} is not found",
    )
