# Topic Recap: reduce() (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Sum of a List
# Explanation: Write a function `sum_list` that takes a list of numbers and returns their sum using the `reduce()` function from the `functools` module.
# Solution:
from functools import reduce

def sum_list(numbers):
    return reduce(lambda x, y: x + y, numbers)

# Example Input:
numbers = [1, 2, 3, 4, 5]
total_sum = sum_list(numbers)
print(f"Sum of the list: {total_sum}")

# Example Output:
# Sum of the list: 15


# Exercise 2 (Easy): Concatenate Strings
# Explanation: Write a function `concatenate_strings` that takes a list of strings and returns a single string where all the input strings are concatenated using `reduce()`.
# Solution:
def concatenate_strings(strings):
    return reduce(lambda x, y: x + y, strings)

# Example Input:
strings = ["Data", "Science", "is", "fun"]
result = concatenate_strings(strings)
print(f"Concatenated String: {result}")

# Example Output:
# Concatenated String: DataScienceisfun


# Exercise 3 (Easy): Product of List Elements
# Explanation: Write a function `product_of_elements` that takes a list of numbers and returns their product using `reduce()`.
# Solution:
def product_of_elements(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example Input:
numbers = [1, 2, 3, 4]
product = product_of_elements(numbers)
print(f"Product of the list: {product}")

# Example Output:
# Product of the list: 24


# 2 Medium Exercises

# Exercise 4 (Medium): Find Maximum Value
# Explanation: Write a function `find_maximum` that takes a list of numbers and returns the maximum value using `reduce()`.
# Solution:
def find_maximum(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

# Example Input:
numbers = [3, 7, 2, 5, 10, 6]
max_value = find_maximum(numbers)
print(f"Maximum value in the list: {max_value}")

# Example Output:
# Maximum value in the list: 10


# Exercise 5 (Medium): Calculate Total Revenue
# Explanation: Write a function `calculate_revenue` that takes a list of tuples representing sales data (`product_name`, `units_sold`, `price_per_unit`) and returns the total revenue using `reduce()`.
# Solution:
def calculate_revenue(sales_data):
    return reduce(lambda total, item: total + item[1] * item[2], sales_data, 0)

# Example Input:
sales_data = [("Laptop", 5, 1000), ("Smartphone", 10, 800), ("Tablet", 3, 600)]
total_revenue = calculate_revenue(sales_data)
print(f"Total Revenue: ${total_revenue}")

# Example Output:
# Total Revenue: $15800


# 1 Hard Exercise

# Exercise 6 (Hard): Cumulative Product of Data Points
# Explanation: Write a function `cumulative_product` that takes a list of numbers and returns a new list where each element is the cumulative product up to that index using `reduce()` and `map()`.
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)
# Solution:
def cumulative_product(numbers):
    return list(reduce(lambda acc, x: acc + [acc[-1] * x], numbers[1:], [numbers[0]]))

# Example Input:
numbers = [1, 2, 3, 4]
cumulative_product_list = cumulative_product(numbers)
print(f"Cumulative Product List: {cumulative_product_list}")

# Example Output:
# Cumulative Product List: [1, 2, 6, 24]
