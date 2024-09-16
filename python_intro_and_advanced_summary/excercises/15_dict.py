# Topic Recap: Dictionaries and Dictionary Methods (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Create and Access Dictionary
# Explanation: Write a function `create_employee_record` that creates a dictionary representing an employee record with keys: 'id', 'name', 'role', and 'salary'. Then, print each value using the keys.
# Solution:


# Example Input:
create_employee_record()

# Example Output:
# Employee ID: 1
# Employee Name: Alice
# Employee Role: Data Engineer
# Employee Salary: $70000


# Exercise 2 (Easy): Update Dictionary Value
# Explanation: Write a function `update_salary` that takes a dictionary representing an employee record and increases their salary by 10%. Return the updated dictionary.
# Solution:


# Example Input:
employee = {'id': 1, 'name': 'Alice', 'role': 'Data Engineer', 'salary': 70000}
updated_employee = update_salary(employee)
print(f"Updated Employee Record: {updated_employee}")

# Example Output:
# Updated Employee Record: {'id': 1, 'name': 'Alice', 'role': 'Data Engineer', 'salary': 77000.0}


# Exercise 3 (Easy): Delete Dictionary Entry
# Explanation: Write a function `remove_entry` that takes a dictionary and a key, and removes the key-value pair from the dictionary using the `pop()` method.
# Solution:


# Example Input:
data = {'id': 1, 'name': 'Alice', 'role': 'Data Engineer', 'salary': 70000}
key_to_remove = 'role'
updated_data = remove_entry(data, key_to_remove)
print(f"Data after removal: {updated_data}")

# Example Output:
# Data after removal: {'id': 1, 'name': 'Alice', 'salary': 70000}


# 2 Medium Exercises

# Exercise 4 (Medium): Merge Two Dictionaries
# Explanation: Write a function `merge_records` that takes two dictionaries representing employee details and merges them into one dictionary.
# Solution:


# Example Input:
employee_details1 = {'id': 1, 'name': 'Alice'}
employee_details2 = {'role': 'Data Engineer', 'salary': 70000}
merged_employee = merge_records(employee_details1, employee_details2)
print(f"Merged Employee Record: {merged_employee}")

# Example Output:
# Merged Employee Record: {'id': 1, 'name': 'Alice', 'role': 'Data Engineer', 'salary': 70000}


# Exercise 5 (Medium): Dictionary-Based Frequency Count
# Explanation: Write a function `count_occurrences` that takes a list of items and returns a dictionary where each key is an item and its value is the frequency of its occurrence.
# Solution:


# Example Input:
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
item_counts = count_occurrences(items)
print(f"Item Counts: {item_counts}")

# Example Output:
# Item Counts: {'apple': 3, 'banana': 2, 'orange': 1}


# 1 Hard Exercise

# Exercise 6 (Hard): Grouping Data by Key
# Explanation: Write a function `group_by_department` that takes a list of employee records (each represented as a dictionary with 'name' and 'department' keys) and returns a dictionary where each key is a department and its value is a list of employee names in that department.
# Solution:


# Example Input:
employees = [
    {'name': 'Alice', 'department': 'Data Science'},
    {'name': 'Bob', 'department': 'Data Engineering'},
    {'name': 'Charlie', 'department': 'Data Science'},
    {'name': 'David', 'department': 'ML Engineering'}
]
grouped_data = group_by_department(employees)
print(f"Grouped Data by Department: {grouped_data}")

# Example Output:
# Grouped Data by Department: {'Data Science': ['Alice', 'Charlie'], 'Data Engineering': ['Bob'], 'ML Engineering': ['David']}
