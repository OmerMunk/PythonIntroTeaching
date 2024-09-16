# Topic Recap: Flask with SQLAlchemy (Data Engineering Oriented)

# SQLAlchemy is a popular SQL toolkit and Object Relational Mapping (ORM) system for Python.
# It provides a powerful and flexible way to work with relational databases in Python applications, such as Flask.

# In this session, we will create a simple Flask application that uses SQLAlchemy to perform CRUD operations on a database.

# Step-by-Step Guide for Building a Flask Application with SQLAlchemy

# Step 1: Set Up Flask and SQLAlchemy
# Install Flask and SQLAlchemy using pip if not already installed:
# pip install flask flask-sqlalchemy

# Create a file named `app.py` and import Flask, SQLAlchemy, and other necessary modules.

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Step 2: Define the Database Model
# Create a model class `User` that represents the user table in the database.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "role": self.role}

# Step 3: Create the Database
# Run the following code once to create the database and tables.

@app.before_first_request
def create_tables():
    db.create_all()

# Step 4: Define Routes for CRUD Operations

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Route: Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict())

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json or 'role' not in request.json:
        abort(400, description="Bad request")
    new_user = User(name=request.json['name'], role=request.json['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# Route: Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    if not request.json:
        abort(400, description="Bad request")
    user.name = request.json.get('name', user.name)
    user.role = request.json.get('role', user.role)
    db.session.commit()
    return jsonify(user.to_dict())

# Route: Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

# Step 5: Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)

# To run the Flask app, execute `python app.py` in your terminal.
# Access the application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

# Explanation:
# 1. `get_users`: Fetches all users from the database.
# 2. `get_user`: Fetches a specific user based on the provided user ID.
# 3. `create_user`: Adds a new user to the database.
# 4. `update_user`: Updates the details of an existing user.
# 5. `delete_user`: Removes a user from the database.

# 3 Easy Exercises

# Exercise 1 (Easy): Create a New Route to Retrieve Users by Role
# Explanation: Write a Flask route `/users/role/<role>` that fetches all users with the specified role from the database.
# Solution:


# Example Input:
# Send a GET request to `/users/role/Data Engineer`.

# Example Output:
# [{"id": 1, "name": "Alice", "role": "Data Engineer"}]


# Exercise 2 (Easy): Create a Route to Count Users in the Database
# Explanation: Write a Flask route `/users/count` that returns the total count of users in the database.
# Solution:


# Example Input:
# Send a GET request to `/users/count`.

# Example Output:
# {"count": 2}


# Exercise 3 (Easy): Create a Route to Check If a User Exists
# Explanation: Write a Flask route `/users/exists/<name>` that checks if a user with the given name exists in the database.
# Solution:


# Example Input:
# Send a GET request to `/users/exists/Alice`.

# Example Output:
# {"exists": true}


# 2 Medium Exercises

# Exercise 4 (Medium): Create a Route to Paginate Users
# Explanation: Write a Flask route `/users/page/<int:page>` that returns a paginated list of users from the database.
# Assume a page size of 2 users per page.
# Solution:


# Example Input:
# Send a GET request to `/users/page/1`.

# Example Output:
# [{"id": 1, "name": "Alice", "role": "Data Engineer"}, {"id": 2, "name": "Bob", "role": "Data Scientist"}]


# Exercise 5 (Medium): Add a Route to Update User Role
# Explanation: Write a Flask route `/users/<int:user_id>/role` that updates the role of the specified user in the database.
# Solution:


# Example Input:
# Send a PUT request to `/users/1/role` with JSON body `{"role": "Data Scientist"}`.

# Example Output:
# {"id": 1, "name": "Alice", "role": "Data Scientist"}


# 1 Hard Exercise

# Exercise 6 (Hard): Create a Route to Search Users by Name Pattern
# Explanation: Write a Flask route `/users/search/<pattern>` that searches for users whose names match a given pattern (e.g., partial name match).
# Use SQLAlchemy's `like` method to perform a pattern search.
# Solution:


# Example Input:
# Send a GET request to `/users/search/Al`.

# Example Output:
# [{"id": 1, "name": "Alice", "role": "Data Engineer"}]
