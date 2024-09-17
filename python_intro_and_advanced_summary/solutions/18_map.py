# Topic Recap: map() (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Convert to Uppercase
# Explanation: Write a function `convert_to_uppercase` that takes a list of names and returns a new list with all names converted to uppercase using the `map()` function.
# Solution:
def convert_to_uppercase(names):
    return list(map(lambda name: name.upper(), names))

# Example Input:
names = ["Alice", "Bob", "Charlie"]
uppercase_names = convert_to_uppercase(names)
print(f"Uppercase Names: {uppercase_names}")

# Example Output:
# Uppercase Names: ['ALICE', 'BOB', 'CHARLIE']


# Exercise 2 (Easy): Square List Elements
# Explanation: Write a function `square_numbers` that takes a list of numbers and returns a new list containing the squares of each number using `map()`.
# Solution:
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Example Input:
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(f"Squared Numbers: {squared_numbers}")

# Example Output:
# Squared Numbers: [1, 4, 9, 16, 25]


# Exercise 3 (Easy): Add Tax to Prices
# Explanation: Write a function `add_tax` that takes a list of prices and returns a new list with a 10% tax added to each price using `map()`.
# Solution:
def add_tax(prices):
    return list(map(lambda price: round(price * 1.1, 2), prices))

# Example Input:
prices = [100, 200, 300]
prices_with_tax = add_tax(prices)
print(f"Prices with Tax: {prices_with_tax}")

# Example Output:
# Prices with Tax: [110.0, 220.0, 330.0]


# 2 Medium Exercises

# Exercise 4 (Medium): Normalize Data Points
# Explanation: Write a function `normalize_data_points` that takes a list of data points and returns a new list where each data point is normalized to a 0-1 range using `map()`.
# Solution:
def normalize_data_points(data_points):
    min_val, max_val = min(data_points), max(data_points)
    return list(map(lambda x: (x - min_val) / (max_val - min_val), data_points))

# Example Input:
data_points = [10, 20, 30, 40, 50]
normalized_data = normalize_data_points(data_points)
print(f"Normalized Data Points: {normalized_data}")

# Example Output:
# Normalized Data Points: [0.0, 0.25, 0.5, 0.75, 1.0]


# Exercise 5 (Medium): Convert List of Tuples to Strings
# Explanation: Write a function `format_employee_data` that takes a list of tuples, where each tuple represents an employee's name and role, and returns a new list with formatted strings like "Name: Role" using `map()`.
# Solution:
def format_employee_data(employee_data):
    return list(map(lambda emp: f"{emp[0]}: {emp[1]}", employee_data))

# Example Input:
employee_data = [("Alice", "Data Engineer"), ("Bob", "Data Scientist"), ("Charlie", "ML Engineer")]
formatted_data = format_employee_data(employee_data)
print(f"Formatted Employee Data: {formatted_data}")

# Example Output:
# Formatted Employee Data: ['Alice: Data Engineer', 'Bob: Data Scientist', 'Charlie: ML Engineer']


# 1 Hard Exercise

# Exercise 6 (Hard): Calculate Yearly Salary Increase
# Explanation: Write a function `calculate_salary_increase` that takes a list of dictionaries representing employees (each with 'name' and 'current_salary' keys) and a percentage increase.
# The function should return a new list of dictionaries with updated salaries using `map()`.
# Solution:
def calculate_salary_increase(employees, percentage):
    return list(map(lambda emp: {'name': emp['name'], 'current_salary': round(emp['current_salary'] * (1 + percentage / 100), 2)}, employees))

# Example Input:
employees = [{'name': 'Alice', 'current_salary': 70000}, {'name': 'Bob', 'current_salary': 85000}, {'name': 'Charlie', 'current_salary': 90000}]
percentage_increase = 5
updated_salaries = calculate_salary_increase(employees, percentage_increase)
print(f"Updated Salaries: {updated_salaries}")

# Example Output:
# Updated Salaries: [{'name': 'Alice', 'current_salary': 73500.0}, {'name': 'Bob', 'current_salary': 89250.0}, {'name': 'Charlie', 'current_salary': 94500.0}]
