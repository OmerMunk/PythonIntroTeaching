# args
# kwargs
# isinstance
# practice collections
# list comperhension
# * , **


list_of_num_list = [
    [1, -5, 3],
    [1, 3, 300],
    [200, 2, 3],
]

maximums = map(lambda x: max(x), list_of_num_list)
print(list(maximums))