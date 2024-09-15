########## args and kwargs ##########


# 1. Introduction to Function Arguments
"""
positional arguments
def(num1, str1):
    pass

keyword arguments
if there are positional arguments, they must come BEFORE keyword args
def(num1, str1="shubulu"): (what if the user didnt provide the keyword arguments)
    pass

default arguments (the = after the keyword)

variable-length arguments
*args, **kwargs
"""



# 2. Understanding * args
"""
*args allow us to pass a variable number of non-keyword arguments
when we do *args, it collects additional positional arguments as a tuple
"""

def print_numbers(*args):
    print(type(args))
    for number in args:
        print(number)

def person_details(*args):
    name = args[0]
    age = args[1]

print_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)

person_details('Omer', 29)


def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result


def calculate(calculate_type, *args):
    if calculate_type == 'multiply':
        total = 1
        for number in args:
            total *= number
        return total
    elif calculate_type == 'add':
        total = 0
        for number in args:
            total += number
        return total

print(calculate('multiply', 1, 2, 3, 4, 5, 6, 7, 8, 9))


# the * operator

def add(a, b, c):
    return a+b+c

numbers = (1,2,3)
print(add(*numbers))




# 3. Understanding ** kwargs

def print_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_info(name='Omer', age='12', city='TA')


def create_user(name, age, **kwargs):
    user = {'userName': name, 'userAge': age}
    user.update(kwargs)
    return user

user1 = create_user('Omer', 12, city='TA')

# unpacking with **

def say_hello(name, age, city):
    print(f'Hello {name}, you are {age} years old. From {city}')

person = {'age': 20,'name': 'Shubi',  'city': 'Taipei'}
# say_hello(person['name'], person['age'], person['city'])
say_hello(**person)


# 4. Using * and ** in Function Calls



# 5. Best Practices with *args and ** kwargs
# 6. Advanced Use Cases
# 7. Key Points