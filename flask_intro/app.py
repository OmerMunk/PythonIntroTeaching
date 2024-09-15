# pip install Flask
# create a directory flask_intro
# create a file app.py
# pip install SQLAlchemy
# pip install -U Flask-SQLAlchemy

"""
create a full rest api backend for users.
you need to implement the following:
create user
get all users
get one user by id
get one user by name
update user
update all users
delete user
delete all users

bonus:
get average of all ages
count how many users
get the sum of all ages
get all the users that has a Gmail.
"""
from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError
from users.models import db
from users.routes import users_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init the database
db.init_app(app)

@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    return jsonify({'error': "Duplicate email or missing data"}), 400

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)

