"""
FP - Functional Programming
HOF - Higher Order Function (1. function that takes af function)
2. function that returns a function
3. both
FIRST CLASS CITIZENS
piping
function composition
memoization
function in function
immutable
PURE - no side effect, deterministic

"""

def pipe(initial_value, *funcs):
    value = initial_value
    for func in funcs:
        value = func(value)
    return value


def power_2(num):
    return num ** 2

def plus_itself(num):
    return num + num

def modulu_minus_1(num):
    return num % num-1



result = pipe(4, plus_itself, modulu_minus_1, power_2)
print(result)



