# Topic Recap: Python Classes (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Create a Simple Class
# Explanation: Write a class `Employee` with attributes `name` and `role`. Include a method `display_info` that prints the employee's details.
# Solution:
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}")

# Example Input:
employee = Employee("Alice", "Data Engineer")
employee.display_info()

# Example Output:
# Name: Alice, Role: Data Engineer


# Exercise 2 (Easy): Class with Method to Update Attribute
# Explanation: Write a class `Product` with attributes `name` and `price`. Include a method `apply_discount` that takes a discount percentage and updates the price.
# Solution:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

# Example Input:
product = Product("Laptop", 1000)
product.apply_discount(10)
print(f"Product: {product.name}, Price after discount: ${product.price}")

# Example Output:
# Product: Laptop, Price after discount: $900.0


# Exercise 3 (Easy): Class with Default Values
# Explanation: Write a class `Customer` with attributes `name` and `membership` (default to "Standard"). Include a method `upgrade_membership` that upgrades membership to "Premium".
# Solution:
class Customer:
    def __init__(self, name, membership="Standard"):
        self.name = name
        self.membership = membership

    def upgrade_membership(self):
        self.membership = "Premium"

# Example Input:
customer = Customer("Bob")
customer.upgrade_membership()
print(f"Customer: {customer.name}, Membership: {customer.membership}")

# Example Output:
# Customer: Bob, Membership: Premium


# 2 Medium Exercises

# Exercise 4 (Medium): Inheritance in Classes
# Explanation: Write a base class `Employee` with attributes `name` and `department`, and a derived class `Manager` that inherits from `Employee` and adds an attribute `team_size`. Include methods to display employee and manager details.
# Solution:
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

class Manager(Employee):
    def __init__(self, name, department, team_size):
        super().__init__(name, department)
        self.team_size = team_size

    def display_manager_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Team Size: {self.team_size}")

# Example Input:
manager = Manager("Alice", "Data Science", 5)
manager.display_info()
manager.display_manager_info()

# Example Output:
# Name: Alice, Department: Data Science
# Name: Alice, Department: Data Science, Team Size: 5


# Exercise 5 (Medium): Class with Class Method
# Explanation: Write a class `Project` with a class attribute `project_count`. Include a class method `increment_count` to increase the project count by 1 every time a new project is created.
# Solution:
class Project:
    project_count = 0

    def __init__(self, name):
        self.name = name
        Project.increment_count()

    @classmethod
    def increment_count(cls):
        cls.project_count += 1

# Example Input:
project1 = Project("Project A")
project2 = Project("Project B")
print(f"Total Projects: {Project.project_count}")

# Example Output:
# Total Projects: 2


# 1 Hard Exercise

# Exercise 6 (Hard): Abstract Base Class and Inheritance
# Explanation: Write an abstract base class `DataProcessor` with an abstract method `process`. Implement two derived classes, `CSVProcessor` and `JSONProcessor`, that override the `process` method to handle CSV and JSON data respectively.
# Solution:
from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

class CSVProcessor(DataProcessor):
    def process(self, data):
        # Example CSV processing logic
        reader = csv.reader(data.splitlines())
        return [row for row in reader]

class JSONProcessor(DataProcessor):
    def process(self, data):
        # Example JSON processing logic
        return json.loads(data)

# Example Input:
csv_data = "name,age\nAlice,30\nBob,25"
json_data = '{"name": "Alice", "age": 30}'

csv_processor = CSVProcessor()
json_processor = JSONProcessor()

print(f"CSV Data: {csv_processor.process(csv_data)}")
print(f"JSON Data: {json_processor.process(json_data)}")

# Example Output:
# CSV Data: [['name', 'age'], ['Alice', '30'], ['Bob', '25']]
# JSON Data: {'name': 'Alice', 'age': 30}
