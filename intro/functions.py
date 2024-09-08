"""
function that gets 2 ints and returns the result divided between them in double

public static double Devide2Numbers(int num1, int num2){
    ....
    return result
}
"""
# rules:
"""
1. start with def
2. name of function
3. ()
4. parameters
5. :
6. logic inside WITH INDENTATION
"""


def divide_2_numbers(num1, num2):
    result = num1 / num2
    return result


def is_prime(num):
    if type(num) != int or num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


is_prime(5)
is_prime(6.5)
