# Topic Recap: List Comprehensions (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Convert Temperature List
# Explanation: Write a function `convert_temperatures` that takes a list of temperatures in Celsius and returns a new list with the temperatures converted to Fahrenheit using a list comprehension.
# Solution:
def convert_temperatures(celsius_list):
    return [(c * 9/5) + 32 for c in celsius_list]

# Example Input:
celsius_list = [0, 20, 30, 40]
fahrenheit_list = convert_temperatures(celsius_list)
print(f"Temperatures in Fahrenheit: {fahrenheit_list}")

# Example Output:
# Temperatures in Fahrenheit: [32.0, 68.0, 86.0, 104.0]


# Exercise 2 (Easy): Extract Even Numbers
# Explanation: Write a function `extract_even_numbers` that takes a list of integers and returns a new list containing only the even numbers using list comprehension.
# Solution:
def extract_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example Input:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = extract_even_numbers(numbers)
print(f"Even Numbers: {even_numbers}")

# Example Output:
# Even Numbers: [2, 4, 6, 8]


# Exercise 3 (Easy): Clean Data Entries
# Explanation: Write a function `clean_entries` that takes a list of strings with leading/trailing spaces and returns a new list with all entries stripped of whitespace and converted to lowercase using list comprehension.
# Solution:
def clean_entries(entries):
    return [entry.strip().lower() for entry in entries]

# Example Input:
entries = ["  Data Science  ", " Machine Learning ", "  AI "]
cleaned_entries = clean_entries(entries)
print(f"Cleaned Entries: {cleaned_entries}")

# Example Output:
# Cleaned Entries: ['data science', 'machine learning', 'ai']


# 2 Medium Exercises

# Exercise 4 (Medium): Normalize Data Points
# Explanation: Write a function `normalize_data` that takes a list of numerical data points and returns a new list with all points normalized to a 0-1 range using list comprehension.
# Solution:
def normalize_data(data_points):
    min_val, max_val = min(data_points), max(data_points)
    return [(x - min_val) / (max_val - min_val) for x in data_points]

# Example Input:
data_points = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data_points)
print(f"Normalized Data: {normalized_data}")

# Example Output:
# Normalized Data: [0.0, 0.25, 0.5, 0.75, 1.0]


# Exercise 5 (Medium): Filter and Transform Records
# Explanation: Write a function `filter_transform_records` that takes a list of tuples representing customer records `(id, name, age)` and returns a new list containing the names of customers who are at least 18 years old, in uppercase, using list comprehension.
# Solution:
def filter_transform_records(records):
    return [name.upper() for (id, name, age) in records if age >= 18]

# Example Input:
records = [(1, "Alice", 17), (2, "Bob", 20), (3, "Charlie", 15), (4, "David", 22)]
filtered_names = filter_transform_records(records)
print(f"Filtered Names: {filtered_names}")

# Example Output:
# Filtered Names: ['BOB', 'DAVID']


# 1 Hard Exercise

# Exercise 6 (Hard): Flatten and Process Nested Lists
# Explanation: Write a function `flatten_and_process_data` that takes a nested list representing sales data where each sublist is a list of sales amounts per day (e.g., `[[120, 150], [100, 200], [130, 170]]`).
# The function should:
# - Flatten the nested list into a single list of all sales amounts.
# - Filter out any sales amount less than 150.
# - Return a new list where each sales amount is increased by 10%.
# Solution:
def flatten_and_process_data(nested_sales):
    return [sale * 1.10 for day_sales in nested_sales for sale in day_sales if sale >= 150]

# Example Input:
nested_sales = [[120, 150], [100, 200], [130, 170]]
processed_sales = flatten_and_process_data(nested_sales)
print(f"Processed Sales: {processed_sales}")

# Example Output:
# Processed Sales: [165.0, 220.0, 187.0]
