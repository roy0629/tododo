from db_process import DB
from schemas import TodoRequest

async def db_create_todo(data: TodoRequest) -> dict:
    with DB() as db:
        db.cursor.execute(
            """
            INSERT INTO
                todos
                (title, description)
            VALUES
                (%s, %s)
            RETURNING *
            """,
            (data.title, data.description)
            )
        return dict(db.cursor.fetchone())
