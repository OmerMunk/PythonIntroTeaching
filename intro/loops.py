# range with 1 param: from 0 to n-1
for i in range(10):
    print(i)

print(range(10))
print(list(range(10)))

# # range with 2 param: from x to y-1
for i in range(200, 217):
    print(i)


for i in range(-5, 2):
    print(i)


# # range with 2 param: from x to y-1, with delta of z (jumps)
for i in range(15, 100, 10):
    print(i)

numbers = [67, 900, -400, 30, 15]
for i in range(len(numbers)):
    print(numbers[i])

for num in numbers:
    print(num)



"""
ex1: create a list with 5 fruits
print all fruits in this format:
"fruit is: ??"


ex2: create a list with 5 fruits
print all fruits in this format:
"fruit in index ?? is: ??"

ex3: write a code that iterates over 10 grades, 
and prints the average of them.
1. using loop
2. dont use loop

ex4: find the maximum of a list
1. using loop
2. dont use loop 
3. dont use loop (2 different ways)


ex5: create code that can print the following:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50


ex6: create a code that counts the vowels of a word


"""

