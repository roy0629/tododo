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
    # conn = psycopg2.connect(DATABASE_URL)
    # cur = conn.cursor(cursor_factory=DictCursor)
    # cur.execute("select * from pg_settings")
    # db_setting_info = cur.fetchall()
    # dict_result = []
    # for row in db_setting_info:
    #     dict_result.append(dict(row))
    # cur.close()
    # conn.close()
    # return dict_result
    with DB() as db:
        db.cursor.execute("select * from pg_settings")
        db_setting_info = db.cursor.fetchall()
        dict_result = []
        for row in db_setting_info:
            dict_result.append(dict(row))
    return dict_result
