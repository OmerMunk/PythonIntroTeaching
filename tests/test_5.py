# File: test_medium_exercises.py

import pytest


# ======================================
# Exercise 1 (With Solution):
# ======================================
# Explanation:
# Write a function that converts a temperature from Celsius to Fahrenheit.
# Include tests for happy flow (normal temperatures), bad flow (invalid input like strings),
# and edge cases (0 degrees, negative temperatures).
def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number")
    return celsius * 9/5 + 32

@pytest.mark.parametrize("celsius, expected", [
    (0, 32),             # edge case: 0 degrees
    (-40, -40),          # edge case: extremely cold temperature
    (100, 212),          # happy flow: boiling point of water
    (37, 98.6)           # happy flow: normal body temperature
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected, 0.1)

def test_celsius_to_fahrenheit_bad_input():
    # Bad flow: input is a string
    with pytest.raises(ValueError):
        celsius_to_fahrenheit("invalid")

    # Python programming edge case: input is None
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(None)


# ======================================
# Exercise 2 (Without Solution):
# ======================================
# Write a function that calculates the factorial of a number.
# Use recursion, and include tests for happy flow (positive numbers),
# bad flow (invalid input such as negative numbers), and edge cases (0, None, or strings).
def factorial(n):
    pass

@pytest.mark.parametrize("n, expected", [
    (0, 1),              # edge case: factorial of 0 is 1
    (5, 120),            # happy flow: factorial of 5
    (7, 5040),           # happy flow: factorial of 7
])
def test_factorial(n, expected):
    pass

def test_factorial_bad_input():
    pass


# ======================================
# Exercise 3 (With Solution):
# ======================================
# Explanation:
# Write a function that takes a string and returns the reverse of it.
# Test with happy flow (normal strings), edge cases (empty strings, single characters),
# and bad flow (non-string input).
def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

@pytest.mark.parametrize("s, expected", [
    ("hello", "olleh"),         # happy flow: normal string
    ("", ""),                   # edge case: empty string
    ("a", "a"),                 # edge case: single character
    ("racecar", "racecar"),     # happy flow: palindrome
])
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected

def test_reverse_string_bad_input():
    # Bad flow: input is not a string
    with pytest.raises(ValueError):
        reverse_string(123)


# ======================================
# Exercise 4 (Without Solution):
# ======================================
# Write a function that sums all even numbers in a list.
# Include tests for happy flow (normal list of numbers), edge cases (empty list, all odd numbers),
# and bad flow (invalid input such as strings or None).
def sum_even_numbers(lst):
    pass

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4, 5, 6], 12),  # happy flow: sum of even numbers
    ([], 0),                   # edge case: empty list
    ([1, 3, 5, 7], 0),         # edge case: no even numbers
])
def test_sum_even_numbers(lst, expected):
    pass

def test_sum_even_numbers_bad_input():
    pass


# ======================================
# Exercise 5 (With Solution):
# ======================================
# Explanation:
# Write a function that calculates the nth Fibonacci number.
# Test happy flow (valid numbers), edge cases (0th Fibonacci number),
# and bad flow (negative numbers, non-integer input).
def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@pytest.mark.parametrize("n, expected", [
    (0, 0),              # edge case: 0th Fibonacci number
    (1, 1),              # happy flow: 1st Fibonacci number
    (10, 55),            # happy flow: 10th Fibonacci number
    (20, 6765),          # happy flow: 20th Fibonacci number
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_bad_input():
    # Bad flow: negative number
    with pytest.raises(ValueError):
        fibonacci(-1)

    # Python programming edge case: input is None
    with pytest.raises(ValueError):
        fibonacci(None)


# ======================================
# Exercise 6 (Without Solution):
# ======================================
# Write a function that calculates the average of a list of numbers.
# Include tests for happy flow (normal lists), edge cases (empty lists),
# and bad flow (None or invalid input like strings).
def calculate_average(lst):
    pass

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4, 5], 3),       # happy flow: average of 1-5 is 3
    ([10, 10, 10], 10),         # happy flow: average of identical numbers
    ([], 0),                    # edge case: empty list
])
def test_calculate_average(lst, expected):
    pass

def test_calculate_average_bad_input():
    pass


# ======================================
# Exercise 7 (With Solution):
# ======================================
# Explanation:
# Write a function that checks if a string is a valid palindrome (ignoring spaces and case).
# Test happy flow (valid palindromes), bad flow (non-palindromes),
# and edge cases (empty strings, single-character strings, None).
def is_palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]

@pytest.mark.parametrize("s, expected", [
    ("A man a plan a canal Panama", True),   # happy flow: palindrome ignoring spaces and case
    ("hello", False),                        # bad flow: not a palindrome
    ("", True),                              # edge case: empty string
    ("a", True),                             # edge case: single character
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

def test_is_palindrome_bad_input():
    # Bad flow: input is not a string
    with pytest.raises(ValueError):
        is_palindrome(123)


# ======================================
# Exercise 8 (Without Solution):
# ======================================
# Write a function that removes all vowels from a string.
# Include tests for happy flow (normal strings), edge cases (empty strings, strings without vowels),
# and bad flow (None or invalid input like integers).
def remove_vowels(s):
    pass

@pytest.mark.parametrize("s, expected", [
    ("hello", "hll"),                 # happy flow: remove vowels
    ("world", "wrld"),                # happy flow: remove vowels
    ("", ""),                         # edge case: empty string
    ("bcdfg", "bcdfg"),               # edge case: no vowels
])
def test_remove_vowels(s, expected):
    pass

def test_remove_vowels_bad_input():
    pass


# ======================================
# Exercise 9 (With Solution):
# ======================================
# Explanation:
# Write a function that checks if a number is a perfect square.
# Test happy flow (perfect squares), edge cases (0),
# and bad flow (negative numbers, non-integer input).
def is_perfect_square(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    return int(n ** 0.5) ** 2 == n

@pytest.mark.parametrize("n, expected", [
    (0, True),               # edge case: 0 is a perfect square
    (1, True),               # happy flow: 1 is a perfect square
    (4, True),               # happy flow: 4 is a perfect square
    (17, False),             # bad flow: 17 is not a perfect square
])
def test_is_perfect_square(n, expected):
    assert is_perfect_square(n) == expected

def test_is_perfect_square_bad_input():
    # Bad flow: negative number
    with pytest.raises(ValueError):
        is_perfect_square(-1)

    # Python programming edge case: input is None
    with pytest.raises(ValueError):
        is_perfect_square(None)


# ======================================
# Exercise 10 (Without Solution):
# ======================================
# Write a function that counts the number of vowels in a string.
# Include tests for happy flow (normal strings), edge cases (empty strings, no vowels),
# and bad flow (None or invalid input like integers).
def count_vowels(s):
    pass

@pytest.mark.parametrize("s, expected", [
    ("hello", 2),                 # happy flow: count vowels
    ("world", 1),                 # happy flow: count vowels
    ("", 0),                      # edge case: empty string
    ("bcdfg", 0),                 # edge case: no vowels
])
def test_count_vowels(s, expected):
    pass

def test_count_vowels_bad_input():
    pass
