import os

import psycopg2
from psycopg2.extras import DictCursor
from fastapi import FastAPI

from db_process import DB


app = FastAPI()
DATABASE_URL = os.environ["DATABASE_URL"]


@app.get("/")
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
