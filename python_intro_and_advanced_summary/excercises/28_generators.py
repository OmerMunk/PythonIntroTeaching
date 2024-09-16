# Topic Recap: Generators and yield (Data Engineering Oriented)

# Generators are a special class of iterators in Python that are defined using a function with one or more `yield` statements.
# Generators are used to create iterators in a simple and concise way, which can be iterated over once.

# 3 Easy Exercises

# Exercise 1 (Easy): Simple Generator for Numbers
# Explanation: Write a generator function `generate_numbers` that yields numbers from 1 to n.
# Solution:


# Example Input:
numbers = generate_numbers(5)
for number in numbers:
    print(number)

# Example Output:
# 1
# 2
# 3
# 4
# 5


# Exercise 2 (Easy): Generator for Even Numbers
# Explanation: Write a generator function `generate_even_numbers` that yields even numbers up to a given number n.
# Solution:


# Example Input:
even_numbers = generate_even_numbers(10)
for number in even_numbers:
    print(number)

# Example Output:
# 2
# 4
# 6
# 8
# 10


# Exercise 3 (Easy): Generator for Squares of Numbers
# Explanation: Write a generator function `generate_squares` that yields the squares of numbers from 1 to n.
# Solution:

# Example Input:
squares = generate_squares(4)
for square in squares:
    print(square)

# Example Output:
# 1
# 4
# 9
# 16


# 2 Medium Exercises

# Exercise 4 (Medium): Generator for Fibonacci Sequence
# Explanation: Write a generator function `fibonacci` that yields the Fibonacci sequence up to a maximum number n.
# Solution:


# Example Input:
fib_sequence = fibonacci(15)
for number in fib_sequence:
    print(number)

# Example Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13


# Exercise 5 (Medium): Generator to Read Large Files Line-by-Line
# Explanation: Write a generator function `read_large_file` that reads a large text file line-by-line.
# This function should yield each line one by one, avoiding loading the entire file into memory.
# Solution:


# Example Input:
# Assume 'large_file.txt' exists with multiple lines of text.
# for line in read_large_file('large_file.txt'):
#     print(line)

# Example Output:
# Each line of 'large_file.txt' printed one by one.


# 1 Hard Exercise

# Exercise 6 (Hard): Generator for Sliding Window
# Explanation: Write a generator function `sliding_window` that takes a list and a window size and yields a sliding window of elements of that size.
# For example, given the list `[1, 2, 3, 4, 5]` and window size 3, the function should yield `[1, 2, 3]`, `[2, 3, 4]`, `[3, 4, 5]`.
# Solution:

# Example Input:
data = [1, 2, 3, 4, 5]
window_size = 3
windows = sliding_window(data, window_size)
for window in windows:
    print(window)

# Example Output:
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]
