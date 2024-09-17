# Topic Recap: Match Case, Nested And/Or

# 3 Easy Exercises

# Exercise 1 (Easy): Day of the Week
# Explanation: Write a Python program that takes a number (1-7) as input and outputs the corresponding day of the week (1: Monday, 2: Tuesday, etc.) using `match case`.
# Guidance: Use the `match case` statement to match the input number to the correct day.
# Solution:
day_number = int(input("Enter a number (1-7) representing the day of the week: "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number")

# Example Input:
# Enter a number (1-7) representing the day of the week: 3
# Example Output:
# Wednesday


# Exercise 2 (Easy): Simple Fruit Checker
# Explanation: Write a Python program that takes a fruit name as input and checks if it is a "Citrus" (orange, lemon, lime) or "Berry" (strawberry, blueberry, raspberry) using `match case`.
# Guidance: Use `match case` to categorize the fruit.
# Solution:
fruit = input("Enter the name of a fruit: ").lower()

match fruit:
    case "orange" | "lemon" | "lime":
        print("Citrus")
    case "strawberry" | "blueberry" | "raspberry":
        print("Berry")
    case _:
        print("Unknown category")

# Example Input:
# Enter the name of a fruit: Lemon
# Example Output:
# Citrus


# Exercise 3 (Easy): Grade Feedback
# Explanation: Write a Python program that takes a letter grade (A, B, C, D, F) as input and provides feedback ("Excellent", "Good", "Fair", "Poor", "Fail") using `match case`.
# Guidance: Use `match case` to match the grade to the feedback.
# Solution:
grade = input("Enter a letter grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Fair")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")

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
role = input("Enter your role (Admin, Moderator, User, Guest): ").capitalize()

match role:
    case "Admin":
        print("Full Access")
    case "Moderator":
        print("Moderate Content")
    case "User":
        print("View Content")
    case "Guest":
        print("Limited Access")
    case _:
        print("Invalid Role")

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
customer_type = input("Enter customer type (Regular, Premium, VIP): ").capitalize()
purchase_amount = float(input("Enter purchase amount: "))

discount = 0
if customer_type == "Regular" and purchase_amount > 100:
    discount = 0.05 * purchase_amount
elif customer_type == "Premium" and purchase_amount > 100:
    discount = 0.10 * purchase_amount
elif customer_type == "VIP" and purchase_amount > 100:
    discount = 0.15 * purchase_amount
    if purchase_amount > 500:
        discount += 0.05 * purchase_amount

print(f"Discount: ${discount:.2f}")

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
employee_level = input("Enter employee level (Junior, Mid, Senior): ").capitalize()
base_salary = float(input("Enter base salary: "))
hours_worked = int(input("Enter hours worked in the month: "))

# Match case for tax rate
match employee_level:
    case "Junior":
        tax_rate = 0.10
    case "Mid":
        tax_rate = 0.15
    case "Senior":
        tax_rate = 0.20
    case _:
        print("Invalid employee level.")
        exit()

# Calculate net salary after tax
net_salary = base_salary * (1 - tax_rate)

# Calculate bonus using nested conditions
if hours_worked > 160:
    bonus = base_salary * 0.05
    if hours_worked > 200:
        bonus += base_salary * 0.10
    net_salary += bonus

print(f"Net Salary after deductions and bonuses: ${net_salary:.2f}")

# Example Input:
# Enter employee level (Junior, Mid, Senior): Senior
# Enter base salary: 4000
# Enter hours worked in the month: 210
# Example Output:
# Net Salary after deductions and bonuses: $4240.00
