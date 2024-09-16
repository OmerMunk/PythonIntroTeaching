# Topic Recap: If, Elif, Else, Switch Case, And, Or, Not, Is, In

# 3 Easy Exercises

# Exercise 1 (Easy): Age Category Checker
# Explanation: Write a Python program that takes a user's age as input and determines which age category they fall into:
# - "Child" for age < 13
# - "Teenager" for age between 13 and 19
# - "Adult" for age >= 20
# Guidance: Use if-elif-else statements to check the age ranges.
# Solution:


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


# Example Input:
# Enter a username: JohnDoe
# Example Output:
# Valid username


# Exercise 3 (Easy): Check for Vowels in a String
# Explanation: Write a program that checks if a given input string contains any vowels (a, e, i, o, u).
# Guidance: Use a for loop and the `in` operator to check for vowels.
# Solution:


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


# Example Input:
# Enter the student's score (0-100): 85
# Example Output:
# Grade: B


# Exercise 5 (Medium): Banking Transaction Checker
# Explanation: Write a program that checks if a bank transaction can be processed. A transaction can only be processed if:
# - The amount is positive and not more than the current account balance.
# - The user is authenticated and is not flagged as a "suspicious user".
# Solution:


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


# Example Input:
# Enter the current salary: 4000
# Enter the performance level (excellent, good, average, poor): good
# Example Output:
# New Salary: 4200.00
