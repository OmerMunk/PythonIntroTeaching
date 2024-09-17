# Topic Recap: groupby() (Data Engineering Oriented)

from itertools import groupby

# 3 Easy Exercises

# Exercise 1 (Easy): Group Data by First Letter
# Explanation: Write a function `group_by_first_letter` that takes a list of names and groups them by their first letter using `groupby()`.
# The function should return a dictionary where the keys are the first letters and the values are lists of names starting with that letter.
# Solution:
def group_by_first_letter(names):
    names_sorted = sorted(names)  # Ensure the list is sorted for groupby to work correctly
    grouped_data = {key: list(group) for key, group in groupby(names_sorted, key=lambda x: x[0])}
    return grouped_data

# Example Input:
names = ["Alice", "Aaron", "Bob", "Charlie", "Cathy", "David"]
grouped_names = group_by_first_letter(names)
print(f"Grouped Names by First Letter: {grouped_names}")

# Example Output:
# Grouped Names by First Letter: {'A': ['Aaron', 'Alice'], 'B': ['Bob'], 'C': ['Cathy', 'Charlie'], 'D': ['David']}


# Exercise 2 (Easy): Group Numbers by Even or Odd
# Explanation: Write a function `group_by_even_odd` that takes a list of numbers and groups them into even and odd numbers using `groupby()`.
# The function should return a dictionary where the keys are "Even" and "Odd".
# Solution:
def group_by_even_odd(numbers):
    numbers_sorted = sorted(numbers, key=lambda x: x % 2)
    grouped_data = {'Even': [], 'Odd': []}
    for key, group in groupby(numbers_sorted, key=lambda x: x % 2):
        if key == 0:
            grouped_data['Even'].extend(list(group))
        else:
            grouped_data['Odd'].extend(list(group))
    return grouped_data

# Example Input:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grouped_numbers = group_by_even_odd(numbers)
print(f"Grouped Numbers by Even/Odd: {grouped_numbers}")

# Example Output:
# Grouped Numbers by Even/Odd: {'Even': [2, 4, 6, 8, 10], 'Odd': [1, 3, 5, 7, 9]}


# Exercise 3 (Easy): Group Words by Length
# Explanation: Write a function `group_by_length` that takes a list of words and groups them by their length using `groupby()`.
# Solution:
def group_by_length(words):
    words_sorted = sorted(words, key=len)  # Sort by length for groupby
    grouped_data = {key: list(group) for key, group in groupby(words_sorted, key=len)}
    return grouped_data

# Example Input:
words = ["data", "science", "python", "AI", "ML", "analytics"]
grouped_words = group_by_length(words)
print(f"Grouped Words by Length: {grouped_words}")

# Example Output:
# Grouped Words by Length: {2: ['AI', 'ML'], 4: ['data'], 6: ['python'], 7: ['science'], 9: ['analytics']}


# 2 Medium Exercises

# Exercise 4 (Medium): Group Transactions by Type
# Explanation: Write a function `group_transactions_by_type` that takes a list of transactions, where each transaction is a dictionary with 'id', 'amount', and 'type' keys, and groups them by transaction type using `groupby()`.
# Solution:
def group_transactions_by_type(transactions):
    transactions_sorted = sorted(transactions, key=lambda x: x['type'])
    grouped_data = {key: list(group) for key, group in groupby(transactions_sorted, key=lambda x: x['type'])}
    return grouped_data

# Example Input:
transactions = [
    {'id': 1, 'amount': 1000, 'type': 'credit'},
    {'id': 2, 'amount': 500, 'type': 'debit'},
    {'id': 3, 'amount': 1200, 'type': 'credit'},
    {'id': 4, 'amount': 200, 'type': 'debit'}
]
grouped_transactions = group_transactions_by_type(transactions)
print(f"Grouped Transactions by Type: {grouped_transactions}")

# Example Output:
# Grouped Transactions by Type: {'credit': [{'id': 1, 'amount': 1000, 'type': 'credit'}, {'id': 3, 'amount': 1200, 'type': 'credit'}], 'debit': [{'id': 2, 'amount': 500, 'type': 'debit'}, {'id': 4, 'amount': 200, 'type': 'debit'}]}


# Exercise 5 (Medium): Group Employees by Department
# Explanation: Write a function `group_employees_by_department` that takes a list of employee dictionaries (each with 'name' and 'department' keys) and groups them by department using `groupby()`.
# Solution:
def group_employees_by_department(employees):
    employees_sorted = sorted(employees, key=lambda x: x['department'])
    grouped_data = {key: list(group) for key, group in groupby(employees_sorted, key=lambda x: x['department'])}
    return grouped_data

# Example Input:
employees = [
    {'name': 'Alice', 'department': 'Data Science'},
    {'name': 'Bob', 'department': 'Data Engineering'},
    {'name': 'Charlie', 'department': 'Data Science'},
    {'name': 'David', 'department': 'ML Engineering'}
]
grouped_employees = group_employees_by_department(employees)
print(f"Grouped Employees by Department: {grouped_employees}")

# Example Output:
# Grouped Employees by Department: {'Data Engineering': [{'name': 'Bob', 'department': 'Data Engineering'}], 'Data Science': [{'name': 'Alice', 'department': 'Data Science'}, {'name': 'Charlie', 'department': 'Data Science'}], 'ML Engineering': [{'name': 'David', 'department': 'ML Engineering'}]}


# 1 Hard Exercise

# Exercise 6 (Hard): Group Sales Data by Month
# Explanation: Write a function `group_sales_by_month` that takes a list of sales records, where each record is a dictionary with 'date' (in 'YYYY-MM-DD' format) and 'amount'. Group the records by month using `groupby()` and calculate the total sales for each month.
# Solution:
from datetime import datetime

def group_sales_by_month(sales):
    sales_sorted = sorted(sales, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d').month)
    grouped_data = {}
    for key, group in groupby(sales_sorted, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d').month):
        total_sales = sum(item['amount'] for item in group)
        grouped_data[key] = total_sales
    return grouped_data

# Example Input:
sales = [
    {'date': '2024-01-15', 'amount': 1000},
    {'date': '2024-02-10', 'amount': 1500},
    {'date': '2024-01-20', 'amount': 2000},
    {'date': '2024-02-18', 'amount': 1800},
    {'date': '2024-03-05', 'amount': 1200}
]
grouped_sales = group_sales_by_month(sales)
print(f"Grouped Sales by Month: {grouped_sales}")

# Example Output:
# Grouped Sales by Month: {1: 3000, 2: 3300, 3: 1200}
