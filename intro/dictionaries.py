# Dictionary acts like in c#
# iterable, unordered, collection of KEY-VALUE pairs
# each key must be unique

# Creating a dictionary
# 1
student1 = {
    "name": "Avi",
    "age": 45,
    "course": "Python"
}

# 2
student2 = dict(name="Shubu", age=40, course="HTML")

print(student1)
print(student2)

# creating an empty dicitonary
#
dict1 = {}
dict2 = dict()

# access values:
# 1
print(student1["name"])
print(student2["age"])
# print(student2["bla"]) # error

# 2
print(student1.get("course"))
print(student1.get("bla"))
print(student1.get("bla", "N/A"))

# add or modify
print(student1)
student1["address"] = "Lod"
student1["age"] = 20
print(student1)

# delete from dictionary
course = student1.pop("course")
print(student1)
del student1["age"]
print(student1)

# num1 = 5
# num1 = 6
# print(num1)
# del num1
# print(num1)

for key in student1.keys():
    print(key)

for value in student1.values():
    print(value)

for key, value in student1.items():
    print(f"{key}: {value}")

person1 = {
    "name": "Avi",
    "age": 30
}

person2 = {
    # "name": "Oren",
    # "age": 35,
    "city": "Metula"
}

person1.update(person2)
print(person1)

person1.clear()
print(person1)

person2_copy = person2.copy()

# nested dictionaries

students = {
    "omer": {
        "age": 29,
        "grade": 0
    },
    "beni": {
        "age": 10,
        "grade": 97
    }
}

# print(students["beni"]["age"])
for student in students.values():
    for key, value in student.items():
        if key == "age":
            print(value)


# TASK!!!!
"""
Write a function count_frequencies, that gets a list of elements and returns a dictionary
containing the frequency of each element.
example:
input = [10, 20, 35, 14, 10, 20, 15, 17, 20]
output:
{
    10: 2,
    20: 3,
    35: 1
    ...
}
"""

def count_frequencies(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency



input1 = [10, 20, 35, 14, 10, 20, 15, 17, 20]
print(count_frequencies(input1))


def group_student_by_grade(students):
    grade_dict = {}
    for student, grade in students:
        grade_dict.setdefault(grade, []).append(student)
    return grade_dict



students = [["omer", 40],["avi", 50],["shlomi", 50],["aron", 25],["bodi", 80]]
print(group_student_by_grade(students))




# Task 1 (Easy): Calculate the Total Balance of Multiple Bank Accounts
# Explanation:
# Write a function `calculate_total_balance` that takes a dictionary representing multiple bank accounts
# and their respective balances. The dictionary's keys are the account numbers (strings), and the values
# are the balances (floats). The function should return the total balance of all accounts.


# Example Input:
# accounts = {
#     "123-456-789": 5000.50,
#     "987-654-321": 3200.75,
#     "111-222-333": 7600.10,
#     "444-555-666": 1500.00
# }

# Example Output:
# Output: Total balance: 17301.35

# ----------------------------------------------------------------------

# Task 2 (Medium): Track Monthly Expenses and Categorize by Type
# Explanation:
# Write a function `categorize_expenses` that takes a dictionary representing monthly expenses for different
# categories in an Israeli bank account. The keys of the dictionary are expense categories (e.g., "Groceries",
# "Utilities", "Entertainment"), and the values are lists of expenses (floats) in NIS for each category. The
# function should return a new dictionary that contains the total expenses for each category.



# Example Input:
# expenses = {
#     "Groceries": [150.75, 200.30, 125.50],
#     "Utilities": [300.00, 250.40],
#     "Entertainment": [100.00, 50.50, 75.75],
#     "Transportation": [60.00, 45.30]
# }

# Example Output:
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
# The function should calculate the remaining balance for each loan after a given number of months, assuming that payments are made
# at the end of each month and interest is compounded monthly. Return a new dictionary with loan IDs as keys and their corresponding
# remaining balances as values.



# Example Input:
# loans = {
#     "Loan1": {"principal": 100000, "annual_interest_rate": 3.5, "months": 24, "monthly_payment": 4500},
#     "Loan2": {"principal": 50000, "annual_interest_rate": 4.0, "months": 12, "monthly_payment": 4300},
#     "Loan3": {"principal": 75000, "annual_interest_rate": 5.5, "months": 36, "monthly_payment": 3200}
# }

# Example Output:
# Output: Remaining balances for each loan: {'Loan1': 48207.37, 'Loan2': 2873.97, 'Loan3': 50190.92}
