numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functions import is_prime

# filter - to filter out or in just the things we want.

# filter to extract only the even numbers

# filter gets 2 params:
# function, iterable
# the function needs to be a function that returns true a false
# the iterable - an object that we can iterate on.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

vowels = ['a', 'e', 'i', 'o', 'u']
str1 = "Hello world"
filtered_with_no_vowels = filter(lambda x: x not in vowels, str1)
print(list(filtered_with_no_vowels))

# create a list with 10 names
# filter only the words with maximum length of 5
words = ["Abraha", "avi", "seth", "shlomo", "shalom", "gadi", "david", "dud"]
MAX_LENGTH = 5

short_words = list(filter(lambda word: len(word) <= MAX_LENGTH, words))

# filter all the prime numbers only, from 2 to 100
MIN_RANGE = 2
MAX_RANGE = 100
numbers = list(range(MIN_RANGE, MAX_RANGE + 1))

prime_numbers = list(filter(is_prime, numbers))

"aa".isalpha()


# filter out non-alphabetic characters form a string.
input_string = "Hi! I am the best soldier 78 in Kodcode, I killed Zbeydi@@@ 😇😇"
cleaned_string =  ''.join(filter(lambda x: x.isalpha(), input_string))
print(cleaned_string)
# exercise - include the " "


# Task 1 (Easy): Filter High-Value Bank Transactions
# Explanation:
# Write a function `filter_high_value_transactions` that takes a list of transactions as input, where each transaction is
# represented by a dictionary with keys "id" (transaction ID) and "amount" (transaction amount in NIS). The function should
# use `filter()` to return a list of all transactions with an amount greater than 1,000 NIS.



# Example Input:
# transactions = [
#     {"id": "T001", "amount": 500.0},
#     {"id": "T002", "amount": 1500.0},
#     {"id": "T003", "amount": 750.0},
#     {"id": "T004", "amount": 2000.0}
# ]

# Example Output:
# Output: High-value transactions: [{'id': 'T002', 'amount': 1500.0}, {'id': 'T004', 'amount': 2000.0}]

# ----------------------------------------------------------------------

# Task 2 (Medium): Filter Customers with Loans Above a Certain Interest Rate
# Explanation:
# Write a function `filter_high_interest_loans` that takes a dictionary representing customer loans, where each key is a
# customer name and the value is another dictionary with keys "loan_amount" (float) and "interest_rate" (float, in %). The
# function should use `filter()` to find and return a list of customer names with loans that have an interest rate above 5%.


# Example Input:
# customers = {
#     "Alice": {"loan_amount": 100000, "interest_rate": 3.5},
#     "Bob": {"loan_amount": 200000, "interest_rate": 6.5},
#     "Charlie": {"loan_amount": 150000, "interest_rate": 5.0},
#     "David": {"loan_amount": 180000, "interest_rate": 7.0}
# }

# Example Output:
# Output: Customers with high-interest loans: ['Bob', 'David']

# ----------------------------------------------------------------------

# Task 3 (Hard): Filter and Sort Bank Accounts Based on Minimum Balance and Account Type
# Explanation:
# Write a function `filter_and_sort_accounts` that takes a list of dictionaries, where each dictionary represents a bank
# account with keys "account_number" (str), "_balance" (float), and "account_type" (str - "savings" or "checking"). The function
# should first use `filter()` to find accounts with a _balance greater than 10,000 NIS and of type "savings". Then, it should
# sort the filtered accounts in descending order by _balance and return the sorted list.



# Example Input:
# accounts = [
#     {"account_number": "001", "_balance": 15000.0, "account_type": "savings"},
#     {"account_number": "002", "_balance": 8000.0, "account_type": "savings"},
#     {"account_number": "003", "_balance": 20000.0, "account_type": "checking"},
#     {"account_number": "004", "_balance": 30000.0, "account_type": "savings"},
#     {"account_number": "005", "_balance": 5000.0, "account_type": "checking"}
# ]

# Example Output:
# Output: Filtered and sorted accounts: [{'account_number': '004', '_balance': 30000.0, 'account_type': 'savings'}, {'account_number': '001', '_balance': 15000.0, 'account_type': 'savings'}]









