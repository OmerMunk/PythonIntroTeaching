# Task 1 (Easy): Create a Basic Defense Class with Magic Methods
# Explanation:
# Create a class `DefenseSystem` that represents a defense unit. Implement the following magic methods:
# - `__init__`: Initialize the defense unit with a name and status.
# - `__str__`: Return a formatted string describing the unit.
# - `__eq__`: Compare two units based on their names.

class DefenseSystem:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Defense System: {self.name}, Status: {self.status}"

    def __eq__(self, other):
        return self.name == other.name

# Example Input:
unit1 = DefenseSystem("Iron Dome", "Active")
unit2 = DefenseSystem("Iron Dome", "Inactive")

# Example Output:
print(unit1)  # Output: Defense System: Iron Dome, Status: Active
print(unit1 == unit2)  # Output: True

# ----------------------------------------------------------------------

# Task 2 (Easy): Use Decorators to Monitor Function Calls
# Explanation:
# Create a decorator `@monitor_activity` that prints a message every time a method in the class `SurveillanceUnit` is called.
# Apply the decorator to the `track_terrorist` method.

def monitor_activity(func):
    def wrapper(*args, **kwargs):
        print(f"Monitoring activity: {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

class SurveillanceUnit:
    def __init__(self, unit_name):
        self.unit_name = unit_name

    @monitor_activity
    def track_terrorist(self, location):
        return f"Tracking terrorist at {location}"

# Example Input:
unit = SurveillanceUnit("Drone Unit")
result = unit.track_terrorist("Gaza Strip")

# Example Output:
# Monitoring activity: track_terrorist called
# Tracking terrorist at Gaza Strip

# ----------------------------------------------------------------------

# Task 3 (Medium): Implement an Abstract Base Class for Intelligence Analysis
# Explanation:
# Create an abstract base class `IntelligenceAnalysis` with an abstract method `analyze_data`.
# Implement a subclass `CommunicationInterceptAnalysis` that provides a concrete implementation for `analyze_data`.

from abc import ABC, abstractmethod

class IntelligenceAnalysis(ABC):
    @abstractmethod
    def analyze_data(self, data):
        pass

class CommunicationInterceptAnalysis(IntelligenceAnalysis):
    def analyze_data(self, data):
        return f"Analyzing communication data: {data}"

# Example Input:
analysis = CommunicationInterceptAnalysis()
result = analysis.analyze_data("Intercepted message content")

# Example Output:
# Analyzing communication data: Intercepted message content

# ----------------------------------------------------------------------

# Task 4 (Medium): Create a Class with @classmethod and @staticmethod
# Explanation:
# Implement a class `AlertSystem` with a class method `create_system` that initializes the class with a name and a status.
# Also, implement a static method `validate_status` to check if a status is valid.

class AlertSystem:
    valid_statuses = ["Active", "Inactive", "Alert"]

    def __init__(self, name, status):
        self.name = name
        self.status = status

    @classmethod
    def create_system(cls, name, status):
        if cls.validate_status(status):
            return cls(name, status)
        else:
            raise ValueError("Invalid status")

    @staticmethod
    def validate_status(status):
        return status in AlertSystem.valid_statuses

# Example Input:
system = AlertSystem.create_system("City Surveillance", "Active")

# Example Output:
print(system)  # Output: <__main__.AlertSystem object at ...>

# ----------------------------------------------------------------------

# Task 5 (Hard): Implement Single Inheritance with Decorators and *args, **kwargs
# Explanation:
# Create a base class `DefenseUnit` with a method to initialize any defense unit.
# Implement a subclass `MissileDefenseUnit` that inherits from `DefenseUnit` and uses decorators to validate initialization.

def validate_initialization(func):
    def wrapper(*args, **kwargs):
        if 'range' in kwargs and kwargs['range'] <= 0:
            raise ValueError("Range must be positive")
        print(f"Initializing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class DefenseUnit:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class MissileDefenseUnit(DefenseUnit):
    @validate_initialization
    def __init__(self, name, status, range):
        super().__init__(name, status)
        self.range = range

# Example Input:
missile_unit = MissileDefenseUnit("Patriot", "Active", range=100)

# Example Output:
# Initializing: __init__
print(missile_unit)  # Output: <__main__.MissileDefenseUnit object at ...>

# ----------------------------------------------------------------------

# Task 6 (Hard): Implement Multiple Inheritance and Advanced Use of cls and self
# Explanation:
# Create two classes `LogisticsSupport` and `FieldOperations` with specific methods.
# Implement a class `CombinedOperation` that inherits from both, using cls and self to manage class-level and instance-level data.

class LogisticsSupport:
    @classmethod
    def supply_equipment(cls, equipment_type):
        print(f"{cls.__name__}: Supplying {equipment_type}")

class FieldOperations:
    def __init__(self, operation_name):
        self.operation_name = operation_name

    def deploy_troops(self, number):
        print(f"Deploying {number} troops for operation {self.operation_name}")

class CombinedOperation(LogisticsSupport, FieldOperations):
    def __init__(self, operation_name, **kwargs):
        super().__init__(operation_name)
        self.details = kwargs

    def execute(self):
        self.deploy_troops(self.details.get('troops', 0))
        cls.supply_equipment(self.details.get('equipment', 'basic gear'))

# Example Input:
operation = CombinedOperation("Operation Thunder", troops=50, equipment="armored vehicles")
operation.execute()

# Example Output:
# Deploying 50 troops for operation Operation Thunder
# CombinedOperation: Supplying armored vehicles
