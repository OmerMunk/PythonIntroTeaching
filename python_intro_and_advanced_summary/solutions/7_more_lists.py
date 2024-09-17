# Topic Recap: List Methods, List Slicing, Nested Lists (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Cleaning Data with List Methods
# Explanation: Write a Python program that takes a list of strings representing raw data entries with extra spaces and removes any leading or trailing whitespace from each entry.
# Guidance: Use the `strip()` method inside a loop or with a list comprehension to clean each entry.
# Solution:
raw_data = ["   Data Engineer   ", "Python Developer", "  Data Analyst ", "  BI Specialist "]
cleaned_data = [entry.strip() for entry in raw_data]

print(f"Cleaned Data: {cleaned_data}")

# Example Input:
# (No input required)
# Example Output:
# Cleaned Data: ['Data Engineer', 'Python Developer', 'Data Analyst', 'BI Specialist']


# Exercise 2 (Easy): Extracting Columns Using List Slicing
# Explanation: Given a list of data points representing daily temperatures, write a program to extract the temperatures for the first 7 days (a week's data).
# Guidance: Use list slicing to extract the first 7 elements from the list.
# Solution:
temperatures = [22, 21, 19, 20, 18, 23, 25, 24, 26, 19, 21]
weekly_temperatures = temperatures[:7]

print(f"Temperatures for the first 7 days: {weekly_temperatures}")

# Example Input:
# (No input required)
# Example Output:
# Temperatures for the first 7 days: [22, 21, 19, 20, 18, 23, 25]


# Exercise 3 (Easy): Nested List Access
# Explanation: Given a nested list representing a matrix (2D list), write a Python program that prints the first column of the matrix.
# Guidance: Use a loop to iterate over the rows and access the first element of each row.
# Solution:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
first_column = [row[0] for row in matrix]

print(f"First column of the matrix: {first_column}")

# Example Input:
# (No input required)
# Example Output:
# First column of the matrix: [1, 4, 7]


# 2 Medium Exercises

# Exercise 4 (Medium): Batch Data Processing with List Methods
# Explanation: Write a Python program that takes a list of transaction amounts (including some invalid data entries represented by 'N/A') and filters out the valid transactions. Then, calculate the total sum of valid transactions.
# Solution:
transactions = ["200.50", "150.00", "N/A", "300.75", "N/A", "400.25"]
valid_transactions = [float(t) for t in transactions if t != "N/A"]
total_amount = sum(valid_transactions)

print(f"Total valid transaction amount: ${total_amount:.2f}")

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
sales_data = [120, 150, 100, 180, 200, 130, 140, 110, 160, 90, 210, 230, 115, 95, 175, 125, 185, 155, 205, 165, 135, 145, 190, 170]
morning_shift = sales_data[:8]
afternoon_shift = sales_data[8:16]
evening_shift = sales_data[16:]

total_morning_sales = sum(morning_shift)
total_afternoon_sales = sum(afternoon_shift)
total_evening_sales = sum(evening_shift)

print(f"Total Morning Sales: ${total_morning_sales}")
print(f"Total Afternoon Sales: ${total_afternoon_sales}")
print(f"Total Evening Sales: ${total_evening_sales}")

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
monthly_sales = [
    [200, 150, 300, 250],  # Week 1
    [180, 220, 140, 210],  # Week 2
    [190, 205, 225, 180],  # Week 3
    [160, 200, 210, 230]   # Week 4
]

# Flattening the nested list
flattened_sales = [sale for week in monthly_sales for sale in week]
total_sales = sum(flattened_sales)

# Finding the week with the highest total sales
weekly_totals = [sum(week) for week in monthly_sales]
highest_sales_week = weekly_totals.index(max(weekly_totals)) + 1

print(f"Flattened Sales Data: {flattened_sales}")
print(f"Total Monthly Sales: ${total_sales}")
print(f"Week with the Highest Sales: Week {highest_sales_week}")

# Example Input:
# (No input required)
# Example Output:
# Flattened Sales Data: [200, 150, 300, 250, 180, 220, 140, 210, 190, 205, 225, 180, 160, 200, 210, 230]
# Total Monthly Sales: $3410
# Week with the Highest Sales: Week 1
