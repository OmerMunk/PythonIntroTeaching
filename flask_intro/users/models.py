from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class User(db.Model):
    # __tablename__ = 'my_app_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<User {self.name} {self.email}>'

    @validates('email')
    def validate_email(self, key, email):
        print(f"key is {key}")
        print(f"email is {email}")
        assert email.count('@') == 1, "Email must contain '@' character"
        return email