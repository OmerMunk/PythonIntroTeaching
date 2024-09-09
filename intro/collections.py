# tuple
# set
# frozen set


"""
tuple
like list but immutable
"""

names = ("omer", "avi", "gadi", "shlomi")
print(names[0])
# names.append("aron") # error!!!


# create empty tuple
list1 = [1, 2, 3]
print(list1)
# נניח שעשינו מלא דברים ובא לנו עכשיו לקבע
final_result = tuple(list1)
print(final_result)


#one element
one1 = (4)
one2 = (4,)

print(type(one1))
print(type(one2))
print(type(tuple([])))


# we can do concatination:
tp1 = (1,2,3)
tp2 = (4,5,6)
print(tp1+tp2)

# we can multiply
print(tp1*4)

# we can slice [4:]
print(2 in tp1)
print(2 in tp2)

my_list = [1, 2, 3, 4, 4, 1, 1, 1, 1, 1]
print(my_list)
my_set = {1, 2, 3, 4, 4, 1, 1, 1, 1, 1}
print(my_set)

my_set2= set()
my_set2.add(4)

fronzen = frozenset()



"""
TUPPLES
easy:
Write a function list_of_tuples_to_dict that takes a list of tuples, where each tuple contains two elements: a key and a value. Convert this list of tuples into a dictionary and return it.
# Example Input
list_of_tuples = [("name", "Alice"), ("age", 30), ("city", "New York")]

# Example Output
# {'name': 'Alice', 'age': 30, 'city': 'New York'}


medium:
Write a function find_max_sum_tuple that takes a list of tuples, where each tuple contains numbers. The function should return the tuple with the maximum sum of its elements.

# Example Input
tuples = [(1, 2, 3), (4, 0), (5, 5, 5), (0, -1, 7)]

# Example Output
# (5, 5, 5)


hard:
Write a function tuple_transform that takes a list of tuples. Each tuple consists of a name (string), an age (integer), and a list of grades (list of integers).

	1.	Filter out tuples where the age is less than 18.
	2.	Transform the remaining tuples to a new structure where:
	•	The first element is the name.
	•	The second element is the average of the grades rounded to 2 decimal places.
	•	The third element is a string “Minor” if the age is below 21 or “Adult” otherwise.
	3.	Sort the resulting tuples by the average grade in descending order and return the sorted list.


# Example Input
students = [
    ("Alice", 20, [85, 90, 95]),
    ("Bob", 17, [70, 80, 60]),
    ("Charlie", 22, [88, 78, 85]),
    ("David", 19, [95, 85, 90])
]

# Example Output
# [('Alice', 90.0, 'Minor'), ('David', 90.0, 'Minor'), ('Charlie', 83.67, 'Adult')]



"""



"""
SETS AND FROZEN SETS:

easy:
Two brokers, Broker A and Broker B, provide a list of stock symbols they currently have available for trading. Write a function find_common_stocks that takes two sets representing these stock symbols and returns a sorted list of symbols that both brokers have in common.

# Example Input
broker_a_stocks = {"AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"}
broker_b_stocks = {"NFLX", "MSFT", "TSLA", "FB", "AAPL"}

# Example Output
# ['AAPL', 'MSFT', 'TSLA']

medium:
A financial analyst tracks monthly expenses for a company and categorizes them into various groups (e.g., “Travel”, “Marketing”, “Salaries”). Write a function unique_expense_categories that takes a list of sets, where each set represents expense categories for a given month, and returns a sorted set of all unique expense categories across all months.

# Example Input
monthly_expenses = [
    {"Travel", "Marketing", "Salaries"},
    {"Marketing", "R&D", "Utilities"},
    {"Salaries", "Legal", "Marketing"},
    {"IT", "Travel", "R&D"}
]

# Example Output
# {'IT', 'Legal', 'Marketing', 'R&D', 'Salaries', 'Travel', 'Utilities'}


hard:


A financial institution is tracking assets that have been frozen by regulatory authorities due to compliance issues. Each frozenset contains the asset IDs frozen in a particular month. Write a function analyze_frozen_assets that takes a list of frozensets representing monthly frozen assets and returns:

	1.	A set of all unique asset IDs that have been frozen at any point.
	2.	A set of asset IDs that were frozen in every month.
	3.	A set of asset IDs that were frozen in only one month.
	
	
	
# Example Input
monthly_frozen_assets = [
    frozenset({"Asset1", "Asset2", "Asset3"}),
    frozenset({"Asset2", "Asset4", "Asset3"}),
    frozenset({"Asset2", "Asset3", "Asset5"}),
]

# Example Output
# All frozen assets: {'Asset1', 'Asset2', 'Asset3', 'Asset4', 'Asset5'}
# Always frozen assets: {'Asset2', 'Asset3'}
# Frozen in only one month: {'Asset1', 'Asset4', 'Asset5'}



"""


