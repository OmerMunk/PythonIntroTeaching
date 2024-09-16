# Topic Recap: Lambdas (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Double Each Number
# Explanation: Write a function `double_numbers` that takes a list of numbers and returns a new list where each number is doubled using a lambda function and `map()`.
# Solution:


# Example Input:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = double_numbers(numbers)
print(f"Doubled Numbers: {doubled_numbers}")

# Example Output:
# Doubled Numbers: [2, 4, 6, 8, 10]


# Exercise 2 (Easy): Sort by Length
# Explanation: Write a function `sort_by_length` that takes a list of strings and returns a new list sorted by their length using a lambda function with `sorted()`.
# Solution:


# Example Input:
strings = ["Data", "Science", "Python", "AI"]
sorted_strings = sort_by_length(strings)
print(f"Sorted by Length: {sorted_strings}")

# Example Output:
# Sorted by Length: ['AI', 'Data', 'Python', 'Science']


# Exercise 3 (Easy): Filter Positive Numbers
# Explanation: Write a function `filter_positive` that takes a list of numbers and returns a new list containing only the positive numbers using a lambda function with `filter()`.
# Solution:


# Example Input:
numbers = [-5, 3, -1, 7, 0, -2]
positive_numbers = filter_positive(numbers)
print(f"Positive Numbers: {positive_numbers}")

# Example Output:
# Positive Numbers: [3, 7]


# 2 Medium Exercises

# Exercise 4 (Medium): Apply Custom Function to List of Dictionaries
# Explanation: Write a function `apply_custom_discount` that takes a list of dictionaries representing products (each with 'name' and 'price' keys) and a discount percentage. Use a lambda function to apply the discount to each product's price and return a new list with updated prices.
# Solution:


# Example Input:
products = [{'name': 'Laptop', 'price': 1200}, {'name': 'Smartphone', 'price': 800}, {'name': 'Tablet', 'price': 600}]
discount = 10
discounted_products = apply_custom_discount(products, discount)
print(f"Discounted Products: {discounted_products}")

# Example Output:
# Discounted Products: [{'name': 'Laptop', 'price': 1080.0}, {'name': 'Smartphone', 'price': 720.0}, {'name': 'Tablet', 'price': 540.0}]


# Exercise 5 (Medium): Sort Employees by Salary
# Explanation: Write a function `sort_employees_by_salary` that takes a list of dictionaries representing employees (each with 'name' and 'salary' keys) and returns a new list sorted by salary in ascending order using a lambda function.
# Solution:

# Example Input:
employees = [{'name': 'Alice', 'salary': 70000}, {'name': 'Bob', 'salary': 60000}, {'name': 'Charlie', 'salary': 80000}]
sorted_employees = sort_employees_by_salary(employees)
print(f"Employees Sorted by Salary: {sorted_employees}")

# Example Output:
# Employees Sorted by Salary: [{'name': 'Bob', 'salary': 60000}, {'name': 'Alice', 'salary': 70000}, {'name': 'Charlie', 'salary': 80000}]


# 1 Hard Exercise

# Exercise 6 (Hard): Group and Sum Sales by Product
# Explanation: Write a function `group_and_sum_sales` that takes a list of tuples representing sales transactions (`product_name`, `units_sold`) and returns a dictionary where the keys are product names and the values are the total units sold for each product.
# Use a lambda function with `reduce()` from `functools` to achieve this.
# Solution:
from functools import reduce



# Example Input:
transactions = [("Laptop", 5), ("Smartphone", 3), ("Laptop", 2), ("Tablet", 4), ("Smartphone", 2)]
total_sales = group_and_sum_sales(transactions)
print(f"Total Sales by Product: {total_sales}")

# Example Output:
# Total Sales by Product: {'Laptop': 7, 'Smartphone': 5, 'Tablet': 4}
