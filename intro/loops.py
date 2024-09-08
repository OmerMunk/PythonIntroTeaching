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



# ex1
fruits = ['apple', 'orange', 'pear', "strawberry", "peach"]
for fruit in fruits:
    print(f"fruit is: {fruit}")


# ex2
fruits = ['apple', 'orange', 'pear', "strawberry", "peach"]
for i in range(len(fruits)):
    print(f"fruit in index {i} is: {fruits[i]}")


# ex3 1
grades = [100, 90, 87, 88, 0, 75, 100, 90, 89, 30]
count = 0
sum_grades = 0
for grade in grades:
    count += 1
    sum_grades += grade
avg = sum_grades / count
print(avg)

# ex3 2
grades = [100, 90, 87, 88, 0, 75, 100, 90, 89, 30]
sum_grades = 0
for grade in grades:
    sum_grades += grade
avg = sum_grades / len(grades)
print(avg)

# ex3 2
grades = [100, 90, 87, 88, 0, 75, 100, 90, 89, 30]
sum_grades = sum(grades)
avg = sum_grades / len(grades)
print(avg)

# ex4
grades = [100, 90, 87, 88, 0, 75, 100, 90, 89, 30]
maximum = grades[0]
for grade in grades:
    if grade > maximum:
        maximum = grade
print(maximum)

maximum = max(grades)

grades.sort()
print(grades[-1])


#ex 5
for i in range(10):
    print(f"5 x {i+1} = {5 * (i + 1)}")


str1 = "Hello Kodcode, Shubulu"
vowels = "aeiou"
vowels += vowels.upper()
count = 0
for char in str1:
    if char in vowels:
        count += 1

print(f"the amount of vowels is: {count}")




# break continue

# if we want to iterate over all the number 0-9
# stop when we get to 5 (not included)
# print odd numbers only
# use for, in, range, if, elif, break, continue


for num in range(10):
    if num == 5:
        break
    elif num % 2 == 0:
        continue
    print(num)



# create a loop, that finds all the prime numbers from 2 to 25
# prime number is a number that can be divided only by 1 and itself.
for num in range(2, 260000):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")

print("FINISH!")







