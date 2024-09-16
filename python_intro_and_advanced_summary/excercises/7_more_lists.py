# Topic Recap: List Methods, List Slicing, Nested Lists (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Cleaning Data with List Methods
# Explanation: Write a Python program that takes a list of strings representing raw data entries with extra spaces and removes any leading or trailing whitespace from each entry.
# Guidance: Use the `strip()` method inside a loop or with a list comprehension to clean each entry.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Cleaned Data: ['Data Engineer', 'Python Developer', 'Data Analyst', 'BI Specialist']


# Exercise 2 (Easy): Extracting Columns Using List Slicing
# Explanation: Given a list of data points representing daily temperatures, write a program to extract the temperatures for the first 7 days (a week's data).
# Guidance: Use list slicing to extract the first 7 elements from the list.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Temperatures for the first 7 days: [22, 21, 19, 20, 18, 23, 25]


# Exercise 3 (Easy): Nested List Access
# Explanation: Given a nested list representing a matrix (2D list), write a Python program that prints the first column of the matrix.
# Guidance: Use a loop to iterate over the rows and access the first element of each row.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# First column of the matrix: [1, 4, 7]


# 2 Medium Exercises

# Exercise 4 (Medium): Batch Data Processing with List Methods
# Explanation: Write a Python program that takes a list of transaction amounts (including some invalid data entries represented by 'N/A') and filters out the valid transactions. Then, calculate the total sum of valid transactions.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Total valid transaction amount: $1051.50


# Exercise 5 (Medium): Slicing and Aggregating Data
# Explanation: Given a list of hourly sales data, write a program to slice the list to extract data for each shift:
# - Morning shift: First 8 hours
# - Afternoon shift: Next 8 hours
# - Evening shift: Remaining hours
# Then, calculate the total sales for each shift.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Total Morning Sales: $1130
# Total Afternoon Sales: $1345
# Total Evening Sales: $1105


# 1 Hard Exercise

# Exercise 6 (Hard): Nested List Flattening and Data Aggregation
# Explanation: Write a Python program that takes a nested list of monthly sales data, where each sublist represents sales data for different weeks in a month. The program should:
# - Flatten the nested list into a single list of all sales data.
# - Calculate the total sales for the month.
# - Find the week with the highest total sales.
# Solution:


# Example Input:
# (No input required)
# Example Output:
# Flattened Sales Data: [200, 150, 300, 250, 180, 220, 140, 210, 190, 205, 225, 180, 160, 200, 210, 230]
# Total Monthly Sales: $3410
# Week with the Highest Sales: Week 1
