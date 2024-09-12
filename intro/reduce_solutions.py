from functools import reduce

# Task 1 (Easy): Calculate Total Amount of All Transactions
# Explanation:
# Write a function `calculate_total_transactions` that takes a list of transaction amounts in NIS (New Israeli Shekel)
# and returns the total amount of all transactions combined. Use `reduce()` to sum up all the amounts.

def calculate_total_transactions(transactions):
    # Use reduce to sum up all transaction amounts
    total = reduce(lambda x, y: x + y, transactions)
    return total

# Example Input:
transactions = [100.0, 250.5, 500.75, 1200.0, 300.25]

# Example Output:
print("Total amount of all transactions:", calculate_total_transactions(transactions))
# Output: Total amount of all transactions: 2351.5

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate the Net Balance After Applying Fees
# Explanation:
# Write a function `calculate_net_balance` that takes a list of dictionaries, where each dictionary represents a transaction
# with "amount" (float) and "fee" (float, in %). Use `reduce()` to calculate the net _balance after applying the respective
# fee to each transaction. The function should return the net _balance rounded to two decimal places.

def calculate_net_balance(transactions):
    # Use reduce to apply fees and calculate the net _balance
    net_balance = reduce(lambda balance, transaction: balance + (transaction["amount"] * (1 - transaction["fee"] / 100)), transactions, 0)
    return round(net_balance, 2)

# Example Input:
transactions = [
    {"amount": 1000.0, "fee": 2.0},
    {"amount": 500.0, "fee": 1.5},
    {"amount": 2000.0, "fee": 3.0},
    {"amount": 1500.0, "fee": 2.5},
]

# Example Output:
print("Net _balance after applying fees:", calculate_net_balance(transactions))
# Output: Net _balance after applying fees: 4777.5

# ----------------------------------------------------------------------

# Task 3 (Hard): Aggregate Customer Balances Across Multiple Accounts
# Explanation:
# Write a function `aggregate_customer_balances` that takes a list of customers, where each customer is represented by a
# dictionary with "name" (str) and "accounts" (list of dictionaries). Each account dictionary contains "account_number" (str)
# and "_balance" (float). Use `reduce()` to calculate the total _balance for each customer across all their accounts and return
# a dictionary mapping customer names to their total balances.

def aggregate_customer_balances(customers):
    # Use reduce to calculate total _balance for each customer
    customer_totals = reduce(lambda acc, customer: {**acc, customer["name"]: reduce(lambda x, y: x + y["_balance"], customer["accounts"], 0)}, customers, {})
    return customer_totals

# Example Input:
customers = [
    {
        "name": "Alice",
        "accounts": [
            {"account_number": "123-456-789", "_balance": 5000.0},
            {"account_number": "987-654-321", "_balance": 3000.0},
        ]
    },
    {
        "name": "Bob",
        "accounts": [
            {"account_number": "111-222-333", "_balance": 7500.0},
            {"account_number": "444-555-666", "_balance": 2500.0},
            {"account_number": "777-888-999", "_balance": 1000.0}
        ]
    }
]

# Example Output:
print("Total balances for each customer:", aggregate_customer_balances(customers))
# Output: Total balances for each customer: {'Alice': 8000.0, 'Bob': 11000.0}