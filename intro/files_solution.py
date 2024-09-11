# Task 1 (Easy): Write and Read Bank Account Details
# Explanation:
# Write a function `write_and_read_accounts` that writes a list of bank account details (account number and balance)
# to a text file named `accounts.txt`. Each account detail should be written in a new line in the format:
# "Account Number: [account_number], Balance: [balance]". Then, the function should read the contents of the file
# and print them.

def write_and_read_accounts(accounts):
    # Write account details to a file
    with open('accounts.txt', 'w') as file:
        for account in accounts:
            file.write(f"Account Number: {account[0]}, Balance: {account[1]}\n")

    # Read the contents of the file
    with open('accounts.txt', 'r') as file:
        content = file.read()
        print(content)

# Example Input:
accounts = [
    ("123-456-789", 5000.0),
    ("987-654-321", 7500.5),
    ("111-222-333", 12000.75)
]

# Example Output:
write_and_read_accounts(accounts)
# Output:
# Account Number: 123-456-789, Balance: 5000.0
# Account Number: 987-654-321, Balance: 7500.5
# Account Number: 111-222-333, Balance: 12000.75

# ----------------------------------------------------------------------

# Task 2 (Medium): Update Balances in a File
# Explanation:
# Write a function `update_balances` that reads a text file `balances.txt` containing account numbers and balances
# (each line in the format: "account_number,balance"). The function should add a specified amount to all account
# balances in the file and then write the updated balances back to the file.

def update_balances(amount_to_add):
    # Read the file and update the balances
    with open('balances.txt', 'r') as file:
        lines = file.readlines()

    # Update balances
    updated_lines = []
    for line in lines:
        account_number, balance = line.strip().split(',')
        new_balance = float(balance) + amount_to_add
        updated_lines.append(f"{account_number},{new_balance:.2f}\n")

    # Write the updated balances back to the file
    with open('balances.txt', 'w') as file:
        file.writelines(updated_lines)

# Example Input:
# balances.txt content before:
# 123-456-789,5000.0
# 987-654-321,7500.5
# 111-222-333,12000.75

update_balances(500.0)

# Example Output:
# balances.txt content after:
# 123-456-789,5500.0
# 987-654-321,8000.5
# 111-222-333,12500.75

# ----------------------------------------------------------------------

# Task 3 (Hard): Merge and Summarize Transaction Files
# Explanation:
# Write a function `merge_and_summarize_transactions` that takes a list of file names, where each file contains
# transaction details for different branches of an Israeli bank. Each file has lines in the format:
# "transaction_id,account_number,amount". The function should merge all the transactions into a single file
# named `merged_transactions.txt` and calculate the total amount for each account, saving the summary in
# `account_summaries.txt` in the format: "account_number,total_amount".

def merge_and_summarize_transactions(file_names):
    # Dictionary to store total amount per account
    account_totals = {}

    # Merge all transactions into a single file
    with open('merged_transactions.txt', 'w') as merged_file:
        for file_name in file_names:
            with open(file_name, 'r') as file:
                for line in file:
                    merged_file.write(line)
                    transaction_id, account_number, amount = line.strip().split(',')
                    amount = float(amount)
                    # Update total for each account
                    if account_number in account_totals:
                        account_totals[account_number] += amount
                    else:
                        account_totals[account_number] = amount

    # Write the summary to a file
    with open('account_summaries.txt', 'w') as summary_file:
        for account_number, total_amount in account_totals.items():
            summary_file.write(f"{account_number},{total_amount:.2f}\n")

# Example Input:
# transactions_branch1.txt content:
# T001,123-456-789,1000.0
# T002,987-654-321,2000.0
#
# transactions_branch2.txt content:
# T003,123-456-789,500.0
# T004,111-222-333,750.0

file_names = ['transactions_branch1.txt', 'transactions_branch2.txt']

merge_and_summarize_transactions(file_names)

# Example Output:
# merged_transactions.txt content:
# T001,123-456-789,1000.0
# T002,987-654-321,2000.0
# T003,123-456-789,500.0
# T004,111-222-333,750.0
#
# account_summaries.txt content:
# 123-456-789,1500.0
# 987-654-321,2000.0
# 111-222-333,750.0