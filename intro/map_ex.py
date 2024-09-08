# map

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


ages = [16, 19, 20, 21, 14, 14, 18, 16, 17, 17, 16, 18, 20, 21, 21, 23, 22]
# result needed: can drink alcohol in israel only (20 >age >= 18)
# result needed: can drink alcohol in israel and us (age >= 21)
# result needed: cant drink alcohol(age < 18)

"""
person number 1 can drink alcohol in israel only
person number 2 can drink alcohol in israel and us
...
"""

