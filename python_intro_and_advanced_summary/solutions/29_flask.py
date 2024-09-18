# Topic Recap: Flask (Data Engineering Oriented)

# Flask is a lightweight WSGI web application framework in Python that provides tools, libraries, and technologies for building web applications.
# Flask is known for its simplicity and flexibility, making it a popular choice for developers.

# Let's create a simple Flask application for basic user management (CRUD operations).

# Step-by-Step Guide for Building a Flask Application

# Step 1: Set Up Flask
# Install Flask using pip if not already installed:
# pip install flask

# Create a file named `app.py` and import Flask and necessary modules.

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Step 2: Create a Simple Data Store (In-Memory Database)
# In this example, we use a Python dictionary to store user data.
users = {
    1: {"name": "Alice", "role": "Data Engineer"},
    2: {"name": "Bob", "role": "Data Scientist"}
}

# Step 3: Define Routes for CRUD Operations

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route: Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json or 'role' not in request.json:
        abort(400, description="Bad request")
    new_id = max(users.keys()) + 1
    new_user = {
        "name": request.json['name'],
        "role": request.json['role']
    }
    users[new_id] = new_user
    return jsonify(new_user), 201

# Route: Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json:
        abort(400, description="Bad request")
    user = users.get(user_id)
    if user is None:
        abort(404, description="User not found")
    user['name'] = request.json.get('name', user['name'])
    user['role'] = request.json.get('role', user['role'])
    return jsonify(user)

# Route: Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if user is None:
        abort(404, description="User not found")
    return jsonify({"message": "User deleted successfully"})

# Step 4: Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)

# To run the Flask app, execute `python app.py` in your terminal.
# Access the application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

# Explanation:
# 1. `get_users`: Returns all users from the in-memory store.
# 2. `get_user`: Returns a single user based on the provided user ID.
# 3. `create_user`: Adds a new user to the in-memory store.
# 4. `update_user`: Updates the details of an existing user.
# 5. `delete_user`: Removes a user from the in-memory store.

# 3 Easy Exercises

# Exercise 1 (Easy): Create a Flask Route to Return Server Status
# Explanation: Write a Flask route `/status` that returns a JSON response with a key `"status"` and value `"running"`.
# Solution:
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({"status": "running"})

# Example Input:
# Send a GET request to `/status`.

# Example Output:
# {"status": "running"}


# Exercise 2 (Easy): Create a Route to Count Users
# Explanation: Write a Flask route `/users/count` that returns the count of users in the system.
# Solution:
@app.route('/users/count', methods=['GET'])
def user_count():
    return jsonify({"count": len(users)})

# Example Input:
# Send a GET request to `/users/count`.

# Example Output:
# {"count": 2}


# Exercise 3 (Easy): Add a Route to Greet Users
# Explanation: Write a Flask route `/greet/<name>` that returns a greeting message for the given user.
# Solution:
@app.route('/greet/<name>', methods=['GET'])
def greet_user(name):
    return jsonify({"message": f"Hello, {name}!"})

# Example Input:
# Send a GET request to `/greet/Alice`.

# Example Output:
# {"message": "Hello, Alice!"}


# 2 Medium Exercises

# Exercise 4 (Medium): Create a Route to Filter Users by Role
# Explanation: Write a Flask route `/users/role/<role>` that returns a list of users who have the specified role.
# Solution:
@app.route('/users/role/<role>', methods=['GET'])
def get_users_by_role(role):
    filtered_users = {uid: user for uid, user in users.items() if user['role'].lower() == role.lower()}
    if not filtered_users:
        abort(404, description="No users found with the specified role")
    return jsonify(filtered_users)

# Example Input:
# Send a GET request to `/users/role/Data Engineer`.

# Example Output:
# {"1": {"name": "Alice", "role": "Data Engineer"}}


# Exercise 5 (Medium): Add a Route to Update User Role
# Explanation: Write a Flask route `/users/<int:user_id>/role` that updates the role of the specified user.
# Solution:
@app.route('/users/<int:user_id>/role', methods=['PUT'])
def update_user_role(user_id):
    if not request.json or 'role' not in request.json:
        abort(400, description="Bad request")
    user = users.get(user_id)
    if user is None:
        abort(404, description="User not found")
    user['role'] = request.json['role']
    return jsonify(user)

# Example Input:
# Send a PUT request to `/users/1/role` with JSON body `{"role": "Data Scientist"}`.

# Example Output:
# {"name": "Alice", "role": "Data Scientist"}


# 1 Hard Exercise

# Exercise 6 (Hard): Create a Route to Paginate Users
# Explanation: Write a Flask route `/users/page/<int:page_number>` that returns a paginated list of users. Assume a page size of 1.
# Solution:
PAGE_SIZE = 1

@app.route('/users/page/<int:page_number>', methods=['GET'])
def paginate_users(page_number):
    start_index = (page_number - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE
    paginated_users = list(users.items())[start_index:end_index]
    if not paginated_users:
        abort(404, description="No users found on this page")
    return jsonify(dict(paginated_users))

# Example Input:
# Send a GET request to `/users/page/1`.

# Example Output:
# {"1": {"name": "Alice", "role": "Data Engineer"}}
