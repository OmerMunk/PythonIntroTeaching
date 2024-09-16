# Topic Recap: Match Case, Nested And/Or

# 3 Easy Exercises

# Exercise 1 (Easy): Day of the Week
# Explanation: Write a Python program that takes a number (1-7) as input and outputs the corresponding day of the week (1: Monday, 2: Tuesday, etc.) using `match case`.
# Guidance: Use the `match case` statement to match the input number to the correct day.
# Solution:


# Example Input:
# Enter a number (1-7) representing the day of the week: 3
# Example Output:
# Wednesday


# Exercise 2 (Easy): Simple Fruit Checker
# Explanation: Write a Python program that takes a fruit name as input and checks if it is a "Citrus" (orange, lemon, lime) or "Berry" (strawberry, blueberry, raspberry) using `match case`.
# Guidance: Use `match case` to categorize the fruit.
# Solution:


# Example Input:
# Enter the name of a fruit: Lemon
# Example Output:
# Citrus


# Exercise 3 (Easy): Grade Feedback
# Explanation: Write a Python program that takes a letter grade (A, B, C, D, F) as input and provides feedback ("Excellent", "Good", "Fair", "Poor", "Fail") using `match case`.
# Guidance: Use `match case` to match the grade to the feedback.
# Solution:


# Example Input:
# Enter a letter grade (A, B, C, D, F): B
# Example Output:
# Good


# 2 Medium Exercises

# Exercise 4 (Medium): Role-Based Access Control
# Explanation: Write a program that takes a user's role (Admin, Moderator, User, Guest) as input and grants permissions based on the role using `match case`. Permissions are:
# - "Admin": Full Access
# - "Moderator": Moderate Content
# - "User": View Content
# - "Guest": Limited Access
# Solution:


# Example Input:
# Enter your role (Admin, Moderator, User, Guest): Moderator
# Example Output:
# Moderate Content


# Exercise 5 (Medium): Multi-Level Discount System
# Explanation: Write a program that calculates a discount based on purchase amount and customer type using nested `and/or` logic.
# - "Regular": 5% discount for amounts over $100
# - "Premium": 10% discount for amounts over $100
# - "VIP": 15% discount for amounts over $100 and additional 5% if amount is over $500
# Solution:


# Example Input:
# Enter customer type (Regular, Premium, VIP): VIP
# Enter purchase amount: 600
# Example Output:
# Discount: $120.00


# 1 Hard Exercise

# Exercise 6 (Hard): Advanced Salary Deduction Calculator
# Explanation: Create a program that calculates an employee's net salary after tax deductions and bonuses based on the following:
# - Use a `match case` to determine the tax rate:
#   - "Junior": 10%
#   - "Mid": 15%
#   - "Senior": 20%
# - Use nested `and/or` logic to determine bonuses:
#   - Employee must work more than 160 hours/month to qualify.
#   - Employees with more than 200 hours/month get an additional bonus.
# - The program should take inputs for the employee level, base salary, and hours worked.
# Solution:


# Example Input:
# Enter employee level (Junior, Mid, Senior): Senior
# Enter base salary: 4000
# Enter hours worked in the month: 210
# Example Output:
# Net Salary after deductions and bonuses: $4240.00
