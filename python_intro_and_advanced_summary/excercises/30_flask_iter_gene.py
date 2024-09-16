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


# Example Input:
# Send a GET request to `/users/iter/1`.

# Example Output:
# {"1": {"name": "Alice", "role": "Data Engineer"}, "2": {"name": "Bob", "role": "Data Scientist"}}


# Exercise 3 (Easy): Create a Generator to Filter Users by Role
# Explanation: Write a Flask route `/users/generator/<role>` that uses a generator to filter users by their role.
# Solution:


# Example Input:
# Send a GET request to `/users/generator/Data Scientist`.

# Example Output:
# [{"2": {"name": "Bob", "role": "Data Scientist"}}]


# 2 Medium Exercises

# Exercise 4 (Medium): Stream Large File Data with Generators
# Explanation: Write a Flask route `/stream/large-file` that uses a generator to stream large file data line-by-line.
# Solution:


# Example Input:
# Send a GET request to `/stream/large-file`.

# Example Output:
# Each line of 'large_file.txt' streamed one by one.


# Exercise 5 (Medium): Paginate and Stream Users Using Iterators and Generators
# Explanation: Write a Flask route `/stream/paginated-users` that combines an iterator and a generator to paginate and stream user data.
# Solution:


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


# Example Input:
# Assume 'user_data.txt' contains:
# 1,Alice,Data Engineer
# 2,Bob,Data Scientist
# 3,Charlie,ML Engineer

# Send a GET request to `/process/data`.

# Example Output:
# ID: 1, Name: ALICE, Role: Data Engineer
