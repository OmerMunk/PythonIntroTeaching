# Topic Recap: Magic Methods and Magic Keywords (Data Engineering Oriented)

# Magic methods (also known as "dunder" methods) in Python are special methods that are surrounded by double underscores (e.g., __init__, __str__) and allow developers to define or customize the behavior of Python objects.
# Magic keywords in Python include special keywords like `self`, `cls`, `@property`, `@staticmethod`, etc.

# 3 Easy Exercises

# Exercise 1 (Easy): Implement __str__ Method
# Explanation: Write a class `Employee` with attributes `name` and `role`. Implement the `__str__` method to provide a readable string representation of the object.
# Solution:


# Example Input:
employee = Employee("Alice", "Data Engineer")
print(employee)

# Example Output:
# Employee(Name: Alice, Role: Data Engineer)


# Exercise 2 (Easy): Implement __len__ Method
# Explanation: Write a class `DataList` that wraps around a list. Implement the `__len__` method to return the length of the list.
# Solution:

# Example Input:
data_list = DataList([1, 2, 3, 4, 5])
print(f"Length of DataList: {len(data_list)}")

# Example Output:
# Length of DataList: 5


# Exercise 3 (Easy): Implement __eq__ Method
# Explanation: Write a class `Product` with attributes `name` and `price`. Implement the `__eq__` method to compare two product objects based on their names and prices.
# Solution:


# Example Input:
product1 = Product("Laptop", 1000)
product2 = Product("Laptop", 1000)
product3 = Product("Phone", 800)
print(product1 == product2)  # True
print(product1 == product3)  # False

# Example Output:
# True
# False


# 2 Medium Exercises

# Exercise 4 (Medium): Implement __getitem__ and __setitem__ Methods
# Explanation: Write a class `CustomList` that wraps around a list. Implement the `__getitem__` and `__setitem__` methods to allow getting and setting list elements using square bracket notation.
# Solution:


# Example Input:
custom_list = CustomList([10, 20, 30])
print(custom_list[1])  # Accessing using __getitem__
custom_list[1] = 25   # Modifying using __setitem__
print(custom_list[1])

# Example Output:
# 20
# 25


# Exercise 5 (Medium): Implement __iter__ and __next__ for Custom Iterator
# Explanation: Write a class `SquareNumbers` that implements an iterator to generate squares of numbers up to a limit. Use the `__iter__` and `__next__` methods.
# Solution:


# Example Input:
squares = SquareNumbers(3)
for num in squares:
    print(num)

# Example Output:
# 0
# 1
# 4
# 9


# 1 Hard Exercise

# Exercise 6 (Hard): Implement Multiple Magic Methods for a Data Class
# Explanation: Write a class `Vector` representing a mathematical vector with x and y coordinates. Implement the following magic methods:
# - `__init__`: Initialize the vector.
# - `__add__`: Add two vectors.
# - `__sub__`: Subtract two vectors.
# - `__mul__`: Multiply a vector by a scalar.
# - `__str__`: Provide a readable string representation.
# - `__repr__`: Provide an unambiguous string representation for debugging.
# Solution:


# Example Input:
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 3
print(v3)
print(v4)
print(v5)
print(repr(v5))

# Example Output:
# Vector(4, 6)
# Vector(2, 2)
# Vector(3, 6)
# Vector(x=3, y=6)
