# main.py
# Import the custom module
# option a
# import the file name, and than access by it.
# import the_snake
# from intro.the_snake import show_yourself
#
# # Use functions and variables from the module
# print(the_snake.show_yourself("Shubulu"))  # Output: Hello, Shubulu! I am the snake
# print("Entered:", the_snake.try_enter(5, 3))  # Output:: False
# print("Value of Snake Magic:", the_snake.SNAKE_MAGIC)  # Output: Value of SNAKE_MAGIC: 2.5178


# #option b
from the_snake import show_yourself
#
# show_yourself()

#option c:
from the_snake import *

#option d:
import the_snake as ts
ts.try_enter()
ts.SNAKE_MAGIC


from utils import *
math_utils.add()
str_utils.make_lower()
shu




