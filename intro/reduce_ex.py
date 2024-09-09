from functools import reduce

# reduce (function, iterable[, initializer]

# sum from zero
numbers = [1, 2, 3, 4]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)

# sum with initial value
data = [
    {
        'name': 'John',
        'money': 200
    },
    {
        'name': 'John',
        'money': 400
    },
    {
        'name': 'John',
        'money': 100
    },
    {
        'name': 'John',
        'money': 300
    },
]
sum_result = reduce(lambda x, y: x + y["money"], data, 100)
print(sum_result)