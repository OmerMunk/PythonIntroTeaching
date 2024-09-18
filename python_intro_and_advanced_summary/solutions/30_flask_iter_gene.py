# Topic Recap: Flask Exercises with Generators and Iterators (Data Engineering Oriented)

# Generators and iterators can be effectively used in Flask applications to handle large datasets or stream responses without loading everything into memory at once.
# These exercises will help you practice using generators and iterators within the context of a Flask web application.

from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# Sample data to use in exercises
users = {
    1: {"name": "Alice", "role": "Data Engineer"},
    2: {"name": "Bob", "role": "Data Scientist"},
    3: {"name": "Charlie", "role": "ML Engineer"},
    4: {"name": "David", "role": "Data Analyst"}
}

# 3 Easy Exercises

# Exercise 1 (Easy): Use a Generator to Stream User Data
# Explanation: Write a Flask route `/stream/users` that uses a generator to stream user data one by one.
# Solution:
def generate_user_stream():
    for user_id, user in users.items():
        yield f"{user_id}: {user['name']} - {user['role']}\n"

@app.route('/stream/users', methods=['GET'])
def stream_users():
    return Response(generate_user_stream(), mimetype='text/plain')

# Example Input:
# Send a GET request to `/stream/users`.

# Example Output:
# 1: Alice - Data Engineer
# 2: Bob - Data Scientist
# 3: Charlie - ML Engineer
# 4: David - Data Analyst


# Exercise 2 (Easy): Use Iterator to Paginate Users
# Explanation: Write a Flask route `/users/iter/<int:page>` that uses an iterator to paginate user data.
# Assume a page size of 2 users per page.
# Solution:
class UserIterator:
    def __init__(self, users, page_size):
        self.users = list(users.items())
        self.page_size = page_size
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page * self.page_size >= len(self.users):
            raise StopIteration
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        self.current_page += 1
        return dict(self.users[start_index:end_index])

@app.route('/users/iter/<int:page>', methods=['GET'])
def paginate_users_with_iterator(page):
    user_iterator = UserIterator(users, 2)
    paginated_users = None
    for i in range(page):
        try:
            paginated_users = next(user_iterator)
        except StopIteration:
            return jsonify({"error": "No more pages"}), 404
    return jsonify(paginated_users)

# Example Input:
# Send a GET request to `/users/iter/1`.

# Example Output:
# {"1": {"name": "Alice", "role": "Data Engineer"}, "2": {"name": "Bob", "role": "Data Scientist"}}


# Exercise 3 (Easy): Create a Generator to Filter Users by Role
# Explanation: Write a Flask route `/users/generator/<role>` that uses a generator to filter users by their role.
# Solution:
def filter_users_by_role(role):
    for user_id, user in users.items():
        if user['role'].lower() == role.lower():
            yield {user_id: user}

@app.route('/users/generator/<role>', methods=['GET'])
def get_users_by_role_generator(role):
    filtered_users = list(filter_users_by_role(role))
    if not filtered_users:
        return jsonify({"error": "No users found with this role"}), 404
    return jsonify(filtered_users)

# Example Input:
# Send a GET request to `/users/generator/Data Scientist`.

# Example Output:
# [{"2": {"name": "Bob", "role": "Data Scientist"}}]


# 2 Medium Exercises

# Exercise 4 (Medium): Stream Large File Data with Generators
# Explanation: Write a Flask route `/stream/large-file` that uses a generator to stream large file data line-by-line.
# Solution:
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line

@app.route('/stream/large-file', methods=['GET'])
def stream_large_file():
    return Response(read_large_file('large_file.txt'), mimetype='text/plain')

# Example Input:
# Send a GET request to `/stream/large-file`.

# Example Output:
# Each line of 'large_file.txt' streamed one by one.


# Exercise 5 (Medium): Paginate and Stream Users Using Iterators and Generators
# Explanation: Write a Flask route `/stream/paginated-users` that combines an iterator and a generator to paginate and stream user data.
# Solution:
def paginate_users_generator(page_size):
    iterator = iter(UserIterator(users, page_size))
    while True:
        try:
            yield str(next(iterator)) + "\n"
        except StopIteration:
            break

@app.route('/stream/paginated-users', methods=['GET'])
def stream_paginated_users():
    return Response(paginate_users_generator(2), mimetype='text/plain')

# Example Input:
# Send a GET request to `/stream/paginated-users`.

# Example Output:
# {"1": {"name": "Alice", "role": "Data Engineer"}, "2": {"name": "Bob", "role": "Data Scientist"}}
# {"3": {"name": "Charlie", "role": "ML Engineer"}, "4": {"name": "David", "role": "Data Analyst"}}


# 1 Hard Exercise

# Exercise 6 (Hard): Advanced Data Processing with Generators and Iterators
# Explanation: Write a Flask route `/process/data` that reads user data from a large file, processes it using a generator, and streams the processed data.
# The data processing should:
# 1. Filter out users with a specific role.
# 2. Apply a transformation (e.g., uppercase the user's name).
# Use a combination of generators and iterators.
# Solution:
def process_user_data(file_path, filter_role):
    with open(file_path, 'r') as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) < 2:
                continue
            user_id, name, role = user_data
            if role.lower() == filter_role.lower():
                yield f"ID: {user_id}, Name: {name.upper()}, Role: {role}\n"

@app.route('/process/data', methods=['GET'])
def process_data_stream():
    return Response(process_user_data('user_data.txt', 'Data Engineer'), mimetype='text/plain')

# Example Input:
# Assume 'user_data.txt' contains:
# 1,Alice,Data Engineer
# 2,Bob,Data Scientist
# 3,Charlie,ML Engineer

# Send a GET request to `/process/data`.

# Example Output:
# ID: 1, Name: ALICE, Role: Data Engineer
