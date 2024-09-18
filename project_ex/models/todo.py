from ..db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task =db.Column(db.String(64), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'due_date': self.due_date,
        }
