# Topic Recap: Files - Reading, Writing, Editing, Appending, Deleting, Handling Multiple Files, Merging Files (CSV, TXT, JSON) (Data Engineering Oriented)

import os
import csv
import json


# 3 Easy Exercises

# Exercise 1 (Easy): Read a Text File
# Explanation: Write a function `read_text_file` that takes a filename and reads its content. Print each line from the file.
# Solution:



# Example Input:
# Create a file named 'sample.txt' with the following content:
# Data Engineering is important.
# Python is a versatile language.

# Run the function:
read_text_file('sample.txt')


# Example Output:
# Data Engineering is important.
# Python is a versatile language.


# Exercise 2 (Easy): Write to a Text File
# Explanation: Write a function `write_text_file` that takes a filename and a list of strings. Write each string to a new line in the file.
# Solution:



# Example Input:
lines_to_write = ["Data Engineering is fun.", "Writing to files in Python."]
write_text_file('output.txt', lines_to_write)


# Example Output:
# Creates 'output.txt' with:
# Data Engineering is fun.
# Writing to files in Python.


# Exercise 3 (Easy): Append to a Text File
# Explanation: Write a function `append_text_file` that takes a filename and a string, and appends the string to the file.
# Solution:



# Example Input:
append_text_file('output.txt', "Appending new data to the file.")


# Example Output:
# Appends the line "Appending new data to the file." to 'output.txt'.


# 2 Medium Exercises

# Exercise 4 (Medium): Read and Merge CSV Files
# Explanation: Write a function `merge_csv_files` that takes two CSV filenames, reads them, and merges their content into a new CSV file.
# Solution:



# Example Input:
# Assuming 'file1.csv' and 'file2.csv' are CSV files with similar structures
merge_csv_files('file1.csv', 'file2.csv', 'merged_output.csv')


# Example Output:
# Creates 'merged_output.csv' with combined content of 'file1.csv' and 'file2.csv'.


# Exercise 5 (Medium): Read and Update JSON File
# Explanation: Write a function `update_json_file` that reads a JSON file, updates a specific key-value pair, and writes the updated content back to the file.
# Solution:


# Example Input:
# Assume 'data.json' contains: {"name": "Alice", "role": "Data Engineer"}
update_json_file('data.json', 'role', 'Senior Data Engineer')


# Example Output:
# Updates 'data.json' to: {"name": "Alice", "role": "Senior Data Engineer"}


# 1 Hard Exercise

# Exercise 6 (Hard): Merge Multiple Files by Type
# Explanation: Write a function `merge_files_by_type` that takes a directory path and merges all files of the same type (CSV, TXT, JSON) within that directory.
# - For CSV files: Combine rows into one CSV file.
# - For TXT files: Concatenate content into one text file.
# - For JSON files: Combine JSON objects into a list and save it in a new JSON file.
# Solution:



# Example Input:
# Assume there are multiple CSV, TXT, and JSON files in the 'data_files' directory.
merge_files_by_type('data_files')

# Example Output:
# Creates 'merged_output.csv', 'merged_output.txt', and 'merged_output.json' with combined content of all files in 'data_files'.
