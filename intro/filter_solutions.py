# Task 1 (Easy): Filter High-Value Bank Transactions
# Explanation:
# Write a function `filter_high_value_transactions` that takes a list of transactions as input, where each transaction is
# represented by a dictionary with keys "id" (transaction ID) and "amount" (transaction amount in NIS). The function should
# use `filter()` to return a list of all transactions with an amount greater than 1,000 NIS.

def filter_high_value_transactions(transactions):
    # Use filter to find transactions with amount greater than 1000
    high_value_transactions = list(filter(lambda x: x["amount"] > 1000, transactions))
    return high_value_transactions

# Example Input:
transactions = [
    {"id": "T001", "amount": 500.0},
    {"id": "T002", "amount": 1500.0},
    {"id": "T003", "amount": 750.0},
    {"id": "T004", "amount": 2000.0}
]

# Example Output:
print("High-value transactions:", filter_high_value_transactions(transactions))
# Output: High-value transactions: [{'id': 'T002', 'amount': 1500.0}, {'id': 'T004', 'amount': 2000.0}]

# ----------------------------------------------------------------------

# Task 2 (Medium): Filter Customers with Loans Above a Certain Interest Rate
# Explanation:
# Write a function `filter_high_interest_loans` that takes a dictionary representing customer loans, where each key is a
# customer name and the value is another dictionary with keys "loan_amount" (float) and "interest_rate" (float, in %). The
# function should use `filter()` to find and return a list of customer names with loans that have an interest rate above 5%.

def filter_high_interest_loans(customers):
    # Use filter to find customers with loans above 5% interest rate
    high_interest_customers = list(filter(lambda customer: customers[customer]["interest_rate"] > 5, customers))
    return high_interest_customers

# Example Input:
customers = {
    "Alice": {"loan_amount": 100000, "interest_rate": 3.5},
    "Bob": {"loan_amount": 200000, "interest_rate": 6.5},
    "Charlie": {"loan_amount": 150000, "interest_rate": 5.0},
    "David": {"loan_amount": 180000, "interest_rate": 7.0}
}

# Example Output:
print("Customers with high-interest loans:", filter_high_interest_loans(customers))
# Output: Customers with high-interest loans: ['Bob', 'David']

# ----------------------------------------------------------------------

# Task 3 (Hard): Filter and Sort Bank Accounts Based on Minimum Balance and Account Type
# Explanation:
# Write a function `filter_and_sort_accounts` that takes a list of dictionaries, where each dictionary represents a bank
# account with keys "account_number" (str), "_balance" (float), and "account_type" (str - "savings" or "checking"). The function
# should first use `filter()` to find accounts with a _balance greater than 10,000 NIS and of type "savings". Then, it should
# sort the filtered accounts in descending order by _balance and return the sorted list.

def filter_and_sort_accounts(accounts):
    # Use filter to find savings accounts with _balance greater than 10,000 NIS
    filtered_accounts = filter(lambda acc: acc["_balance"] > 10000 and acc["account_type"] == "savings", accounts)
    # Sort the filtered accounts by _balance in descending order
    sorted_accounts = sorted(filtered_accounts, key=lambda acc: acc["_balance"], reverse=True)
    return sorted_accounts

# Example Input:
accounts = [
    {"account_number": "001", "_balance": 15000.0, "account_type": "savings"},
    {"account_number": "002", "_balance": 8000.0, "account_type": "savings"},
    {"account_number": "003", "_balance": 20000.0, "account_type": "checking"},
    {"account_number": "004", "_balance": 30000.0, "account_type": "savings"},
    {"account_number": "005", "_balance": 5000.0, "account_type": "checking"}
]

# Example Output:
print("Filtered and sorted accounts:", filter_and_sort_accounts(accounts))
# Output: Filtered and sorted accounts: [{'account_number': '004', '_balance': 30000.0, 'account_type': 'savings'}, {'account_number': '001', '_balance': 15000.0, 'account_type': 'savings'}]