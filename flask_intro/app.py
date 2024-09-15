# pip install Flask
# create a directory flask_intro
# create a file app.py

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


users = []

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the best Kodcode API ever!! Shkoyech'

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201



if __name__ == '__main__':
    app.run(debug=True)

