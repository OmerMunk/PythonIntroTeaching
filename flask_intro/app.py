# pip install Flask
# create a directory flask_intro
# create a file app.py

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

