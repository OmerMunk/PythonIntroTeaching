from itertools import groupby

data = [
    ("TerroristA", "18:40", (12, 17)),
    ("TerroristB", "12:40", (18, 17)),
    ("TerroristC", "19:40", (20, 7)),
    ("TerroristA", "11:40", (300, -17)),
    ("TerroristB", "17:40", (350, -17))
]

sorted_data = sorted(data, key=lambda terrorist: terrorist[0])

print(sorted_data)



for key, group in groupby(sorted_data, key=lambda terrorist: terrorist[0]):
    print(f"key: {key}, group: {list(group)}")

from itertools import groupby


# Task 1 (Easy): Group Transactions by Type
# Explanation:
# Write a function `group_transactions_by_type` that takes a list of transactions, where each transaction is represented
# as a tuple with a transaction ID and a type (either "deposit" or "withdrawal"). Use `groupby` to group the transactions
# by type and return a dictionary with the types as keys and the list of transaction IDs as values.



# Example Input:
# transactions = [
#     ("T001", "deposit"),
#     ("T002", "withdrawal"),
#     ("T003", "deposit"),
#     ("T004", "deposit"),
#     ("T005", "withdrawal"),
# ]

# Example Output:


# Output: Grouped transactions by type: {'deposit': ['T001', 'T003', 'T004'], 'withdrawal': ['T002', 'T005']}

# ----------------------------------------------------------------------

# Task 2 (Medium): Group Account Balances by Status
# Explanation:
# Write a function `group_balances_by_status` that takes a list of dictionaries, where each dictionary represents
# an account with "account_number" (str) and "_balance" (float). Group the accounts into "positive" or "negative"
# based on their _balance using `groupby`, and return a dictionary with the statuses as keys and a list of account numbers as values.




# Example Input:
# accounts = [
#     {"account_number": "123-456-789", "_balance": 5000.0},
#     {"account_number": "987-654-321", "_balance": -750.0},
#     {"account_number": "111-222-333", "_balance": 12000.0},
#     {"account_number": "444-555-666", "_balance": -200.0},
# ]

# Example Output:


# Output: Grouped balances by status: {'positive': ['123-456-789', '111-222-333'], 'negative': ['987-654-321', '444-555-666']}

# ----------------------------------------------------------------------

# Task 3 (Hard): Group and Summarize Transactions by Customer and Type
# Explanation:
# Write a function `summarize_transactions_by_customer` that takes a list of transactions, where each transaction
# is represented as a dictionary with "customer_id", "transaction_id", "type" (either "deposit" or "withdrawal"),
# and "amount" (float). Group the transactions by customer ID and type, and calculate the total amount for each group.
# Return a dictionary with the customer IDs as keys and a nested dictionary of transaction types and their total amounts as values.



# Example Input:
# transactions = [
#     {"customer_id": "C001", "transaction_id": "T001", "type": "deposit", "amount": 1000.0},
#     {"customer_id": "C002", "transaction_id": "T002", "type": "withdrawal", "amount": 500.0},
#     {"customer_id": "C001", "transaction_id": "T003", "type": "deposit", "amount": 2000.0},
#     {"customer_id": "C002", "transaction_id": "T004", "type": "deposit", "amount": 1500.0},
#     {"customer_id": "C001", "transaction_id": "T005", "type": "withdrawal", "amount": 300.0},
# ]

# Example Output:
# Output: Summarized transactions by customer: {'C001': {'deposit': 3000.0, 'withdrawal': 300.0}, 'C002': {'withdrawal': 500.0, 'deposit': 1500.0}}