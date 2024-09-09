# working with files

# open and close file
# file flags:
"""
r - read
w - write
a - append
r+ - read and write
"""

import os
import json

file_path = 'data.txt'
# open the file
file = open(file_path, 'r')

# closing
file.close()

#

with open(file_path, 'r') as f:
    print("opened the file")
    pass
    pass
    pass
    pass
    pass
    print("closing the file")

print("the file is closed")

try:
    pass
except:
    pass

print("23123")

with open(file_path, 'r') as file:
    # read the entire file
    content = file.read()
    print(content)

    print('-' * 100)
    # move to the start of the file
    file.seek(0)
    # read part
    part_of_content = file.read(10)
    print(part_of_content)
    print('-' * 100)
    part_of_content = file.read(10)
    print(part_of_content)

    # read one line at a time
    file.seek(0)
    line = file.readline()
    while line:
        print(f"line is: {line}")
        line = file.readline()

    # read all lline to a list
    file.seek(0)
    lines = file.readlines()
    print(lines)

exit(1)
output_path = 'output.txt'
with open(output_path, 'w') as file:
    file.write("This is the first line.\n")
    file.write("another line.\n")

people = [("avi", 40), ('john', 35), ('beni', 10)]
with open('people.csv', 'w') as file:
    columns = ["name", "age"]
    first_line = ",".join(columns)
    file.write(f'{first_line}\n')
    for person in people:
        file.write(f'{person[0]},{person[1]}\n')
    # for name, age in people:
    #     file.write(f'{name},{age}\n')


with open('people.csv', 'a') as file:
    new_people = [("Omer", 29)]
    for person in new_people:
        file.write(f'{person[0]},{person[1]}\n')

exit(1)

# delete file

file_name_to_delete = 'people1.csv'
if os.path.exists(file_name_to_delete):
    os.remove(file_name_to_delete)
    print(f"deleted {file_name_to_delete}")
else:
    print(f"file {file_name_to_delete} does not exist")

# working with json:
people = {
    "person1": {
        "name": "avi",
        "money": -500
    },
    "person2": {
        "name": "davi",
        "money": 1_000_000
    }
}

list_people = [
    {
        "name": "avi",
        "money": -500
    },
    {
        "name": "davi",
        "money": 1_000_000
    }
]
with open('people.json', 'w') as file:
    json.dump(list_people, file)

# with open('people.json', 'r') as file:
#     people = json.load(file)
#     print(people)
#     print(type(people))
#
# people.update({"person3": {
#     "name": "shubulu",
#     "money": -100
# }})
# people.update({"person4": [1, 2, 3]})
#
# with open('people.json', 'w') as file:
#     json.dump(people, file)


# Task 1 (Easy): Write and Read Bank Account Details
# Explanation:
# Write a function `write_and_read_accounts` that writes a list of bank account details (account number and balance)
# to a text file named `accounts.txt`. Each account detail should be written in a new line in the format:
# "Account Number: [account_number], Balance: [balance]". Then, the function should read the contents of the file
# and print them.


# Example Input:
# accounts = [
#     ("123-456-789", 5000.0),
#     ("987-654-321", 7500.5),
#     ("111-222-333", 12000.75)
# ]

# Example Output:
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


# Example Input:
# balances.txt content before:
# 123-456-789,5000.0
# 987-654-321,7500.5
# 111-222-333,12000.75


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


# Example Input:
# transactions_branch1.txt content:
# T001,123-456-789,1000.0
# T002,987-654-321,2000.0
#
# transactions_branch2.txt content:
# T003,123-456-789,500.0
# T004,111-222-333,750.0

# file_names = ['transactions_branch1.txt', 'transactions_branch2.txt']


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
