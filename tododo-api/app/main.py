import os

from fastapi import FastAPI

from db_process import DB
from routers import route_todo
from schemas import SuccessMsg


DATABASE_URL = os.environ["DATABASE_URL"]

app = FastAPI()
app.include_router(route_todo.router)


@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "tododo api running !"}


@app.get("/db-access")
def db_access_check():
    with DB() as db:
        db.cursor.execute("select * from pg_settings")
        db_setting_info = db.cursor.fetchall()
        dict_result = []
        for row in db_setting_info:
            dict_result.append(dict(row))
    return dict_result
