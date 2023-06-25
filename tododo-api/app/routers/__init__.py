from routers.todo import router as todo_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(todo_router, prefix="/todo", tags=["todo"])
