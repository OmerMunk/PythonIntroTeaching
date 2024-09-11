from itertools import groupby
#
# data = [
#     ("TerroristA", "18:40", (12, 17)),
#     ("TerroristB", "12:40", (18, 17)),
#     ("TerroristC", "19:40", (20, 7)),
#     ("TerroristA", "11:40", (300, -17)),
#     ("TerroristB", "17:40", (350, -17))
# ]
#
# sorted_data = sorted(data, key=lambda terrorist: terrorist[0])
#
# print(sorted_data)
#
#
#
# for key, group in groupby(sorted_data, key=lambda terrorist: terrorist[0]):
#     print(f"key: {key}, group: {list(group)}")


# Task 1 (Easy): Group Transactions by Type
# Explanation:
# Write a function `group_transactions_by_type` that takes a list of transactions, where each transaction is represented
# as a tuple with a transaction ID and a type (either "deposit" or "withdrawal"). Use `groupby` to group the transactions
# by type and return a dictionary with the types as keys and the list of transaction IDs as values.



# Example Input:


# Example Output:

# Output: Grouped transactions by type: {'deposit': ['T001', 'T003', 'T004'], 'withdrawal': ['T002', 'T005']}

TRANSACTION_TYPE_INDEX = 1
TRANSACTION_ID_INDEX = 0

def transaction_key(transaction):

    return transaction[TRANSACTION_TYPE_INDEX]

def group_transactions_by_type(transactions: list):
    sorted_transactions = sorted(transactions, key=transaction_key)
    transaction_by_type = {}
    for key, group in groupby(sorted_transactions, key=transaction_key):
        transaction_by_type[key] = [x[TRANSACTION_ID_INDEX] for x in list(group)]
    return transaction_by_type





transactions = [
    ("T001", "deposit"),
    ("T002", "withdrawal"),
    ("T003", "deposit"),
    ("T004", "deposit"),
    ("T005", "withdrawal"),
]

print(group_transactions_by_type(transactions))

# {'deposit': [('T001', 'deposit'), ('T003', 'deposit'), ('T004', 'deposit')], 'withdrawal': [('T002', 'withdrawal'), ('T005', 'withdrawal')]}
# {'deposit': ['T001', 'T003', 'T004'], 'withdrawal': ['T002', 'T005']}

