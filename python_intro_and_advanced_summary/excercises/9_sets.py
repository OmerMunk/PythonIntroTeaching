# Topic Recap: Sets and Frozen Sets (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Unique Items in a Data List
# Explanation: Write a Python program that takes a list of data entries (e.g., customer IDs) and prints a set of unique IDs.
# Guidance: Use the `set()` constructor to create a set of unique entries.
# Solution:

# Example Input:
# (No input required)
# Example Output:
# Unique customer IDs: {101, 102, 103, 104, 105}


# Exercise 2 (Easy): Check Membership in a Set
# Explanation: Write a program that checks if a specific product is available in a set of available products.
# Guidance: Use the `in` operator to check membership in the set.
# Solution:


# Example Input:
# Enter the product name to check: Tablet
# Example Output:
# Tablet is available.


# Exercise 3 (Easy): Convert List to Frozen Set for Immutable Data
# Explanation: Write a program that takes a list of cities and converts it to a frozen set to ensure the data remains unchanged.
# Guidance: Use the `frozenset()` constructor.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Immutable set of cities: frozenset({'Chicago', 'New York', 'Houston', 'Los Angeles'})


# 2 Medium Exercises

# Exercise 4 (Medium): Set Operations for Data Comparison
# Explanation: Write a Python program that compares two sets of employees (Team A and Team B) to find:
# - Employees who are in both teams (intersection)
# - Employees who are only in Team A (difference)
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Employees in both teams: {'Charlie', 'David'}
# Employees only in Team A: {'Alice', 'Bob'}


# Exercise 5 (Medium): Detect Duplicates in Data Entries
# Explanation: Write a program that takes a list of email addresses and uses a set to detect and display any duplicate entries.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Duplicate email addresses: {'alice@example.com'}


# 1 Hard Exercise

# Exercise 6 (Hard): Set-Based Data Validation and Analysis
# Explanation: Create a program that takes two sets of data:
# - `existing_customers`: Set of customer IDs representing customers already in the database.
# - `new_customers`: Set of customer IDs representing newly registered customers.
# The program should:
# - Identify customers who are already in the database (intersection).
# - Identify new unique customers (difference).
# - Combine both sets to get a full list of customers (union).
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Customers already in the database: {1004, 1005}
# New unique customers: {1006, 1007, 1008}
# Full list of customers: {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008}
