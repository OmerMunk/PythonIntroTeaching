#  zip(*iterables)
# list1, list2, list3
# zip(list1, list2)
# zip(list1, list2, list3)

# how to zip elements together
names = ["Abraham", "Yitshak", "Yaakov", "Metushelah"]
ages = [137, 185, 147, 969]
properties = ["Yazam", "Leader", "Fighter", "Zaken"]
combined = list(zip(names, ages))
combined_extra = list(zip(names, ages, properties))
print(combined)
print(combined_extra)


#this is how to unzip
unzipped_names, unzipped_ages, unzipped_properties = zip(*combined_extra)
print(f"unzipped names: {unzipped_names}")
print(f"unzipped unzipped_ages: {unzipped_ages}")
print(f"unzipped unzipped_properties: {unzipped_properties}")



# Task 1 (Easy): Pair Customer Names with Their Account Numbers
# Explanation:
# Write a function `pair_customers_with_accounts` that takes two lists: one containing customer names and the other containing
# their corresponding account numbers. Use `zip()` to create a list of tuples where each tuple contains a customer name and
# their account number.


# Example Input:
# names = ["Alice", "Bob", "Charlie"]
# account_numbers = ["123-456-789", "987-654-321", "111-222-333"]

# Example Output:
# Output: Paired customers with accounts: [('Alice', '123-456-789'), ('Bob', '987-654-321'), ('Charlie', '111-222-333')]

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate Total Balance Across Multiple Accounts for Each Customer
# Explanation:
# Write a function `calculate_total_balance_per_customer` that takes two lists: one containing customer names (where a customer
# might appear multiple times) and the other containing their corresponding account balances. Use `zip()` to combine the lists
# and then use a dictionary to sum up the total _balance for each customer.



# Example Input:
# names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
# balances = [5000.0, 3000.0, 1500.0, 7000.0, 2500.0]

# Example Output:
# Output: Total _balance per customer: {'Alice': 6500.0, 'Bob': 5500.0, 'Charlie': 7000.0}

# ----------------------------------------------------------------------

# Task 3 (Hard): Generate Financial Report of Multiple Branches
# Explanation:
# Write a function `generate_financial_report` that takes three lists: one containing branch names, another containing lists of
# account balances for each branch, and a third list containing the corresponding list of transaction counts for each branch.
# Use `zip()` to pair these values together and then generate a financial report showing the branch name, total _balance, and
# average transaction amount per branch.



# Example Input:
# branches = ["Tel Aviv", "Jerusalem", "Haifa"]
# balances_per_branch = [
#     [5000, 7500, 10000],  # Balances for Tel Aviv
#     [3000, 4000, 2000],   # Balances for Jerusalem
#     [7000, 8000, 6000]    # Balances for Haifa
# ]
# transactions_per_branch = [
#     [10, 15, 20],  # Transactions for Tel Aviv
#     [8, 12, 10],   # Transactions for Jerusalem
#     [5, 8, 7]      # Transactions for Haifa
# ]

# Example Output:
# Output:
# Financial report: [
#   {'branch': 'Tel Aviv', 'total_balance': 22500, 'average_transaction_amount': 500.0},
#   {'branch': 'Jerusalem', 'total_balance': 9000, 'average_transaction_amount': 300.0},
#   {'branch': 'Haifa', 'total_balance': 21000, 'average_transaction_amount': 1050.0}
# ]
