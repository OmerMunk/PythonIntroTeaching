# Topic Recap: Enumerate (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Indexing Items in a List
# Explanation: Write a function `index_items` that takes a list of data entries and prints each entry along with its index using `enumerate`.
# Solution:
def index_items(data_entries):
    for index, entry in enumerate(data_entries):
        print(f"Index: {index}, Entry: {entry}")

# Example Input:
data_entries = ["Data Engineer", "Data Scientist", "ML Engineer", "BI Specialist"]
index_items(data_entries)

# Example Output:
# Index: 0, Entry: Data Engineer
# Index: 1, Entry: Data Scientist
# Index: 2, Entry: ML Engineer
# Index: 3, Entry: BI Specialist


# Exercise 2 (Easy): Enumerate with Custom Start Index
# Explanation: Write a function `list_projects` that takes a list of project names and prints each project name with a custom starting index using `enumerate`.
# Solution:
def list_projects(projects, start_index):
    for index, project in enumerate(projects, start=start_index):
        print(f"Project {index}: {project}")

# Example Input:
projects = ["Customer Segmentation", "Sales Forecasting", "Anomaly Detection"]
list_projects(projects, 1)

# Example Output:
# Project 1: Customer Segmentation
# Project 2: Sales Forecasting
# Project 3: Anomaly Detection


# Exercise 3 (Easy): Enumerate for Data Validation
# Explanation: Write a function `validate_data` that takes a list of data entries and prints a warning message for each entry that is an empty string, along with its index, using `enumerate`.
# Solution:
def validate_data(data_entries):
    for index, entry in enumerate(data_entries):
        if entry == "":
            print(f"Warning: Empty entry found at index {index}!")

# Example Input:
data_entries = ["Alice", "", "Bob", "Charlie", ""]
validate_data(data_entries)

# Example Output:
# Warning: Empty entry found at index 1!
# Warning: Empty entry found at index 4!


# 2 Medium Exercises

# Exercise 4 (Medium): Enumerate for Data Transformation
# Explanation: Write a function `transform_data` that takes a list of numerical data points and transforms them into a dictionary where each key is the index and each value is the squared value of the data point.
# Solution:
def transform_data(data_points):
    return {index: value ** 2 for index, value in enumerate(data_points)}

# Example Input:
data_points = [2, 3, 5, 7]
transformed_data = transform_data(data_points)
print(f"Transformed Data: {transformed_data}")

# Example Output:
# Transformed Data: {0: 4, 1: 9, 2: 25, 3: 49}


# Exercise 5 (Medium): Enumerate and Filter Data
# Explanation: Write a function `filter_data_by_index` that takes a list of data points and filters out data points where the index is even using `enumerate`.
# Solution:
def filter_data_by_index(data_points):
    return [value for index, value in enumerate(data_points) if index % 2 != 0]

# Example Input:
data_points = [10, 15, 20, 25, 30, 35]
filtered_data = filter_data_by_index(data_points)
print(f"Filtered Data: {filtered_data}")

# Example Output:
# Filtered Data: [15, 25, 35]


# 1 Hard Exercise

# Exercise 6 (Hard): Data Processing with Enumerate
# Explanation: Write a function `process_sales_data` that takes a list of sales amounts and applies the following rules:
# - For sales amounts at even indexes, apply a 10% discount.
# - For sales amounts at odd indexes, apply a 15% surcharge.
# Return the new list of processed sales amounts.
# Solution:
def process_sales_data(sales):
    return [sale * 0.9 if index % 2 == 0 else sale * 1.15 for index, sale in enumerate(sales)]

# Example Input:
sales = [100, 200, 300, 400, 500]
processed_sales = process_sales_data(sales)
print(f"Processed Sales: {processed_sales}")

# Example Output:
# Processed Sales: [90.0, 230.0, 270.0, 460.0, 450.0]
