import os

from fastapi import FastAPI

from database.db_process import DB
from routers import router as api_router
from schemas.common import SuccessMsg


DATABASE_URL = os.environ["DATABASE_URL"]

app = FastAPI()
app.include_router(api_router, prefix="/api")


@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "tododo api running !"}


@app.get("/db-access-check")
def db_connection_confirmation():
    with DB() as db:
        db.cursor.execute("select * from pg_settings")
        db_setting_info = db.cursor.fetchall()
        dict_result = []
        for row in db_setting_info:
            dict_result.append(dict(row))
    return dict_result
