# Task 1 (Easy): Pair Customer Names with Their Account Numbers
# Explanation:
# Write a function `pair_customers_with_accounts` that takes two lists: one containing customer names and the other containing
# their corresponding account numbers. Use `zip()` to create a list of tuples where each tuple contains a customer name and
# their account number.

def pair_customers_with_accounts(names, account_numbers):
    # Use zip to pair names with their account numbers
    paired_list = list(zip(names, account_numbers))
    return paired_list

# Example Input:
names = ["Alice", "Bob", "Charlie"]
account_numbers = ["123-456-789", "987-654-321", "111-222-333"]

# Example Output:
print("Paired customers with accounts:", pair_customers_with_accounts(names, account_numbers))
# Output: Paired customers with accounts: [('Alice', '123-456-789'), ('Bob', '987-654-321'), ('Charlie', '111-222-333')]

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate Total Balance Across Multiple Accounts for Each Customer
# Explanation:
# Write a function `calculate_total_balance_per_customer` that takes two lists: one containing customer names (where a customer
# might appear multiple times) and the other containing their corresponding account balances. Use `zip()` to combine the lists
# and then use a dictionary to sum up the total balance for each customer.

def calculate_total_balance_per_customer(names, balances):
    # Use zip to combine names with their corresponding balances
    combined = zip(names, balances)
    # Dictionary to store the total balance for each customer
    total_balances = {}
    for name, balance in combined:
        if name in total_balances:
            total_balances[name] += balance
        else:
            total_balances[name] = balance
    return total_balances

# Example Input:
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
balances = [5000.0, 3000.0, 1500.0, 7000.0, 2500.0]

# Example Output:
print("Total balance per customer:", calculate_total_balance_per_customer(names, balances))
# Output: Total balance per customer: {'Alice': 6500.0, 'Bob': 5500.0, 'Charlie': 7000.0}

# ----------------------------------------------------------------------

# Task 3 (Hard): Generate Financial Report of Multiple Branches
# Explanation:
# Write a function `generate_financial_report` that takes three lists: one containing branch names, another containing lists of
# account balances for each branch, and a third list containing the corresponding list of transaction counts for each branch.
# Use `zip()` to pair these values together and then generate a financial report showing the branch name, total balance, and
# average transaction amount per branch.

def generate_financial_report(branches, balances_per_branch, transactions_per_branch):
    # Use zip to combine branches, balances, and transactions
    report = []
    for branch, balances, transactions in zip(branches, balances_per_branch, transactions_per_branch):
        total_balance = sum(balances)
        total_transactions = sum(transactions)
        average_transaction_amount = total_balance / total_transactions if total_transactions != 0 else 0
        report.append({
            "branch": branch,
            "total_balance": total_balance,
            "average_transaction_amount": round(average_transaction_amount, 2)
        })
    return report

# Example Input:
branches = ["Tel Aviv", "Jerusalem", "Haifa"]
balances_per_branch = [
    [5000, 7500, 10000],  # Balances for Tel Aviv
    [3000, 4000, 2000],   # Balances for Jerusalem
    [7000, 8000, 6000]    # Balances for Haifa
]
transactions_per_branch = [
    [10, 15, 20],  # Transactions for Tel Aviv
    [8, 12, 10],   # Transactions for Jerusalem
    [5, 8, 7]      # Transactions for Haifa
]

# Example Output:
print("Financial report:", generate_financial_report(branches, balances_per_branch, transactions_per_branch))
res = generate_financial_report(branches, balances_per_branch, transactions_per_branch)
for i in res:
    print(i)
# Output:
# Financial report: [
#   {'branch': 'Tel Aviv', 'total_balance': 22500, 'average_transaction_amount': 562.5},
#   {'branch': 'Jerusalem', 'total_balance': 9000, 'average_transaction_amount': 391.3},
#   {'branch': 'Haifa', 'total_balance': 21000, 'average_transaction_amount': 1000.0}
# ]