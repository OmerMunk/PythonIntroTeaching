# Topic Recap: Functions (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Function for Data Cleaning
# Explanation: Write a Python function named `clean_data` that takes a string input and returns the string with leading and trailing whitespace removed and all characters converted to lowercase.
# Guidance: Use the `strip()` and `lower()` string methods within the function.
# Solution:


# Example Output:
# Cleaned Data: 'data engineer'


# Exercise 2 (Easy): Function to Calculate Average
# Explanation: Write a function named `calculate_average` that takes a list of numbers and returns their average.
# Guidance: Use the `sum()` function and `len()` function to compute the average.
# Solution:


# Example Output:
# Average: 30.0


# Exercise 3 (Easy): Function to Convert Temperature
# Explanation: Write a Python function named `celsius_to_fahrenheit` that converts a temperature from Celsius to Fahrenheit.
# Guidance: Use the formula `F = (C * 9/5) + 32`.
# Solution:


# Example Output:
# 25°C in Fahrenheit is 77.0°F


# 2 Medium Exercises

# Exercise 4 (Medium): Function for Data Transformation
# Explanation: Write a function named `transform_data` that takes a list of numerical data points and normalizes them to a 0-1 scale.
# The function should:
# - Subtract the minimum value from each data point.
# - Divide the result by the range (max - min) of the list.
# Solution:


# Example Output:
# Normalized Data: [0.0, 0.25, 0.5, 0.75, 1.0]


# Exercise 5 (Medium): Function for Data Aggregation
# Explanation: Write a function named `aggregate_sales` that takes a list of tuples, where each tuple contains a product name and the number of units sold.
# The function should return a dictionary with the product names as keys and the total units sold as values.
# Solution:


# Example Output:
# Sales Summary: {'Laptop': 8, 'Smartphone': 10, 'Tablet': 7}


# 1 Hard Exercise

# Exercise 6 (Hard): Function for Data Filtering and Mapping
# Explanation: Create a function named `filter_and_map_data` that takes two arguments:
# - A list of dictionaries, each representing a data record (e.g., {'id': 1, 'age': 34, 'city': 'New York'})
# - A filter criterion dictionary (e.g., {'city': 'New York'})
# The function should filter the records that match the filter criterion and then map them to a new structure, returning only the 'id' and 'age' of the matched records.
# Solution:


# Example Output:
# Filtered Data: [{'id': 1, 'age': 34}, {'id': 3, 'age': 42}]
