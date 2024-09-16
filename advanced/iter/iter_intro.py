numbers = [1, 2, 3, 4]
iter_obj = iter(numbers)
# iter works on every collection

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

for num in numbers:
    print(num)

details = {'name': 'omer', 'age': 29}
iter_obj = iter(details)
print(next(iter_obj))
print(next(iter_obj))
dict()
