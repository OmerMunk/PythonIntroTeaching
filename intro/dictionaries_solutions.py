# Task 1 (Easy): Calculate the Total Balance of Multiple Bank Accounts
# Explanation:
# Write a function `calculate_total_balance` that takes a dictionary representing multiple bank accounts
# and their respective balances. The dictionary's keys are the account numbers (strings), and the values
# are the balances (floats). The function should return the total _balance of all accounts.

def calculate_total_balance(accounts):
    # Calculate the total _balance by summing all values in the dictionary
    total_balance = sum(accounts.values())
    return total_balance

# Example Input:
accounts = {
    "123-456-789": 5000.50,
    "987-654-321": 3200.75,
    "111-222-333": 7600.10,
    "444-555-666": 1500.00
}

# Example Output:
print("Total _balance:", calculate_total_balance(accounts))
# Output: Total _balance: 17301.35

# ----------------------------------------------------------------------

# Task 2 (Medium): Track Monthly Expenses and Categorize by Type
# Explanation:
# Write a function `categorize_expenses` that takes a dictionary representing monthly expenses for different
# categories in an Israeli bank account. The keys of the dictionary are expense categories (e.g., "Groceries",
# "Utilities", "Entertainment"), and the values are lists of expenses (floats) in NIS for each category. The
# function should return a new dictionary that contains the total expenses for each category.

def categorize_expenses(expenses):
    # Create a new dictionary to store total expenses by category
    total_expenses_by_category = {}
    # Iterate over each category and list of expenses
    for category, amounts in expenses.items():
        # Calculate the total for each category
        total_expenses_by_category[category] = sum(amounts)
    return total_expenses_by_category

# Example Input:
expenses = {
    "Groceries": [150.75, 200.30, 125.50],
    "Utilities": [300.00, 250.40],
    "Entertainment": [100.00, 50.50, 75.75],
    "Transportation": [60.00, 45.30]
}

# Example Output:
print("Total expenses by category:", categorize_expenses(expenses))
# Output: Total expenses by category: {'Groceries': 476.55, 'Utilities': 550.4, 'Entertainment': 226.25, 'Transportation': 105.3}

# ----------------------------------------------------------------------

# Task 3 (Hard): Simulate Loan Repayment Tracking with Interest Calculation
# Explanation:
# Write a function `track_loan_repayments` that takes a dictionary representing different loans for a customer in an Israeli bank.
# The dictionary keys are loan IDs (strings), and the values are another dictionary containing:
# - "principal": the principal amount of the loan (float).
# - "annual_interest_rate": the annual interest rate (float).
# - "months": the total number of months for repayment (integer).
# - "monthly_payment": the fixed monthly payment amount (float).
# The function should calculate the remaining _balance for each loan after a given number of months, assuming that payments are made
# at the end of each month and interest is compounded monthly. Return a new dictionary with loan IDs as keys and their corresponding
# remaining balances as values.

def track_loan_repayments(loans):
    # Dictionary to store remaining balances
    remaining_balances = {}
    # Iterate through each loan
    for loan_id, details in loans.items():
        principal = details["principal"]
        annual_interest_rate = details["annual_interest_rate"]
        months = details["months"]
        monthly_payment = details["monthly_payment"]
        # Calculate the monthly interest rate
        monthly_interest_rate = annual_interest_rate / (12 / 100)# 35 -->> 0.035  3.5 / 100
        # 1000 0.01  1000 * (1 + 0.01)
        # Calculate the remaining _balance using the formula
        remaining_balance = principal * ((1 + monthly_interest_rate) ** months) - monthly_payment * (((1 + monthly_interest_rate) ** months - 1) / monthly_interest_rate)
        # Store the rounded remaining _balance in the dictionary
        remaining_balances[loan_id] = round(remaining_balance, 2)
    return remaining_balances

# Example Input:
loans = {
    "Loan1": {"principal": 100000, "annual_interest_rate": 3.5, "months": 24, "monthly_payment": 4500},
    "Loan2": {"principal": 50000, "annual_interest_rate": 4.0, "months": 12, "monthly_payment": 4300},
    "Loan3": {"principal": 75000, "annual_interest_rate": 5.5, "months": 36, "monthly_payment": 3200}
}

# Example Output:
print("Remaining balances for each loan:", track_loan_repayments(loans))
# Output: Remaining balances for each loan: {'Loan1': 48207.37, 'Loan2': 2873.97, 'Loan3': 50190.92}