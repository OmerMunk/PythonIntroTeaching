# Topic Recap: Variables, Numbers, Math, Strings, Input/Output, Operators, Booleans, Casting

# 3 Easy Exercises

# Exercise 1 (Easy): Variable and String Manipulation
# Explanation: Write a Python program that takes a user's first name and last name as input, then concatenates them into a full name with proper capitalization and prints it.
# Guidance: Use `input()` to receive the user's input, and use string methods like `capitalize()` or `title()` to format the names correctly.
# Solution:
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
full_name = first_name.capitalize() + " " + last_name.capitalize()
print(f"Full Name: {full_name}")

# Example Input:
# first_name: john
# last_name: doe
# Example Output:
# Full Name: John Doe


# Exercise 2 (Easy): Basic Math Operations
# Explanation: Create a program that asks the user for two numbers and prints the sum, difference, product, and quotient.
# Guidance: Use `input()` to take user input, convert the input to integers or floats using `int()` or `float()`, and use basic math operators (`+`, `-`, `*`, `/`).
# Solution:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2 if num2 != 0 else 'Undefined (division by zero)'}")

# Example Input:
# Enter first number: 8
# Enter second number: 4
# Example Output:
# Sum: 12.0
# Difference: 4.0
# Product: 32.0
# Quotient: 2.0


# Exercise 3 (Easy): Boolean and Comparison Operators
# Explanation: Write a Python program that takes two numbers as input and checks whether the first number is greater than, less than, or equal to the second number.
# Guidance: Use comparison operators (`>`, `<`, `==`) and `print()` statements to display the results.
# Solution:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Is {num1} greater than {num2}? {num1 > num2}")
print(f"Is {num1} less than {num2}? {num1 < num2}")
print(f"Is {num1} equal to {num2}? {num1 == num2}")

# Example Input:
# Enter first number: 7
# Enter second number: 10
# Example Output:
# Is 7.0 greater than 10.0? False
# Is 7.0 less than 10.0? True
# Is 7.0 equal to 10.0? False


# 2 Medium Exercises

# Exercise 4 (Medium): Temperature Conversion
# Explanation: Write a Python program that takes a temperature in Celsius from the user and converts it to Fahrenheit and Kelvin.
# Solution:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
print(f"Temperature in Kelvin: {kelvin:.2f}")

# Example Input:
# Enter temperature in Celsius: 25
# Example Output:
# Temperature in Fahrenheit: 77.00
# Temperature in Kelvin: 298.15


# Exercise 5 (Medium): Simple Interest Calculator
# Explanation: Create a program that calculates the simple interest for a given principal amount, interest rate, and time period (in years).
# Solution:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
interest = (principal * rate * time) / 100
print(f"Simple Interest: {interest:.2f}")

# Example Input:
# Enter the principal amount: 1000
# Enter the annual interest rate (in %): 5
# Enter the time period (in years): 2
# Example Output:
# Simple Interest: 100.00


# 1 Hard Exercise

# Exercise 6 (Hard): Financial Report Formatter
# Explanation: Write a Python program that takes a user's income and expenses for the past month (as multiple inputs) and calculates the total income, total expenses, and net savings. The program should then print a formatted report showing all these values.
# Solution:
incomes = []
expenses = []

# Getting inputs from the user
num_incomes = int(input("Enter the number of income entries: "))
for i in range(num_incomes):
    income = float(input(f"Enter income #{i + 1}: "))
    incomes.append(income)

num_expenses = int(input("Enter the number of expense entries: "))
for i in range(num_expenses):
    expense = float(input(f"Enter expense #{i + 1}: "))
    expenses.append(expense)

# Calculating totals and net savings
total_income = sum(incomes)
total_expenses = sum(expenses)
net_savings = total_income - total_expenses

# Displaying the financial report
print("\n--- Financial Report ---")
print(f"Total Income: {total_income:.2f}")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Net Savings: {net_savings:.2f}")

# Example Input:
# Enter the number of income entries: 3
# Enter income #1: 5000
# Enter income #2: 2000
# Enter income #3: 1500
# Enter the number of expense entries: 2
# Enter expense #1: 3000
# Enter expense #2: 1200
# Example Output:
# --- Financial Report ---
# Total Income: 8500.00
# Total Expenses: 4200.00
# Net Savings: 4300.00
