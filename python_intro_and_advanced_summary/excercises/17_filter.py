# Topic Recap: filter() (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Filter Even Numbers
# Explanation: Write a function `filter_even_numbers` that takes a list of numbers and returns a new list containing only the even numbers using the `filter()` function.
# Solution:


# Example Input:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(f"Even Numbers: {even_numbers}")

# Example Output:
# Even Numbers: [2, 4, 6, 8, 10]


# Exercise 2 (Easy): Filter Short Names
# Explanation: Write a function `filter_short_names` that takes a list of names and returns a new list containing only the names shorter than 5 characters using `filter()`.
# Solution:

# Example Input:
names = ["Alice", "Bob", "Eve", "John", "Michael"]
short_names = filter_short_names(names)
print(f"Short Names: {short_names}")

# Example Output:
# Short Names: ['Bob', 'Eve', 'John']


# Exercise 3 (Easy): Filter Positive Numbers
# Explanation: Write a function `filter_positive_numbers` that takes a list of numbers and returns a new list containing only the positive numbers using `filter()`.
# Solution:


# Example Input:
numbers = [-2, -1, 0, 1, 2, 3, -5, -4]
positive_numbers = filter_positive_numbers(numbers)
print(f"Positive Numbers: {positive_numbers}")

# Example Output:
# Positive Numbers: [1, 2, 3]


# 2 Medium Exercises

# Exercise 4 (Medium): Filter Employees by Department
# Explanation: Write a function `filter_by_department` that takes a list of dictionaries representing employees (each with 'name' and 'department' keys) and returns a new list of employees who belong to the "Data Science" department using `filter()`.
# Solution:


# Example Input:
employees = [
    {'name': 'Alice', 'department': 'Data Science'},
    {'name': 'Bob', 'department': 'Data Engineering'},
    {'name': 'Charlie', 'department': 'Data Science'},
    {'name': 'David', 'department': 'ML Engineering'}
]
filtered_employees = filter_by_department(employees)
print(f"Filtered Employees: {filtered_employees}")

# Example Output:
# Filtered Employees: [{'name': 'Alice', 'department': 'Data Science'}, {'name': 'Charlie', 'department': 'Data Science'}]


# Exercise 5 (Medium): Filter Outliers from Data
# Explanation: Write a function `filter_outliers` that takes a list of numerical data points and filters out any points that are outside the range [mean - std_dev, mean + std_dev].
# Use `filter()` to achieve this.
# Solution:
from statistics import mean, stdev



# Example Input:
data = [10, 12, 14, 15, 17, 22, 24, 30, 35]
filtered_data = filter_outliers(data)
print(f"Filtered Data: {filtered_data}")

# Example Output:
# Filtered Data: [12, 14, 15, 17, 22, 24]


# 1 Hard Exercise

# Exercise 6 (Hard): Filter Transactions Above Threshold
# Explanation: Write a function `filter_transactions` that takes a list of dictionaries representing financial transactions (each with 'id', 'amount', and 'type' keys) and filters out transactions that are "debit" and above a certain threshold amount using `filter()`.
# Solution:


# Example Input:
transactions = [
    {'id': 1, 'amount': 1500, 'type': 'debit'},
    {'id': 2, 'amount': 800, 'type': 'credit'},
    {'id': 3, 'amount': 2000, 'type': 'debit'},
    {'id': 4, 'amount': 500, 'type': 'debit'},
    {'id': 5, 'amount': 1200, 'type': 'credit'}
]
threshold = 1000
filtered_transactions = filter_transactions(transactions, threshold)
print(f"Filtered Transactions: {filtered_transactions}")

# Example Output:
# Filtered Transactions: [{'id': 1, 'amount': 1500, 'type': 'debit'}, {'id': 3, 'amount': 2000, 'type': 'debit'}]
