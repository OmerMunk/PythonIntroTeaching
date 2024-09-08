numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter - to filter out or in just the things we want.

# filter to extract only the even numbers

# filter gets 2 params:
# function, iterable
# the function needs to be a function that returns true a false
# the iterable - an object that we can iterate on.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# () => {}