from database.db_process import DB
from schemas.todo import TodoRequest


async def db_create_todo(data: TodoRequest) -> dict:
    with DB() as db:
        db.cursor.execute(
            """
            INSERT INTO
                todos
                (title, description)
            VALUES
                (%s, %s)
            RETURNING
                *
            """,
            (data.title, data.description)
            )
        return dict(db.cursor.fetchone())


async def db_get_todos() -> list:
    with DB() as db:
        db.cursor.execute(
            """
            SELECT
                id, title, description
            FROM
                todos
            """
            )
        return [dict(todo) for todo in db.cursor.fetchall()]


async def db_get_single_todo(TodoRequestId: str) -> dict | bool:
    with DB() as db:
        db.cursor.execute(
            """
            SELECT
                id, title, description
            FROM
                todos
            WHERE
                id = %s
            """,
            (TodoRequestId,)
            )
        if db.cursor.rowcount:
            return dict(db.cursor.fetchone())
        return False


async def db_update_todo(TodoRequestId: str, data: TodoRequest) -> dict | bool:
    with DB() as db:
        db.cursor.execute(
            """
            UPDATE
                todos
            SET
                title=%s, description=%s
            WHERE
                id = %s
            RETURNING
                *
            """,
            (data.title, data.description, TodoRequestId)
            )
        if db.cursor.rowcount:
            return dict(db.cursor.fetchone())
        return False


async def db_delete_todo(TodoRequestId: str) -> bool:
    with DB() as db:
        db.cursor.execute(
            """
            DELETE
            FROM
                todos
            WHERE
                id = %s
            """,
            (TodoRequestId,)
            )
        if db.cursor.rowcount:
            return True
        else:
            return False
