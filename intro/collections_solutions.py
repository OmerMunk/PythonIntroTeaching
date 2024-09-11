def list_of_tuples_to_dict(tuples):
    # Convert list of tuples to dictionary
    return dict(tuples)

# Test the function
list_of_tuples = [("name", "Alice"), ("age", 30), ("city", "New York")]
result = list_of_tuples_to_dict(list_of_tuples)
print(result)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


def find_max_sum_tuple(tuples):
    # Find the tuple with the maximum sum of elements
    return max(tuples, key=lambda x: sum(x))

# Test the function
tuples = [(1, 2, 3), (4, 0), (5, 5, 5), (0, -1, 7)]
result = find_max_sum_tuple(tuples)
print(result)  # Output: (5, 5, 5)


def tuple_transform(students):
    # Filter out students with age less than 18
    filtered_students = filter(lambda x: x[1] >= 18, students)

    # Transform the filtered students
    transformed_students = [
        (
            student[0],  # Name
            round(sum(student[2]) / len(student[2]), 2),  # Average grade rounded to 2 decimal places
            "Minor" if student[1] < 21 else "Adult"  # Age category
        )
        for student in filtered_students
    ]

    # Sort the transformed students by average grade in descending order
    sorted_students = sorted(transformed_students, key=lambda x: x[1], reverse=True)

    return sorted_students


# Test the function
students = [
    ("Alice", 20, [85, 90, 95]),
    ("Bob", 17, [70, 80, 60]),
    ("Charlie", 22, [88, 78, 85]),
    ("David", 19, [95, 85, 90])
]
result = tuple_transform(students)
print('_' * 100)
print(result)  # Output: [('David', 90.0, 'Minor'), ('Alice', 90.0, 'Adult'), ('Charlie', 83.67, 'Adult')]
print('_' * 100)



def find_common_stocks(broker_a_stocks, broker_b_stocks):
    # Find the intersection of both sets
    common_stocks = broker_a_stocks & broker_b_stocks

    # Return a sorted list of the common stock symbols
    return sorted(common_stocks)


# Test the function
broker_a_stocks = {"AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"}
broker_b_stocks = {"NFLX", "MSFT", "TSLA", "FB", "AAPL"}
result = find_common_stocks(broker_a_stocks, broker_b_stocks)
print("Common stocks:", result)



def unique_expense_categories(monthly_expenses):
    # Initialize an empty set to collect all unique categories
    all_categories = set()

    # Iterate over each month's expense categories and update the set
    for categories in monthly_expenses:
        all_categories.update(categories)

    # Return the sorted set of all unique categories
    return sorted(all_categories)

# Test the function
monthly_expenses = [
    {"Travel", "Marketing", "Salaries"},
    {"Marketing", "R&D", "Utilities"},
    {"Salaries", "Legal", "Marketing"},
    {"IT", "Travel", "R&D"}
]
result = unique_expense_categories(monthly_expenses)
print("Unique expense categories:", result)




def analyze_frozen_assets(monthly_frozen_assets):
    # Find all unique assets that have been frozen at any point
    all_frozen_assets = set.union(*monthly_frozen_assets)


    # Find assets that were frozen in every month
    always_frozen_assets = set.intersection(*monthly_frozen_assets)

    # Find assets that were frozen in only one month
    frozen_in_one_month = set()
    for asset in all_frozen_assets:
        count = sum(asset in month for month in monthly_frozen_assets)
        if count == 1:
            frozen_in_one_month.add(asset)

    return all_frozen_assets, always_frozen_assets, frozen_in_one_month

# Test the function
monthly_frozen_assets = [
    frozenset({"Asset1", "Asset2", "Asset3"}),
    frozenset({"Asset2", "Asset4", "Asset3"}),
    frozenset({"Asset2", "Asset3", "Asset5"}),
]

all_frozen, always_frozen, one_month_frozen = analyze_frozen_assets(monthly_frozen_assets)
print("All frozen assets:", all_frozen)
print("Always frozen assets:", always_frozen)
print("Frozen in only one month:", one_month_frozen)