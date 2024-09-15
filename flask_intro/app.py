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
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# users: list = [
#     {
#         'id': 1,
#         'name': 'Omer',
#         'age': 29
#     },
#     {
#         'id': 2,
#         'name': 'Pahshish',
#         'age': 12
#     }
# ]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)


# init the database
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return 'Welcome to the best Kodcode API ever!! Shkoyech'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'name': user.name, 'email': user.email, 'age': user.age} for user in users]), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'name': user.name, 'email': user.email, 'age': user.age}), 200
    # filtered = list(filter(lambda user: user['id'] == id, ))
    # if (len(filtered) == 1):
    #     return jsonify(filtered[0]), 200
    # else: #len = 0
    #     return jsonify({"error": f"user with the id {id} not exist"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message': 'user created',
        'user': {
            'id': new_user.id,
            'name': new_user.name,
        }

    }), 201



if __name__ == '__main__':
    app.run(debug=True)

