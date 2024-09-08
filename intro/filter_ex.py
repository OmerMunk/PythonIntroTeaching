numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter - to filter out or in just the things we want.

# filter to extract only the even numbers

# filter gets 2 params:
# function, iterable
# the function needs to be a function that returns true a false
# the iterable - an object that we can iterate on.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8, 10]


vowels = ['a', 'e', 'i', 'o', 'u']
str1= "Hello world"
filtered_with_no_vowels = filter(lambda x: x not in vowels, str1)
print(list(filtered_with_no_vowels))


# create a list with 10 names
# filter only the words with maximum length of 5
words = ["Abraha", "avi", "seth", "shlomo", "shalom", "gadi", "david", "dud"]
MAX_LENGTH = 5

short_words = list(filter(lambda word: len(word) <= MAX_LENGTH, words))


