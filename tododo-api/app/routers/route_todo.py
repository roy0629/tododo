import traceback
from typing import List

from fastapi import APIRouter, Response, Request, HTTPException
# from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from schemas import TodoRequest, TodoResponse, SuccessMsg
from database import db_create_todo, db_get_todos, db_get_single_todo, db_update_todo, db_delete_todo


router = APIRouter(prefix="/api/todo", tags=["todo"])


@router.post("", response_model=TodoResponse)
async def create_todo(response: Response, data: TodoRequest):
    try:
        # todo = jsonable_encoder(data) psycopg2でのやり取りではdictで良いから
        res = await db_create_todo(data)
        response.status_code = HTTP_201_CREATED
        if res:
            return res
        raise HTTPException(status_code=404, detail="Create task failed")
    except Exception:
        traceback.print_exc()


@router.get("", response_model=List[TodoResponse])
async def get_todos():
    res = await db_get_todos()
    return res


@router.get("/{id}", response_model=TodoResponse)
async def get_single_todo(id: str):
    try:
        res = await db_get_single_todo(id)
        if res:
            return res
        raise HTTPException(status_code=404, detail=f"Task of ID:{id} doesn't exist")
    except Exception:
        traceback.print_exc()


@router.put("/{id}", response_model=TodoResponse)
async def update_todo(id: str, data: TodoRequest):
    try:
        res = await db_update_todo(id, data)
        if res:
            return res
        raise HTTPException(status_code=404, detail=f"Update task failed")
    except Exception:
        traceback.print_exc()


@router.delete("/{id}", response_model=SuccessMsg)
async def delete_todo(id: str):
    try:
        res = await db_delete_todo(id)
        if res:
            return {"message": "Successfully deleted"}
        raise HTTPException(status_code=404, detail=f"Delete task failed")
    except Exception:
        traceback.print_exc()
