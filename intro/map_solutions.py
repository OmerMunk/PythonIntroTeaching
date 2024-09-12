# Task 1 (Easy): Convert Amounts from NIS to USD
# Explanation:
# Write a function `convert_to_usd` that takes a list of transaction amounts in NIS (New Israeli Shekel)
# and converts them to USD using a fixed exchange rate of 1 NIS = 0.27 USD. Use `map()` to apply the conversion
# to all amounts in the list and return a list of amounts in USD.

def convert_to_usd(amounts_nis):
    # Define the conversion rate
    exchange_rate = 0.27
    # Use map to apply the conversion to each amount in the list
    amounts_usd = list(map(lambda x: round(x * exchange_rate, 2), amounts_nis))
    return amounts_usd

# Example Input:
amounts_nis = [100, 250, 1500, 7500]

# Example Output:
print("Amounts in USD:", convert_to_usd(amounts_nis))
# Output: Amounts in USD: [27.0, 67.5, 405.0, 2025.0]

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate Monthly Interest for Savings Accounts
# Explanation:
# Write a function `calculate_monthly_interest` that takes a dictionary representing customer savings accounts,
# where each key is the account number (str) and the value is a tuple containing the _balance (float) and annual
# interest rate (float, in %). Use `map()` to calculate the monthly interest for each account and return a list
# of tuples containing the account number and its calculated monthly interest.

def calculate_monthly_interest(accounts):
    # Define a function to calculate monthly interest
    def calculate(account):
        balance, annual_rate = accounts[account]
        monthly_interest = (balance * (annual_rate / 100)) / 12
        return (account, round(monthly_interest, 2))

    # Use map to apply the interest calculation to each account
    monthly_interests = list(map(calculate, accounts))
    return monthly_interests

# Example Input:
accounts = {
    "123-456-789": (10000, 3.5),
    "987-654-321": (20000, 2.0),
    "111-222-333": (15000, 4.0),
}

# Example Output:
print("Monthly interest for each account:", calculate_monthly_interest(accounts))
# Output: Monthly interest for each account: [('123-456-789', 29.17), ('987-654-321', 33.33), ('111-222-333', 50.0)]

# ----------------------------------------------------------------------

# Task 3 (Hard): Apply a Custom Fee to Transactions Based on Conditions
# Explanation:
# Write a function `apply_custom_fee` that takes a list of dictionaries representing transactions,
# where each dictionary contains "id" (str), "amount" (float), and "type" (str - "domestic" or "international").
# Apply a custom fee:
# - For "domestic" transactions, apply a 1% fee.
# - For "international" transactions, apply a 3% fee.
# Use `map()` to update the amount after the fee is applied, and return a list of transactions with updated amounts.

def apply_custom_fee(transactions):
    # Define a function to calculate the new amount with the fee
    def calculate_fee(transaction):
        if transaction["type"] == "domestic":
            fee = 0.01
        elif transaction["type"] == "international":
            fee = 0.03
        else:
            fee = 0  # No fee for unknown type
        # Apply the fee to the amount
        transaction["amount"] = round(transaction["amount"] * (1 - fee), 2)
        return transaction

    # Use map to apply the fee calculation to each transaction
    updated_transactions = list(map(calculate_fee, transactions))
    return updated_transactions

# Example Input:
transactions = [
    {"id": "T001", "amount": 1000.0, "type": "domestic"},
    {"id": "T002", "amount": 2000.0, "type": "international"},
    {"id": "T003", "amount": 1500.0, "type": "domestic"},
    {"id": "T004", "amount": 5000.0, "type": "international"},
]

# Example Output:
print("Transactions after applying fees:", apply_custom_fee(transactions))
# Output: Transactions after applying fees: [{'id': 'T001', 'amount': 990.0, 'type': 'domestic'}, {'id': 'T002', 'amount': 1940.0, 'type': 'international'}, {'id': 'T003', 'amount': 1485.0, 'type': 'domestic'}, {'id': 'T004', 'amount': 4850.0, 'type': 'international'}]