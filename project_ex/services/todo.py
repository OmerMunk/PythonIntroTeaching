from ..models.todo import Todo
from ..db import db


def create_todo(data: dict) -> dict:
    try:
        new_todo = Todo(
            task=data["task"],
            due_date=data["due_date"],
        )

        db.session.add(new_todo)
        db.session.commit()
        return new_todo.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

