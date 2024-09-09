# map

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)



ages = [16, 19, 20, 21, 14, 14, 18, 16, 17, 17, 16, 18, 20, 21, 21, 23, 22]
# result needed: can drink alcohol in israel only (21 >age >= 18)
# result needed: can drink alcohol in israel and us (age >= 21)
# result needed: cant drink alcohol(age < 18)

"""
person number 1 can drink alcohol in israel only
person number 2 can drink alcohol in israel and us
...
"""
MIN_AGE_ALCOHOL_US: int = 21
MIN_AGE_ALCOHOL_ISRAEL: int = 18

def alcohol_state(age: int) -> str:
    if MIN_AGE_ALCOHOL_US > age >= MIN_AGE_ALCOHOL_ISRAEL:
        return "can drink alcohol in israel only"
    elif age >= MIN_AGE_ALCOHOL_US:
        return "can drink alcohol in israel and us"
    else:
        return "cant drink alcohol"

results: list = list(map(alcohol_state ,ages))
# for i in range(len(results)):
#     print(f"person {i +1} {results[i]}")

for i, result in enumerate(results):
    print(f"person {i + 1} {result}")





# Task 1 (Easy): Convert Amounts from NIS to USD
# Explanation:
# Write a function `convert_to_usd` that takes a list of transaction amounts in NIS (New Israeli Shekel)
# and converts them to USD using a fixed exchange rate of 1 NIS = 0.27 USD. Use `map()` to apply the conversion
# to all amounts in the list and return a list of amounts in USD.



# Example Input:
# amounts_nis = [100, 250, 1500, 7500]

# Example Output:
# Output: Amounts in USD: [27.0, 67.5, 405.0, 2025.0]

# ----------------------------------------------------------------------

# Task 2 (Medium): Calculate Monthly Interest for Savings Accounts
# Explanation:
# Write a function `calculate_monthly_interest` that takes a dictionary representing customer savings accounts,
# where each key is the account number (str) and the value is a tuple containing the balance (float) and annual
# interest rate (float, in %). Use `map()` to calculate the monthly interest for each account and return a list
# of tuples containing the account number and its calculated monthly interest.


# Example Input:
# accounts = {
#     "123-456-789": (10000, 3.5),
#     "987-654-321": (20000, 2.0),
#     "111-222-333": (15000, 4.0),
# }

# Example Output:
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



# Example Input:
# transactions = [
#     {"id": "T001", "amount": 1000.0, "type": "domestic"},
#     {"id": "T002", "amount": 2000.0, "type": "international"},
#     {"id": "T003", "amount": 1500.0, "type": "domestic"},
#     {"id": "T004", "amount": 5000.0, "type": "international"},
# ]

# Example Output:
# Output: Transactions after applying fees: [{'id': 'T001', 'amount': 990.0, 'type': 'domestic'}, {'id': 'T002', 'amount': 1940.0, 'type': 'international'}, {'id': 'T003', 'amount': 1485.0, 'type': 'domestic'}, {'id': 'T004', 'amount': 4850.0, 'type': 'international'}]






