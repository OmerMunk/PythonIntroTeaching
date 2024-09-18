# File: test_hard_exercises.py

import pytest


# ======================================
# Exercise 1 (With Solution):
# ======================================
# Explanation:
# Write a function that computes the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
# The function should handle edge cases like negative numbers and zero.
# The test should cover positive integers (happy flow), negative integers (logical edge case), and zero (bad flow).
def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers")
    if a == 0 or b == 0:
        return max(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def test_gcd():
    # Happy flow
    assert gcd(48, 18) == 6
    assert gcd(7, 5) == 1

    # Logical edge cases
    assert gcd(0, 5) == 5
    assert gcd(10, 0) == 10

    # Bad flow - negative numbers
    with pytest.raises(ValueError):
        gcd(-48, 18)

    # Python programming edge cases
    with pytest.raises(TypeError):
        gcd(None, 5)
    with pytest.raises(TypeError):
        gcd("10", 5)


# ======================================
# Exercise 2 (Without Solution):
# ======================================
# Write a function that checks whether a string is a valid email address.
# The test should include happy flow (valid email), bad flow (invalid email formats),
# and edge cases (empty strings, None, and special characters).
def is_valid_email(email):
    pass


def test_is_valid_email():
    pass


# ======================================
# Exercise 3 (With Solution):
# ======================================
# Explanation:
# Write a function that performs matrix multiplication. The function should handle rectangular matrices
# and return the correct product matrix. Handle edge cases where one or both matrices are empty.
def matrix_multiply(A, B):
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def test_matrix_multiply():
    # Happy flow
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    assert matrix_multiply(A, B) == [[58, 64], [139, 154]]

    # Logical edge case
    A = [[0, 0], [0, 0]]
    B = [[0, 0], [0, 0]]
    assert matrix_multiply(A, B) == [[0, 0], [0, 0]]

    # Bad flow - matrices with incompatible dimensions
    A = [[1, 2]]
    B = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError):
        matrix_multiply(A, B)

    # Python programming edge cases - empty matrices
    with pytest.raises(ValueError):
        matrix_multiply([], [[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        matrix_multiply([[1, 2], [3, 4]], [])


# ======================================
# Exercise 4 (Without Solution):
# ======================================
# Write a function that checks if a string is a valid palindrome when ignoring spaces and punctuation.
# The test should include happy flow (valid palindrome), bad flow (invalid palindrome),
# and edge cases (empty strings, None, and strings with only spaces or punctuation).
def is_valid_palindrome(s):
    pass


def test_is_valid_palindrome():
    pass


# ======================================
# Exercise 5 (With Solution):
# ======================================
# Explanation:
# Write a function that reads a CSV file and returns the data as a list of dictionaries.
# The test should cover cases where the file exists (happy flow), the file is empty, and the file doesn't exist.
import csv
import os


def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist")

    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(dict(row))
    return data


def test_read_csv(tmpdir):
    # Happy flow - valid CSV file
    csv_file = tmpdir.join("test.csv")
    csv_file.write("name,age\nAlice,30\nBob,25\n")

    data = read_csv(str(csv_file))
    assert data == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]

    # Logical edge case - empty CSV file
    empty_csv_file = tmpdir.join("empty.csv")
    empty_csv_file.write("")
    assert read_csv(str(empty_csv_file)) == []

    # Bad flow - non-existent file
    with pytest.raises(FileNotFoundError):
        read_csv("non_existent_file.csv")


# ======================================
# Exercise 6 (Without Solution):
# ======================================
# Write a function that returns the median of a list of numbers.
# Handle cases like lists with an odd number of elements, even number of elements, and edge cases like empty lists or None.
def find_median(lst):
    pass


def test_find_median():
    pass


# ======================================
# Exercise 7 (With Solution):
# ======================================
# Explanation:
# Write a function that generates all permutations of a list.
# Test it with normal lists (happy flow), empty lists, and edge cases like None.
import itertools


def generate_permutations(lst):
    if lst is None:
        raise ValueError("Input cannot be None")
    return list(itertools.permutations(lst))


def test_generate_permutations():
    # Happy flow
    assert generate_permutations([1, 2, 3]) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    # Logical edge cases
    assert generate_permutations([]) == []
    assert generate_permutations([1]) == [(1,)]

    # Bad flow - input is None
    with pytest.raises(ValueError):
        generate_permutations(None)


# ======================================
# Exercise 8 (Without Solution):
# ======================================
# Write a function that checks if two lists are anagrams of each other.
# The test should include happy flow (valid anagrams), bad flow (non-anagrams),
# and edge cases like empty lists, None, or lists with different lengths.
def are_anagrams(list1, list2):
    pass


def test_are_anagrams():
    pass


# ======================================
# Exercise 9 (With Solution):
# ======================================
# Explanation:
# Write a function that parses a JSON file and returns the data.
# The function should handle non-existent files and files with invalid JSON format.
import json


def parse_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist")

    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")


def test_parse_json(tmpdir):
    # Happy flow - valid JSON file
    json_file = tmpdir.join("test.json")
    json_file.write('{"name": "Alice", "age": 30}')

    data = parse_json(str(json_file))
    assert data == {"name": "Alice", "age": 30}

    # Bad flow - invalid JSON format
    invalid_json_file = tmpdir.join("invalid.json")
    invalid_json_file.write('{"name": "Alice", "age": 30')  # Missing closing brace
    with pytest.raises(ValueError):
        parse_json(str(invalid_json_file))

    # Bad flow - non-existent file
    with pytest.raises(FileNotFoundError):
        parse_json("non_existent_file.json")


# ======================================
# Exercise 10 (Without Solution):
# ======================================
# Write a function that computes the longest common subsequence (LCS) of two strings.
# Test the function with normal strings (happy flow), empty strings, None, and edge cases like strings with no common characters.
def longest_common_subsequence(s1, s2):
    pass


def test_longest_common_subsequence():
    pass
