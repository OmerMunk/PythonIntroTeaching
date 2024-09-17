# Topic Recap: Sets and Frozen Sets (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Unique Items in a Data List
# Explanation: Write a Python program that takes a list of data entries (e.g., customer IDs) and prints a set of unique IDs.
# Guidance: Use the `set()` constructor to create a set of unique entries.
# Solution:
customer_ids = [101, 102, 103, 101, 104, 102, 105]
unique_ids = set(customer_ids)

print(f"Unique customer IDs: {unique_ids}")

# Example Input:
# (No input required)
# Example Output:
# Unique customer IDs: {101, 102, 103, 104, 105}


# Exercise 2 (Easy): Check Membership in a Set
# Explanation: Write a program that checks if a specific product is available in a set of available products.
# Guidance: Use the `in` operator to check membership in the set.
# Solution:
available_products = {"Laptop", "Smartphone", "Tablet", "Smartwatch"}
product_to_check = input("Enter the product name to check: ")

if product_to_check in available_products:
    print(f"{product_to_check} is available.")
else:
    print(f"{product_to_check} is not available.")

# Example Input:
# Enter the product name to check: Tablet
# Example Output:
# Tablet is available.


# Exercise 3 (Easy): Convert List to Frozen Set for Immutable Data
# Explanation: Write a program that takes a list of cities and converts it to a frozen set to ensure the data remains unchanged.
# Guidance: Use the `frozenset()` constructor.
# Solution:
cities = ["New York", "Los Angeles", "Chicago", "New York", "Houston"]
immutable_cities = frozenset(cities)

print(f"Immutable set of cities: {immutable_cities}")

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
team_a = {"Alice", "Bob", "Charlie", "David"}
team_b = {"Charlie", "David", "Edward", "Fiona"}

# Finding intersection and difference
employees_in_both_teams = team_a & team_b
employees_only_in_team_a = team_a - team_b

print(f"Employees in both teams: {employees_in_both_teams}")
print(f"Employees only in Team A: {employees_only_in_team_a}")

# Example Input:
# (No input required)
# Example Output:
# Employees in both teams: {'Charlie', 'David'}
# Employees only in Team A: {'Alice', 'Bob'}


# Exercise 5 (Medium): Detect Duplicates in Data Entries
# Explanation: Write a program that takes a list of email addresses and uses a set to detect and display any duplicate entries.
# Solution:
email_addresses = ["alice@example.com", "bob@example.com", "charlie@example.com", "alice@example.com", "david@example.com"]
unique_emails = set()
duplicates = set()

for email in email_addresses:
    if email in unique_emails:
        duplicates.add(email)
    else:
        unique_emails.add(email)

print(f"Duplicate email addresses: {duplicates}")

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
existing_customers = {1001, 1002, 1003, 1004, 1005}
new_customers = {1004, 1005, 1006, 1007, 1008}

# Finding existing customers who are already in the database
customers_already_in_db = existing_customers & new_customers

# Finding new unique customers
unique_new_customers = new_customers - existing_customers

# Combining both sets for a full customer list
all_customers = existing_customers | new_customers

print(f"Customers already in the database: {customers_already_in_db}")
print(f"New unique customers: {unique_new_customers}")
print(f"Full list of customers: {all_customers}")

# Example Input:
# (No input required)
# Example Output:
# Customers already in the database: {1004, 1005}
# New unique customers: {1006, 1007, 1008}
# Full list of customers: {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008}
