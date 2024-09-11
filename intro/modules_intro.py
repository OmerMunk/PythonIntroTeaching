"""
    1.	Introduction to Python Modules
	2.	Creating a Python Module
	3.	Importing Modules
	4.	Using import Variants (import, from ... import, import ... as)
	5.	Exploring Built-in Modules
	6.	Creating and Using Packages
	7.	Understanding __init__.py and Its Purpose
	8.	Using __name__ and Module Execution
	9.	Reloading Modules with importlib
	10.	Best Practices for Using and Organizing Modules in Python
"""


"""

1. Introduction to Python Modules

A module is a file containing Python code, such as functions, classes, or variables, which can be reused across multiple scripts or programs. Python modules help organize your code logically and make it more maintainable.

	•	Standard Modules: Built-in modules that come with Python (e.g., os, sys, math).
	•	Third-Party Modules: Modules that are not part of the standard library and need to be installed (e.g., requests, pandas).
	•	Custom Modules: Modules that you create for your specific needs.


"""



"""
2. Creating a Python Module

To create a module, simply write a Python file (.py) containing functions, variables, or classes.

Example: Creating a Module

Let’s create a module named the_snake.py:


# the_snake.py

def show_yourself(name):
    return f"Hello, {name}! I am the snake"
    
SNAKE_MAGIC = 2.5178

def try_enter(a, b):
    return a + b == SNAKE_MAGIC

 
 
This file (the_snake.py) is now a module that can be imported and used in other Python scripts.

"""


"""

3. Importing Modules

You can import modules into other Python scripts using the import statement.

Example: Importing a Module

Create a new Python script named main.py and import the the_snake module:



# main.py

# Import the custom module
import the_snake

# Use functions and variables from the module
print(the_snake.show_yourself("Shubulu"))  # Output: Hello, Shubulu! I am the snake
print("Entered:", the_snake.add(5, 3))  # Output: Sum: False
print("Value of Snake Magic:", the_snake.SNAKE_MAGIC)  # Output: Value of SNAKE_MAGIC: 2.5178

"""



"""
4. Using import Variants (import, from ... import, import ... as)

There are several ways to import modules in Python:

	•	import module_name: Imports the entire module.
	•	from module_name import item: Imports specific items (functions, classes, variables) from a module.
	•	import module_name as alias: Imports a module and gives it a local alias.
	
	
	
# Import specific functions from the module
from mymodule import greet, PI

print(greet("Bob"))  # Output: Hello, Bob!
print("Value of PI:", PI)  # Output: Value of PI: 3.14159



# Import the module with an alias
import mymodule as mm

print(mm.greet("Charlie"))  # Output: Hello, Charlie!
print("Sum:", mm.add(10, 5))  # Output: Sum: 15

"""




"""
5. Exploring Built-in Modules

Python comes with a rich set of built-in modules that you can use without installing anything. Here are some commonly used built-in modules:

	•	os: Provides functions for interacting with the operating system.
	•	sys: Provides access to some variables used or maintained by the Python interpreter.
	•	math: Provides mathematical functions.
	•	datetime: Provides classes for manipulating dates and times.
	•	random: Provides functions for generating random numbers.
	
	
	
import math

print("Square root of 16:", math.sqrt(16))  # Output: Square root of 16: 4.0
print("Factorial of 5:", math.factorial(5))  # Output: Factorial of 5: 120
print("Cosine of 0 radians:", math.cos(0))  # Output: Cosine of 0 radians: 1.0



import os

# Get the current working directory
print("Current Directory:", os.getcwd())

# List files in the current directory
print("Files:", os.listdir())

# Check if a path is a file or directory
print("Is 'main.py' a file?", os.path.isfile('main.py'))

"""





"""

6. Creating and Using Packages

A package is a collection of modules organized in a directory hierarchy. Packages help organize modules and provide a namespace hierarchy for better code organization.

mypackage/
    __init__.py
    module1.py
    module2.py


	•	__init__.py: A special file that indicates that the directory is a package. It can be empty or contain package initialization code.



	1.	Create Package Structure:
	2.	Create math_utils.py Module:
    3.	Create string_utils.py Module:
	4.	Import and Use Package Modules:


"""



"""
7. Understanding __init__.py and Its Purpose
The __init__.py file is used to initialize Python packages. It can be an empty file or contain code that initializes the package when it is imported.

	•	Defines Package Content: Can specify which modules or subpackages should be imported when using from package import *.
	•	Executes Initialization Code: Code inside __init__.py is executed when the package is imported.
	
	
	
# __init__.py

print("Initializing mypackage...")

__all__ = ['math_utils', 'string_utils']  # Specifies modules to import with 'from mypackage import *'

"""




"""
8. Using __name__ and Module Execution

The __name__ variable is a special built-in variable that determines if a module is being run as the main program or imported as a module.

	•	__name__ == "__main__": If the module is being run directly, __name__ will be "__main__".
	•	__name__ == "module_name": If the module is imported, __name__ will be its name.
	
	
	
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))  # This will only run if the module is executed directly

"""



"""
9. Reloading Modules with importlib

Python caches imported modules to improve performance. If you modify a module after importing it, the changes won’t be reflected unless you reload it using the importlib module.



import importlib
import mymodule

# Modify 'mymodule' code externally...

# Reload the modified module
importlib.reload(mymodule)


"""



"""
10. Best Practices for Using and Organizing Modules in Python

	•	Use Meaningful Names: Name your modules and packages according to their purpose.
	•	Keep Modules Small: Divide code into small, manageable modules that perform specific tasks.
	•	Avoid Circular Imports: Structure modules to avoid circular dependencies, which can cause import errors.
	•	Use Packages for Organization: Group related modules into packages for better organization.
	•	Document Modules and Functions: Provide clear and concise documentation for modules and functions.

"""