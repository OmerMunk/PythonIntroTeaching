# Topic Recap: try, except, raise, Exception Handling, Different Exception Types, Multiple Exceptions (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Basic try-except Block
# Explanation: Write a function `divide_numbers` that takes two numbers and divides them. Use a `try-except` block to handle a `ZeroDivisionError` if the divisor is zero.
# Solution:
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Example Input:
divide_numbers(10, 0)

# Example Output:
# Error: Cannot divide by zero!


# Exercise 2 (Easy): Handle Multiple Exceptions
# Explanation: Write a function `parse_integer` that takes a string input and tries to convert it to an integer. Handle `ValueError` if the input is not a valid integer and `TypeError` if the input is not a string.
# Solution:
def parse_integer(input_string):
    try:
        result = int(input_string)
        print(f"Parsed Integer: {result}")
    except ValueError:
        print("Error: Invalid integer format!")
    except TypeError:
        print("Error: Input must be a string!")

# Example Input:
parse_integer("abc")

# Example Output:
# Error: Invalid integer format!


# Exercise 3 (Easy): Raising Custom Exceptions
# Explanation: Write a function `check_age` that raises a `ValueError` if the input age is less than 0.
# Solution:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age: {age}")

# Example Input:
try:
    check_age(-5)
except ValueError as e:
    print(e)

# Example Output:
# Age cannot be negative!


# 2 Medium Exercises

# Exercise 4 (Medium): Multiple Exceptions in One Block
# Explanation: Write a function `read_file` that takes a filename as input and tries to open and read it. Handle `FileNotFoundError` if the file does not exist and `PermissionError` if the file is not accessible.
# Solution:
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")

# Example Input:
read_file("non_existent_file.txt")

# Example Output:
# Error: File not found!


# Exercise 5 (Medium): Using finally with try-except
# Explanation: Write a function `calculate_average` that takes a list of numbers and returns the average. Use `try-except-finally` to handle `ZeroDivisionError` and ensure a cleanup message is printed in the `finally` block.
# Solution:
def calculate_average(numbers):
    try:
        avg = sum(numbers) / len(numbers)
        print(f"Average: {avg}")
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list!")
    finally:
        print("Calculation attempt completed.")

# Example Input:
calculate_average([])

# Example Output:
# Error: Cannot calculate average of an empty list!
# Calculation attempt completed.


# 1 Hard Exercise

# Exercise 6 (Hard): Handling Multiple Exceptions and Raising Custom Exceptions
# Explanation: Write a function `process_data` that takes a list of data entries. For each entry, try to:
# 1. Convert the entry to an integer.
# 2. Check if the integer is positive.
# If the conversion fails, handle `ValueError` and raise a custom `DataFormatError`. If the value is negative, raise a `NegativeValueError`.
# Solution:
class DataFormatError(Exception):
    pass

class NegativeValueError(Exception):
    pass

def process_data(data_entries):
    for entry in data_entries:
        try:
            value = int(entry)
            if value < 0:
                raise NegativeValueError(f"Negative value found: {value}")
            print(f"Processed value: {value}")
        except ValueError:
            raise DataFormatError(f"Invalid data format: {entry}")
        except NegativeValueError as e:
            print(e)

# Example Input:
try:
    process_data(["10", "-5", "abc", "20"])
except DataFormatError as e:
    print(e)

# Example Output:
# Processed value: 10
# Negative value found: -5
# Invalid data format: abc
# Processed value: 20
