from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model import Todo, TodoRequest

todo_router = APIRouter()

todo_list: list[Todo] = []


@todo_router.post(
    "/todos",
    status_code=status.HTTP_201_CREATED,
)
async def add_todo(todo: TodoRequest) -> Todo:
    if len(todo_list) == 0:
        id = 1
    else:
        id = max(todo_list, key=lambda x: x.id).id + 1

    new_todo = Todo(id=id, title=todo.title, description=todo.description)

    todo_list.append(new_todo)
    json_obj = new_todo.model_dump()
    return JSONResponse(json_obj, status_code=status.HTTP_201_CREATED)


@todo_router.get("/todos")
async def get_todos() -> dict:
    json = jsonable_encoder(todo_list)
    return JSONResponse(json)
    # return {"todos": todo_list}


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


@todo_router.put("/todos/{id}")
async def update_todo(id: int, todo: TodoRequest) -> dict:
    for x in todo_list:
        if x.id == id:
            x.title = todo.title
            x.description = todo.description
            return {"msg": "Todo update successfully"}

    return {"msg": f"The todo with ID={id} is not found."}


@todo_router.delete("/todos/{id}")
async def delete_todo(id: int) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == id:
            todo_list.pop(i)
            return {"msg": f"The todo with ID={id} is deleted."}

    return {"msg": f"The todo with ID={id} is not found."}
