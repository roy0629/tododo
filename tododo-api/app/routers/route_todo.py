import traceback
from typing import List

from fastapi import APIRouter, Response, Request, HTTPException
# from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from schemas import TodoRequest, TodoResponse
from database import db_create_todo, db_get_todos, db_get_single_todo


router = APIRouter()


@router.post("/api/todo", response_model=TodoResponse)
async def create_todo(response: Response, data: TodoRequest):
    try:
        # todo = jsonable_encoder(data)
        res = await db_create_todo(data)
        response.status_code = HTTP_201_CREATED
        if res:
            return res
        raise HTTPException(status_code=404, detail="Create task failed")
    except Exception:
        traceback.print_exc()


@router.get("/api/todo", response_model=List[TodoResponse])
async def get_todos():
    res = await db_get_todos()
    return res


@router.get("/api/todo/{id}", response_model=TodoResponse)
async def get_single_todo(id: str):
    try:
        res = await db_get_single_todo(id)
        if res:
            return res
        raise HTTPException(status_code=404, detail=f"Task of ID:{id} doesn't exist")
    except Exception:
        traceback.print_exc()
