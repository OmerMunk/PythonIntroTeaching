# Topic Recap: Tuples (Data Engineering Oriented)

# 3 Easy Exercises

# Exercise 1 (Easy): Data Record Creation
# Explanation: Write a Python program that creates a tuple representing a data record of a data engineer, containing the name, age, and years of experience.
# Guidance: Use a tuple to store immutable data values.
# Solution:
data_engineer = ("Alice", 29, 5)  # (name, age, years of experience)
print(f"Data Engineer Record: {data_engineer}")

# Example Input:
# (No input required)
# Example Output:
# Data Engineer Record: ('Alice', 29, 5)


# Exercise 2 (Easy): Accessing Tuple Elements
# Explanation: Write a program that takes a tuple representing a database connection configuration (host, port, database name) and prints each element.
# Guidance: Use tuple indexing to access and print each element.
# Solution:
db_config = ("localhost", 5432, "sales_db")
print(f"Host: {db_config[0]}")
print(f"Port: {db_config[1]}")
print(f"Database Name: {db_config[2]}")

# Example Input:
# (No input required)
# Example Output:
# Host: localhost
# Port: 5432
# Database Name: sales_db


# Exercise 3 (Easy): Count Elements in a Tuple
# Explanation: Write a program that takes a tuple of department names and counts how many times "Data Engineering" appears in it.
# Guidance: Use the `count()` method of a tuple.
# Solution:
departments = ("Data Engineering", "Data Science", "Data Engineering", "ML Engineering")
count_data_engineering = departments.count("Data Engineering")

print(f"'Data Engineering' appears {count_data_engineering} times.")

# Example Input:
# (No input required)
# Example Output:
# 'Data Engineering' appears 2 times.


# 2 Medium Exercises

# Exercise 4 (Medium): Unpacking Tuples for Data Transformation
# Explanation: Given a tuple containing multiple data points (temperature, humidity, pressure), write a Python program that unpacks the tuple into individual variables and prints them formatted.
# Solution:
data_point = (25.4, 60, 1012)  # (temperature, humidity, pressure)
temperature, humidity, pressure = data_point

print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")

# Example Input:
# (No input required)
# Example Output:
# Temperature: 25.4°C
# Humidity: 60%
# Pressure: 1012 hPa


# Exercise 5 (Medium): Tuple Conversion for Data Cleansing
# Explanation: Write a program that takes a list of tuples, each representing a data row (id, name, age), and converts it into a cleaned-up format by filtering out any rows where the age is below 18.
# Solution:
data_rows = [(1, "Alice", 25), (2, "Bob", 17), (3, "Charlie", 30)]
cleaned_data = [row for row in data_rows if row[2] >= 18]

print(f"Cleaned Data: {cleaned_data}")

# Example Input:
# (No input required)
# Example Output:
# Cleaned Data: [(1, 'Alice', 25), (3, 'Charlie', 30)]


# 1 Hard Exercise

# Exercise 6 (Hard): Tuple-Based Aggregation for Data Analysis
# Explanation: Create a program that takes a list of tuples representing sales data for different products (product_name, units_sold, unit_price) and calculates:
# - The total revenue generated for each product.
# - The product with the highest revenue.
# Solution:
sales_data = [
    ("Laptop", 10, 1500),
    ("Smartphone", 20, 800),
    ("Tablet", 15, 600),
    ("Smartwatch", 5, 300)
]

# Calculate total revenue for each product
product_revenue = [(product, units_sold * unit_price) for product, units_sold, unit_price in sales_data]

# Find the product with the highest revenue
highest_revenue_product = max(product_revenue, key=lambda x: x[1])

# Print results
for product, revenue in product_revenue:
    print(f"Total revenue for {product}: ${revenue:.2f}")

print(f"Product with the highest revenue: {highest_revenue_product[0]} with ${highest_revenue_product[1]:.2f}")

# Example Input:
# (No input required)
# Example Output:
# Total revenue for Laptop: $15000.00
# Total revenue for Smartphone: $16000.00
# Total revenue for Tablet: $9000.00
# Total revenue for Smartwatch: $1500.00
# Product with the highest revenue: Smartphone with $16000.00
