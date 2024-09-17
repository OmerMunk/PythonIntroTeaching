# Topic Recap: ABC (Abstract Base Class), Abstract Class, Class Method, Static Method, Inheritance (Data Engineering Oriented)

from abc import ABC, abstractmethod

# 3 Easy Exercises

# Exercise 1 (Easy): Define Abstract Base Class
# Explanation: Write an abstract base class `Shape` with an abstract method `area()`. Then, create two derived classes `Square` and `Circle` that implement the `area()` method.
# Solution:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

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
class Counter:
    count = 0

    @classmethod
    def increment(cls, value):
        cls.count += value

# Example Input:
Counter.increment(5)
Counter.increment(3)
print(f"Current Count: {Counter.count}")

# Example Output:
# Current Count: 8


# Exercise 3 (Easy): Static Method
# Explanation: Write a class `MathOperations` with a static method `add` that takes two numbers and returns their sum.
# Solution:
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

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
class Employee(ABC):
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @classmethod
    def from_string(cls, employee_string):
        name, department = employee_string.split(',')
        return cls(name, department)

    @abstractmethod
    def display_info(self):
        pass

class DataEngineer(Employee):
    def __init__(self, name, department, tools):
        super().__init__(name, department)
        self.tools = tools

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Tools: {self.tools}")

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
class Vehicle:
    @staticmethod
    def is_motorized():
        return True

class Bicycle(Vehicle):
    @staticmethod
    def is_motorized():
        return False

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
class Database(ABC):
    _instances = {}

    @abstractmethod
    def connect(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = cls()
        return cls._instances[cls]

    @staticmethod
    def status():
        return "Active"

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL Database"

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
