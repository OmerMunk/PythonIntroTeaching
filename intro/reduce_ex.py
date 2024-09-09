from functools import reduce

# reduce (function, iterable[, initializer]

# sum from zero
numbers = [1, 2, 3, 4]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)

# sum with initial value
data = [
    {
        'name': 'John',
        'money': 200
    },
    {
        'name': 'John',
        'money': 400
    },
    {
        'name': 'John',
        'money': 100
    },
    {
        'name': 'John',
        'money': 300
    },
]
sum_result = reduce(lambda x, y: x + y["money"], data, 100)
print(sum_result)




from functools import reduce

# Task 1 (Easy): Calculate Total Amount of All Transactions
# Explanation:
# Write a function `calculate_total_transactions` that takes a list of transaction amounts in NIS (New Israeli Shekel)
# and returns the total amount of all transactions combined. Use `reduce()` to sum up all the amounts.


# Example Input:
# transactions = [100.0, 250.5, 500.75, 1200.0, 300.25]

# Example Output:
# Output: Total amount of all transactions: 2351.5

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate the Net Balance After Applying Fees
# Explanation:
# Write a function `calculate_net_balance` that takes a list of dictionaries, where each dictionary represents a transaction
# with "amount" (float) and "fee" (float, in %). Use `reduce()` to calculate the net balance after applying the respective
# fee to each transaction. The function should return the net balance rounded to two decimal places.


# Example Input:
# transactions = [
#     {"amount": 1000.0, "fee": 2.0},
#     {"amount": 500.0, "fee": 1.5},
#     {"amount": 2000.0, "fee": 3.0},
#     {"amount": 1500.0, "fee": 2.5},
# ]

# Example Output:
# Output: Net balance after applying fees: 4777.5

# ----------------------------------------------------------------------

# Task 3 (Hard): Aggregate Customer Balances Across Multiple Accounts
# Explanation:
# Write a function `aggregate_customer_balances` that takes a list of customers, where each customer is represented by a
# dictionary with "name" (str) and "accounts" (list of dictionaries). Each account dictionary contains "account_number" (str)
# and "balance" (float). Use `reduce()` to calculate the total balance for each customer across all their accounts and return
# a dictionary mapping customer names to their total balances.


# Example Input:
# customers = [
#     {
#         "name": "Alice",
#         "accounts": [
#             {"account_number": "123-456-789", "balance": 5000.0},
#             {"account_number": "987-654-321", "balance": 3000.0},
#         ]
#     },
#     {
#         "name": "Bob",
#         "accounts": [
#             {"account_number": "111-222-333", "balance": 7500.0},
#             {"account_number": "444-555-666", "balance": 2500.0},
#             {"account_number": "777-888-999", "balance": 1000.0}
#         ]
#     }
# ]

# Example Output:
# Output: Total balances for each customer: {'Alice': 8000.0, 'Bob': 11000.0}