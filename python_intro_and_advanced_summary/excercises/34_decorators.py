# Topic Recap: Decorators in Python (Data Engineering Oriented)

# Decorators in Python are functions that modify the behavior of other functions or methods.
# They are a powerful tool for enhancing or extending the functionality of existing code in a reusable way.
# In Flask, decorators are often used for routing, authentication, and other common tasks.

# Let's start with some basic examples of decorators and then move on to more advanced use cases.

# Basic Decorator Example

# Step 1: Create a Basic Decorator
# Explanation: Write a simple decorator `my_decorator` that adds some behavior before and after a function.
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

# Step 2: Use the Decorator on a Function
@my_decorator
def say_hello():
    print("Hello!")

# Example Input:
say_hello()

# Example Output:
# Something before the function.
# Hello!
# Something after the function.


# Step-by-Step Guide for Using Decorators in Flask

# In Flask, decorators are used extensively for defining routes and managing common tasks.

# Step 3: Set Up a Flask Application with Decorators
from flask import Flask, jsonify, request, abort, g, current_app
from functools import wraps

app = Flask(__name__)

# Decorator for logging requests
def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Request to {request.path} with method {request.method}")
        return func(*args, **kwargs)
    return wrapper

# Route: Use the log_request decorator to log each request
@app.route('/hello', methods=['GET'])
@log_request
def hello():
    return jsonify({"message": "Hello, World!"})

# Step 4: Create a Custom Decorator for Authentication
# Explanation: Write a decorator `require_api_key` that checks for an API key in the request headers.
def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != 'secret-key':
            abort(401, description="Unauthorized")
        return func(*args, **kwargs)
    return wrapper

# Route: Protect the `/secure-data` route with the require_api_key decorator
@app.route('/secure-data', methods=['GET'])
@require_api_key
def secure_data():
    return jsonify({"data": "Sensitive Information"})

# Step 5: Use Decorators for Caching Results
# Explanation: Write a decorator `cache_result` that caches the result of a function to optimize performance.
cache = {}

def cache_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = f"{func.__name__}:{args}:{kwargs}"
        if cache_key in cache:
            print("Returning cached result.")
            return cache[cache_key]
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
    return wrapper

# Route: Use the cache_result decorator to cache the result of this computation
@app.route('/compute', methods=['GET'])
@cache_result
def compute():
    # Simulate a time-consuming computation
    result = sum(range(1000000))
    return jsonify({"result": result})

# Step 6: Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)

# To run the Flask app, execute `python app.py` in your terminal.
# Access the application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

# Explanation:
# 1. `log_request`: A simple decorator that logs each request to the console.
# 2. `require_api_key`: A decorator that checks for an API key in the request headers for authentication.
# 3. `cache_result`: A decorator that caches the result of a function to avoid repeated computation.

# 3 Easy Exercises

# Exercise 1 (Easy): Create a Decorator to Track Function Execution
# Explanation: Write a decorator `track_execution` that prints "Executing..." before a function runs and "Done." after it runs.
# Solution:


# Example Usage:
@track_execution
def process_data():
    print("Processing data...")

# Example Input:
process_data()

# Example Output:
# Executing...
# Processing data...
# Done.


# Exercise 2 (Easy): Create a Decorator to Log Function Arguments
# Explanation: Write a decorator `log_arguments` that logs the arguments passed to a function.
# Solution:


# Example Usage:
@log_arguments
def add(a, b):
    return a + b

# Example Input:
result = add(5, 10)
print(result)

# Example Output:
# Arguments: args=(5, 10), kwargs={}
# 15


# Exercise 3 (Easy): Create a Decorator to Measure Execution Time
# Explanation: Write a decorator `measure_time` that measures and prints the execution time of a function.
# Solution:
import time



# Example Usage:
@measure_time
def long_running_task():
    time.sleep(2)

# Example Input:
long_running_task()

# Example Output:
# Execution time: 2.0001 seconds


# 2 Medium Exercises

# Exercise 4 (Medium): Create a Decorator to Validate JSON Input in Flask
# Explanation: Write a decorator `validate_json` that ensures the incoming request has a valid JSON body with required fields.
# Solution:


# Example Usage in Flask:
@app.route('/data', methods=['POST'])
@validate_json(['name', 'age'])
def add_data():
    return jsonify({"message": "Data added successfully"})

# Example Input:
# Send a POST request to `/data` with JSON body `{"name": "Alice", "age": 30}`.

# Example Output:
# {"message": "Data added successfully"}


# Exercise 5 (Medium): Create a Decorator to Limit API Requests
# Explanation: Write a decorator `rate_limit` that limits the number of API requests per user within a given time window.
# Solution:
from functools import wraps
from time import time

user_requests = {}



# Example Usage in Flask:
@app.route('/limited', methods=['GET'])
@rate_limit(limit=5, period=60)
def limited_route():
    return jsonify({"message": "Request successful"})

# Example Input:
# Send GET requests to `/limited` up to 5 times in 60 seconds.

# Example Output:
# {"message": "Request successful"} for the first 5 requests, then 429 Too Many Requests for subsequent requests.


# 1 Hard Exercise

# Exercise 6 (Hard): Create a Decorator to Handle Exceptions Globally in Flask
# Explanation: Write a decorator `handle_exceptions` that wraps Flask routes and provides a generic error handler for exceptions, logging errors and returning a JSON response.
# Solution:


# Example Usage in Flask:
@app.route('/error-prone', methods=['GET'])
@handle_exceptions
def error_prone_route():
    # Simulate an error
    raise ValueError("This is an intentional error!")

# Example Input:
# Send a GET request to `/error-prone`.

# Example Output:
# {"error": "This is an intentional error!"}
