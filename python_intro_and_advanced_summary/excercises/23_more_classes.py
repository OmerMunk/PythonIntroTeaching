# Topic Recap: ABC (Abstract Base Class), Abstract Class, Class Method, Static Method, Inheritance (Data Engineering Oriented)

from abc import ABC, abstractmethod

# 3 Easy Exercises

# Exercise 1 (Easy): Define Abstract Base Class
# Explanation: Write an abstract base class `Shape` with an abstract method `area()`. Then, create two derived classes `Square` and `Circle` that implement the `area()` method.
# Solution:

# Example Input:
square = Square(4)
circle = Circle(3)
print(f"Area of Square: {square.area()}")
print(f"Area of Circle: {circle.area()}")

# Example Output:
# Area of Square: 16
# Area of Circle: 28.26


# Exercise 2 (Easy): Class Method
# Explanation: Write a class `Counter` with a class attribute `count` and a class method `increment` that increases the count by a given value.
# Solution:


# Example Input:
Counter.increment(5)
Counter.increment(3)
print(f"Current Count: {Counter.count}")

# Example Output:
# Current Count: 8


# Exercise 3 (Easy): Static Method
# Explanation: Write a class `MathOperations` with a static method `add` that takes two numbers and returns their sum.
# Solution:


# Example Input:
result = MathOperations.add(5, 7)
print(f"Sum: {result}")

# Example Output:
# Sum: 12


# 2 Medium Exercises

# Exercise 4 (Medium): Abstract Class with Class Method
# Explanation: Write an abstract class `Employee` with a class method `from_string` that creates an instance from a string (formatted as "name,department").
# Implement a subclass `DataEngineer` that inherits from `Employee` and adds an attribute `tools`.
# Solution:


# Example Input:
employee_data = "Alice,Data Science"
employee = DataEngineer.from_string(employee_data)
employee.tools = ["Python", "SQL", "Spark"]
employee.display_info()

# Example Output:
# Name: Alice, Department: Data Science, Tools: ['Python', 'SQL', 'Spark']


# Exercise 5 (Medium): Inheritance with Static Method
# Explanation: Write a base class `Vehicle` with a static method `is_motorized` that returns `True`. Then, create a derived class `Bicycle` that overrides this method to return `False`.
# Solution:


# Example Input:
print(f"Is Vehicle Motorized? {Vehicle.is_motorized()}")
print(f"Is Bicycle Motorized? {Bicycle.is_motorized()}")

# Example Output:
# Is Vehicle Motorized? True
# Is Bicycle Motorized? False


# 1 Hard Exercise

# Exercise 6 (Hard): Complex Class Hierarchy with Abstract Methods, Static Methods, and Class Methods
# Explanation: Write an abstract base class `Database` with an abstract method `connect`, a class method `get_instance` that returns a singleton instance of the subclass, and a static method `status` that returns "Active".
# Implement two subclasses, `MySQLDatabase` and `PostgreSQLDatabase`, that provide different implementations of the `connect` method.
# Solution:


# Example Input:
mysql_db = MySQLDatabase.get_instance()
postgresql_db = PostgreSQLDatabase.get_instance()
print(mysql_db.connect())
print(postgresql_db.connect())
print(f"MySQL DB Status: {MySQLDatabase.status()}")
print(f"PostgreSQL DB Status: {PostgreSQLDatabase.status()}")

# Example Output:
# Connected to MySQL Database
# Connected to PostgreSQL Database
# MySQL DB Status: Active
# PostgreSQL DB Status: Active
