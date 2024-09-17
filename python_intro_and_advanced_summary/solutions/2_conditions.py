# Topic Recap: If, Elif, Else, Switch Case, And, Or, Not, Is, In

# 3 Easy Exercises

# Exercise 1 (Easy): Age Category Checker
# Explanation: Write a Python program that takes a user's age as input and determines which age category they fall into:
# - "Child" for age < 13
# - "Teenager" for age between 13 and 19
# - "Adult" for age >= 20
# Guidance: Use if-elif-else statements to check the age ranges.
# Solution:
age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")

# Example Input:
# Enter your age: 15
# Example Output:
# Category: Teenager


# Exercise 2 (Easy): Valid Username Checker
# Explanation: Write a program that checks if a username is valid. The username should:
# - Be between 5 and 15 characters long
# - Not contain spaces
# Guidance: Use if statements and the `in` operator to check for spaces.
# Solution:
username = input("Enter a username: ")

if 5 <= len(username) <= 15 and ' ' not in username:
    print("Valid username")
else:
    print("Invalid username")

# Example Input:
# Enter a username: JohnDoe
# Example Output:
# Valid username


# Exercise 3 (Easy): Check for Vowels in a String
# Explanation: Write a program that checks if a given input string contains any vowels (a, e, i, o, u).
# Guidance: Use a for loop and the `in` operator to check for vowels.
# Solution:
string = input("Enter a string: ").lower()
vowels = "aeiou"
contains_vowels = False

for char in string:
    if char in vowels:
        contains_vowels = True
        break

if contains_vowels:
    print("The string contains vowels.")
else:
    print("The string does not contain vowels.")

# Example Input:
# Enter a string: Hello
# Example Output:
# The string contains vowels.


# 2 Medium Exercises

# Exercise 4 (Medium): Simple Grading System
# Explanation: Write a program that takes a student's score (0-100) as input and outputs their grade based on the following:
# - "A" for 90-100
# - "B" for 80-89
# - "C" for 70-79
# - "D" for 60-69
# - "F" for below 60
# Solution:
score = int(input("Enter the student's score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Example Input:
# Enter the student's score (0-100): 85
# Example Output:
# Grade: B


# Exercise 5 (Medium): Banking Transaction Checker
# Explanation: Write a program that checks if a bank transaction can be processed. A transaction can only be processed if:
# - The amount is positive and not more than the current account balance.
# - The user is authenticated and is not flagged as a "suspicious user".
# Solution:
balance = 5000.00
user_authenticated = True
suspicious_user = False
transaction_amount = float(input("Enter the transaction amount: "))

if transaction_amount > 0 and transaction_amount <= balance and user_authenticated and not suspicious_user:
    print("Transaction approved.")
else:
    print("Transaction denied.")

# Example Input:
# Enter the transaction amount: 3000
# Example Output:
# Transaction approved.


# 1 Hard Exercise

# Exercise 6 (Hard): Employee Salary Adjustment System
# Explanation: Create a program that calculates an employee's new salary based on their performance and current salary. The program should:
# - Take the current salary and performance level ("excellent", "good", "average", "poor") as input.
# - Adjust the salary based on the performance:
#   - "excellent" -> +10% salary increase
#   - "good" -> +5% salary increase
#   - "average" -> no change
#   - "poor" -> -5% salary decrease
# - The program should use if-elif-else statements and a switch-case alternative (dictionary-based) for the performance-based logic.
# Solution:
current_salary = float(input("Enter the current salary: "))
performance = input("Enter the performance level (excellent, good, average, poor): ").lower()

# Dictionary-based switch-case alternative
adjustments = {
    "excellent": 1.10,
    "good": 1.05,
    "average": 1.00,
    "poor": 0.95
}

if performance in adjustments:
    new_salary = current_salary * adjustments[performance]
    print(f"New Salary: {new_salary:.2f}")
else:
    print("Invalid performance level.")

# Example Input:
# Enter the current salary: 4000
# Enter the performance level (excellent, good, average, poor): good
# Example Output:
# New Salary: 4200.00
