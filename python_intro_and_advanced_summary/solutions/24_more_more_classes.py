# Topic Recap: Multiple Inheritance and Polymorphism (Data Engineering Oriented)

from abc import ABC, abstractmethod

# 3 Easy Exercises

# Exercise 1 (Easy): Multiple Inheritance Basics
# Explanation: Write two base classes `Person` and `Worker`. Create a class `Employee` that inherits from both `Person` and `Worker`.
# The `Employee` class should have access to methods from both base classes.
# Solution:
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Worker:
    def __init__(self, role):
        self.role = role

    def get_role(self):
        return self.role

class Employee(Person, Worker):
    def __init__(self, name, role):
        Person.__init__(self, name)
        Worker.__init__(self, role)

# Example Input:
employee = Employee("Alice", "Data Engineer")
print(f"Name: {employee.get_name()}, Role: {employee.get_role()}")

# Example Output:
# Name: Alice, Role: Data Engineer


# Exercise 2 (Easy): Polymorphism with Methods
# Explanation: Write two classes `CSVProcessor` and `JSONProcessor` that both have a method `process_data`.
# Demonstrate polymorphism by calling `process_data` on an instance of each class.
# Solution:
class CSVProcessor:
    def process_data(self, data):
        return f"Processing CSV data: {data}"

class JSONProcessor:
    def process_data(self, data):
        return f"Processing JSON data: {data}"

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
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

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
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized: {self.name}")

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        print(f"Employee initialized: {self.name}, ID: {self.employee_id}")

class Manager(Employee, Person):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
        print(f"Manager initialized: {self.name}, Department: {self.department}")

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
class DataProcessor:
    def process(self, data):
        raise NotImplementedError("Subclasses should implement this!")

class CSVDataProcessor(DataProcessor):
    def process(self, data):
        return f"Processing CSV data: {data}"

class JSONDataProcessor(DataProcessor):
    def process(self, data):
        return f"Processing JSON data: {data}"

class HybridProcessor(CSVDataProcessor, JSONDataProcessor):
    def process(self, data):
        csv_result = super().process(data)
        json_result = JSONDataProcessor.process(self, data)
        return f"Hybrid Result: {csv_result} | {json_result}"

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
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class SQLDatabase(Database):
    def connect(self):
        return "Connecting to SQL Database"

class NoSQLDatabase(Database):
    def connect(self):
        return "Connecting to NoSQL Database"

class HybridDatabase(SQLDatabase, NoSQLDatabase):
    def connect(self):
        sql_result = super().connect()  # Follows MRO, calls SQLDatabase's connect
        nosql_result = NoSQLDatabase.connect(self)  # Directly calls NoSQLDatabase's connect
        return f"Hybrid Connect: {sql_result} | {nosql_result}"

# Example Input:
hybrid_db = HybridDatabase()
print(hybrid_db.connect())

# Example Output:
# Hybrid Connect: Connecting to SQL Database | Connecting to NoSQL Database
