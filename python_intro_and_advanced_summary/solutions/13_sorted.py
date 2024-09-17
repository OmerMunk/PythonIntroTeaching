# Topic Recap: sorted(), sort() (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Sort List of Numbers
# Explanation: Write a function `sort_numbers` that takes a list of numbers and returns a new list with the numbers sorted in ascending order using the `sorted()` function.
# Solution:
def sort_numbers(numbers):
    return sorted(numbers)

# Example Input:
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sort_numbers(numbers)
print(f"Sorted Numbers: {sorted_numbers}")

# Example Output:
# Sorted Numbers: [1, 2, 5, 7, 9]


# Exercise 2 (Easy): Sort Data Alphabetically
# Explanation: Write a function `sort_data` that takes a list of strings representing data entries and returns a new list with the entries sorted alphabetically using `sorted()`.
# Solution:
def sort_data(entries):
    return sorted(entries)

# Example Input:
entries = ["Data Engineer", "Data Scientist", "ML Engineer", "BI Specialist"]
sorted_entries = sort_data(entries)
print(f"Sorted Data Entries: {sorted_entries}")

# Example Output:
# Sorted Data Entries: ['BI Specialist', 'Data Engineer', 'Data Scientist', 'ML Engineer']


# Exercise 3 (Easy): Sort Data in Reverse Order
# Explanation: Write a function `sort_reverse` that takes a list of numbers and returns a new list with the numbers sorted in descending order using the `sorted()` function.
# Solution:
def sort_reverse(numbers):
    return sorted(numbers, reverse=True)

# Example Input:
numbers = [10, 5, 8, 3]
sorted_reverse = sort_reverse(numbers)
print(f"Sorted Numbers in Descending Order: {sorted_reverse}")

# Example Output:
# Sorted Numbers in Descending Order: [10, 8, 5, 3]


# 2 Medium Exercises

# Exercise 4 (Medium): Sort List of Dictionaries by Key
# Explanation: Write a function `sort_records` that takes a list of dictionaries representing employee records, each containing 'name' and 'age' keys, and returns a new list sorted by 'age' in ascending order using `sorted()`.
# Solution:
def sort_records(records):
    return sorted(records, key=lambda x: x['age'])

# Example Input:
records = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_records = sort_records(records)
print(f"Sorted Records by Age: {sorted_records}")

# Example Output:
# Sorted Records by Age: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


# Exercise 5 (Medium): Sort and Filter Data
# Explanation: Write a function `sort_and_filter_sales` that takes a list of tuples representing sales data (product_name, sales_amount) and returns a sorted list of products with sales over 100, in descending order by sales amount.
# Solution:
def sort_and_filter_sales(sales_data):
    filtered_data = [record for record in sales_data if record[1] > 100]
    return sorted(filtered_data, key=lambda x: x[1], reverse=True)

# Example Input:
sales_data = [("Laptop", 150), ("Smartphone", 80), ("Tablet", 120), ("Monitor", 90)]
sorted_sales = sort_and_filter_sales(sales_data)
print(f"Sorted and Filtered Sales Data: {sorted_sales}")

# Example Output:
# Sorted and Filtered Sales Data: [('Laptop', 150), ('Tablet', 120)]


# 1 Hard Exercise

# Exercise 6 (Hard): Sort Nested Lists by Column
# Explanation: Write a function `sort_nested_lists` that takes a nested list representing a dataset (e.g., [[ID, Name, Age], ...]) and sorts the list by a specified column index. The function should:
# - Take two arguments: the nested list and the column index to sort by.
# - Return the sorted nested list.
# Solution:
def sort_nested_lists(data, column_index):
    return sorted(data, key=lambda x: x[column_index])

# Example Input:
data = [[1, "Alice", 30], [2, "Bob", 25], [3, "Charlie", 35]]
sorted_data_by_age = sort_nested_lists(data, 2)  # Sort by age (column index 2)
print(f"Sorted Data by Age: {sorted_data_by_age}")

# Example Output:
# Sorted Data by Age: [[2, 'Bob', 25], [1, 'Alice', 30], [3, 'Charlie', 35]]
