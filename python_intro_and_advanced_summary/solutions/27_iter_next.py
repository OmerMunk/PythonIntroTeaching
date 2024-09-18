# Topic Recap: iter(), next() (Data Engineering Oriented)

# `iter()` and `next()` are built-in functions in Python used to create and manipulate iterators.
# `iter()` is used to get an iterator object from an iterable.
# `next()` retrieves the next item from an iterator.

# 3 Easy Exercises

# Exercise 1 (Easy): Convert List to Iterator
# Explanation: Write a function `list_to_iterator` that takes a list and returns an iterator for that list using `iter()`.
# Then, use `next()` to get the first item from the iterator.
# Solution:
def list_to_iterator(lst):
    iterator = iter(lst)
    first_item = next(iterator)
    return first_item

# Example Input:
lst = [10, 20, 30, 40]
first_item = list_to_iterator(lst)
print(f"First Item: {first_item}")

# Example Output:
# First Item: 10


# Exercise 2 (Easy): Iterate Over a String Using iter() and next()
# Explanation: Write a function `iterate_string` that takes a string and iterates over each character using `iter()` and `next()`.
# Solution:
def iterate_string(s):
    iterator = iter(s)
    result = []
    try:
        while True:
            result.append(next(iterator))
    except StopIteration:
        pass
    return result

# Example Input:
s = "Python"
characters = iterate_string(s)
print(f"Characters in String: {characters}")

# Example Output:
# Characters in String: ['P', 'y', 't', 'h', 'o', 'n']


# Exercise 3 (Easy): Iterate Over a Dictionary
# Explanation: Write a function `iterate_dictionary` that takes a dictionary and iterates over its keys using `iter()` and `next()`.
# Solution:
def iterate_dictionary(d):
    iterator = iter(d.keys())
    result = []
    try:
        while True:
            result.append(next(iterator))
    except StopIteration:
        pass
    return result

# Example Input:
d = {'a': 1, 'b': 2, 'c': 3}
keys = iterate_dictionary(d)
print(f"Dictionary Keys: {keys}")

# Example Output:
# Dictionary Keys: ['a', 'b', 'c']


# 2 Medium Exercises

# Exercise 4 (Medium): Create a Custom Iterator for a Range
# Explanation: Write a class `CustomRange` that mimics the behavior of Python's built-in `range` function using `iter()` and `next()`.
# Solution:
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Example Input:
custom_range = CustomRange(1, 5)
for number in custom_range:
    print(number)

# Example Output:
# 1
# 2
# 3
# 4


# Exercise 5 (Medium): Implement a Reverse Iterator
# Explanation: Write a class `ReverseIterator` that takes a list and iterates over it in reverse order using `iter()` and `next()`.
# Solution:
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value

# Example Input:
reversed_list = ReverseIterator([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# Example Output:
# 4
# 3
# 2
# 1


# 1 Hard Exercise

# Exercise 6 (Hard): Custom Iterator with a Step and Limit
# Explanation: Write a class `StepIterator` that iterates over a sequence with a given step size and limit.
# It should implement the `__iter__()` and `__next__()` methods.
# Solution:
class StepIterator:
    def __init__(self, start, limit, step):
        self.current = start
        self.limit = limit
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

# Example Input:
step_iterator = StepIterator(0, 10, 2)
for number in step_iterator:
    print(number)

# Example Output:
# 0
# 2
# 4
# 6
# 8
