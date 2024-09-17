# Topic Recap: Functions (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Function for Data Cleaning
# Explanation: Write a Python function named `clean_data` that takes a string input and returns the string with leading and trailing whitespace removed and all characters converted to lowercase.
# Guidance: Use the `strip()` and `lower()` string methods within the function.
# Solution:
def clean_data(data_entry):
    return data_entry.strip().lower()

# Example Input:
input_data = "   Data Engineer   "
cleaned_data = clean_data(input_data)
print(f"Cleaned Data: '{cleaned_data}'")

# Example Output:
# Cleaned Data: 'data engineer'


# Exercise 2 (Easy): Function to Calculate Average
# Explanation: Write a function named `calculate_average` that takes a list of numbers and returns their average.
# Guidance: Use the `sum()` function and `len()` function to compute the average.
# Solution:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example Input:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"Average: {average}")

# Example Output:
# Average: 30.0


# Exercise 3 (Easy): Function to Convert Temperature
# Explanation: Write a Python function named `celsius_to_fahrenheit` that converts a temperature from Celsius to Fahrenheit.
# Guidance: Use the formula `F = (C * 9/5) + 32`.
# Solution:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example Input:
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C in Fahrenheit is {fahrenheit_temp}°F")

# Example Output:
# 25°C in Fahrenheit is 77.0°F


# 2 Medium Exercises

# Exercise 4 (Medium): Function for Data Transformation
# Explanation: Write a function named `transform_data` that takes a list of numerical data points and normalizes them to a 0-1 scale.
# The function should:
# - Subtract the minimum value from each data point.
# - Divide the result by the range (max - min) of the list.
# Solution:
def transform_data(data):
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    normalized_data = [(x - min_val) / range_val for x in data]
    return normalized_data

# Example Input:
data_points = [10, 20, 30, 40, 50]
normalized_data = transform_data(data_points)
print(f"Normalized Data: {normalized_data}")

# Example Output:
# Normalized Data: [0.0, 0.25, 0.5, 0.75, 1.0]


# Exercise 5 (Medium): Function for Data Aggregation
# Explanation: Write a function named `aggregate_sales` that takes a list of tuples, where each tuple contains a product name and the number of units sold.
# The function should return a dictionary with the product names as keys and the total units sold as values.
# Solution:
def aggregate_sales(sales_data):
    sales_summary = {}
    for product, units_sold in sales_data:
        if product in sales_summary:
            sales_summary[product] += units_sold
        else:
            sales_summary[product] = units_sold
    return sales_summary

# Example Input:
sales_data = [("Laptop", 5), ("Smartphone", 10), ("Laptop", 3), ("Tablet", 7)]
sales_summary = aggregate_sales(sales_data)
print(f"Sales Summary: {sales_summary}")

# Example Output:
# Sales Summary: {'Laptop': 8, 'Smartphone': 10, 'Tablet': 7}


# 1 Hard Exercise

# Exercise 6 (Hard): Function for Data Filtering and Mapping
# Explanation: Create a function named `filter_and_map_data` that takes two arguments:
# - A list of dictionaries, each representing a data record (e.g., {'id': 1, 'age': 34, 'city': 'New York'})
# - A filter criterion dictionary (e.g., {'city': 'New York'})
# The function should filter the records that match the filter criterion and then map them to a new structure, returning only the 'id' and 'age' of the matched records.
# Solution:
def filter_and_map_data(records, criterion):
    filtered_records = [
        {'id': record['id'], 'age': record['age']}
        for record in records
        if all(record[key] == value for key, value in criterion.items())
    ]
    return filtered_records

# Example Input:
data_records = [
    {'id': 1, 'age': 34, 'city': 'New York'},
    {'id': 2, 'age': 29, 'city': 'Los Angeles'},
    {'id': 3, 'age': 42, 'city': 'New York'},
    {'id': 4, 'age': 30, 'city': 'Chicago'}
]
filter_criterion = {'city': 'New York'}
filtered_data = filter_and_map_data(data_records, filter_criterion)
print(f"Filtered Data: {filtered_data}")

# Example Output:
# Filtered Data: [{'id': 1, 'age': 34}, {'id': 3, 'age': 42}]
