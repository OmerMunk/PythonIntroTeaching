# Topic Recap: Multiple Inheritance and Polymorphism (Data Engineering Oriented)

from abc import ABC, abstractmethod

# 3 Easy Exercises

# Exercise 1 (Easy): Multiple Inheritance Basics
# Explanation: Write two base classes `Person` and `Worker`. Create a class `Employee` that inherits from both `Person` and `Worker`.
# The `Employee` class should have access to methods from both base classes.
# Solution:


# Example Input:
employee = Employee("Alice", "Data Engineer")
print(f"Name: {employee.get_name()}, Role: {employee.get_role()}")

# Example Output:
# Name: Alice, Role: Data Engineer


# Exercise 2 (Easy): Polymorphism with Methods
# Explanation: Write two classes `CSVProcessor` and `JSONProcessor` that both have a method `process_data`.
# Demonstrate polymorphism by calling `process_data` on an instance of each class.
# Solution:


# Example Input:
csv_processor = CSVProcessor()
json_processor = JSONProcessor()
print(csv_processor.process_data("CSV File Content"))
print(json_processor.process_data("JSON File Content"))

# Example Output:
# Processing CSV data: CSV File Content
# Processing JSON data: JSON File Content


# Exercise 3 (Easy): Polymorphism with a Common Interface
# Explanation: Write an abstract base class `Shape` with an abstract method `area()`. Create two subclasses `Rectangle` and `Circle` that implement the `area()` method.
# Demonstrate polymorphism by calling `area()` on instances of both subclasses.
# Solution:


# Example Input:
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# Example Output:
# Area: 20
# Area: 28.26


# 2 Medium Exercises

# Exercise 4 (Medium): Multiple Inheritance with Method Resolution Order (MRO)
# Explanation: Write three classes: `Person` (base class), `Employee` (derived from `Person`), and `Manager` (derived from both `Person` and `Employee`).
# Use `super()` to demonstrate the method resolution order (MRO) and how Python determines which method to call.
# Solution:


# Example Input:
manager = Manager("Alice", 12345, "Data Science")

# Example Output:
# Person initialized: Alice
# Employee initialized: Alice, ID: 12345
# Manager initialized: Alice, Department: Data Science


# Exercise 5 (Medium): Polymorphic Behavior with Multiple Inheritance
# Explanation: Write a class `DataProcessor` with a method `process`. Write two subclasses `CSVDataProcessor` and `JSONDataProcessor` that inherit from `DataProcessor` and override the `process` method.
# Additionally, implement a class `HybridProcessor` that inherits from both `CSVDataProcessor` and `JSONDataProcessor` and demonstrates polymorphic behavior.
# Solution:


# Example Input:
hybrid_processor = HybridProcessor()
print(hybrid_processor.process("Sample Data"))

# Example Output:
# Hybrid Result: Processing CSV data: Sample Data | Processing JSON data: Sample Data


# 1 Hard Exercise

# Exercise 6 (Hard): Advanced Multiple Inheritance with Polymorphism
# Explanation: Write an abstract base class `Database` with an abstract method `connect`.
# Implement two subclasses, `SQLDatabase` and `NoSQLDatabase`, that provide different implementations of the `connect` method.
# Create a `HybridDatabase` class that inherits from both `SQLDatabase` and `NoSQLDatabase`.
# Use method resolution order (MRO) and demonstrate polymorphism by calling `connect` on an instance of `HybridDatabase`.
# Solution:


# Example Input:
hybrid_db = HybridDatabase()
print(hybrid_db.connect())

# Example Output:
# Hybrid Connect: Connecting to SQL Database | Connecting to NoSQL Database
