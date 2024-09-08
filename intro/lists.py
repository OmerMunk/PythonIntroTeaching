# empty list:
# 1
list1 = []
# 2
list2 = list()


numbers = [16, 52, -300, 4,-300, 5]

# optional BUT not recommended
numbers2 = [1, 2, 3, 4, "omer"]

print(numbers)
print(type(numbers))
print(numbers[2])
print(numbers[1:4])

print(numbers[::-1])

print(f"number before append: {numbers}")
numbers.append(20)
numbers.insert(2, 10)
print(f"number after append: {numbers}")
print(numbers.pop())
print(numbers)
print(numbers.index(-300))
numbers.copy()
numbers.sort()
print(numbers)







