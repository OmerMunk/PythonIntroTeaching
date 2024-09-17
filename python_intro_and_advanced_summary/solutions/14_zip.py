# Topic Recap: zip() (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Pairing Data with zip()
# Explanation: Write a function `pair_data` that takes two lists: one with employee names and another with their respective roles, and returns a list of tuples pairing each name with the corresponding role using `zip()`.
# Solution:
def pair_data(names, roles):
    return list(zip(names, roles))

# Example Input:
names = ["Alice", "Bob", "Charlie"]
roles = ["Data Engineer", "Data Scientist", "ML Engineer"]
paired_data = pair_data(names, roles)
print(f"Paired Data: {paired_data}")

# Example Output:
# Paired Data: [('Alice', 'Data Engineer'), ('Bob', 'Data Scientist'), ('Charlie', 'ML Engineer')]


# Exercise 2 (Easy): Combine Lists of Numbers
# Explanation: Write a function `combine_and_sum` that takes two lists of numbers and returns a new list containing the sum of corresponding elements using `zip()`.
# Solution:
def combine_and_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

# Example Input:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed_list = combine_and_sum(list1, list2)
print(f"Summed List: {summed_list}")

# Example Output:
# Summed List: [5, 7, 9]


# Exercise 3 (Easy): Creating Dictionary from Two Lists
# Explanation: Write a function `create_dict` that takes two lists: one of keys and one of values, and returns a dictionary created from these lists using `zip()`.
# Solution:
def create_dict(keys, values):
    return dict(zip(keys, values))

# Example Input:
keys = ["id", "name", "age"]
values = [1, "Alice", 30]
result_dict = create_dict(keys, values)
print(f"Created Dictionary: {result_dict}")

# Example Output:
# Created Dictionary: {'id': 1, 'name': 'Alice', 'age': 30}


# 2 Medium Exercises

# Exercise 4 (Medium): Compare Two Datasets
# Explanation: Write a function `compare_datasets` that takes two lists of sales data (sales_data1 and sales_data2) where each list contains the sales amounts of different regions. The function should:
# - Use `zip()` to pair the corresponding sales data of the two datasets.
# - Return a list of tuples containing each region's sales difference (sales_data1 - sales_data2).
# Solution:
def compare_datasets(sales_data1, sales_data2):
    return [(region1 - region2) for region1, region2 in zip(sales_data1, sales_data2)]

# Example Input:
sales_data1 = [150, 200, 250]
sales_data2 = [100, 180, 300]
sales_difference = compare_datasets(sales_data1, sales_data2)
print(f"Sales Difference by Region: {sales_difference}")

# Example Output:
# Sales Difference by Region: [50, 20, -50]


# Exercise 5 (Medium): Merging and Formatting Data
# Explanation: Write a function `merge_and_format_data` that takes two lists: one with column names and another with corresponding data points. The function should:
# - Use `zip()` to merge the lists.
# - Return a list of formatted strings like "Column: Data".
# Solution:
def merge_and_format_data(columns, data):
    return [f"{col}: {val}" for col, val in zip(columns, data)]

# Example Input:
columns = ["Name", "Role", "Location"]
data = ["Alice", "Data Engineer", "New York"]
formatted_data = merge_and_format_data(columns, data)
print(f"Formatted Data: {formatted_data}")

# Example Output:
# Formatted Data: ['Name: Alice', 'Role: Data Engineer', 'Location: New York']


# 1 Hard Exercise

# Exercise 6 (Hard): Aggregating Data from Multiple Sources
# Explanation: Write a function `aggregate_data` that takes three lists representing data from different sources (e.g., sales, returns, net profit). Each list contains monthly figures.
# - Use `zip()` to combine these lists into a single list of tuples where each tuple represents a month (sales, returns, net profit).
# - Return a list containing the total amount for each month (sales - returns + net profit).
# Solution:
def aggregate_data(sales, returns, net_profit):
    return [(sale - ret + profit) for sale, ret, profit in zip(sales, returns, net_profit)]

# Example Input:
sales = [1000, 1200, 1100]
returns = [200, 150, 100]
net_profit = [300, 400, 500]
monthly_totals = aggregate_data(sales, returns, net_profit)
print(f"Monthly Totals: {monthly_totals}")

# Example Output:
# Monthly Totals: [1100, 1450, 1500]