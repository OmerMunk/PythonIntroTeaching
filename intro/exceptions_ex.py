# https://www.w3schools.com/python/python_ref_exceptions.asp

# errors
# 1. understand what it is
# 2. try except
# 3. how to handle multiple ex
# 4. else with try and except
# 5. finally
# 6. raise


# try:
#     # risky code
# except Exception:
#     # handle exception

try:
    number = int(input("enter a number: "))
    result = 100 / number
    print(f'result is {result}')
except ZeroDivisionError:
    print("Invalid input, cannot divide by zero, please try again")
except ValueError:
    print("Invalid input, please enter a valid integer")
except Exception as e:
    print(f"unknown error: {e}, please try again ")

#
# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
# except (ValueError, ZeroDivisionError) as e:
#     print(f"An error occurred: invalid input: {e}")



# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
# except (ValueError, ZeroDivisionError) as e:
#     print(f"An error occurred: {e}")
# else:
#     print("No errors occurred. Result is:", result)
#
# print("THIS WILL RUN ANYWAY")


# try except finally
# never mind if the try completed or the except happend, the finally will run

# try:
#     file = open("my_text.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     file.close()



# ZeroDivisionError
# ValueError


def check_age(age):
    if (age < 0):
        # raise ValueError("Age must be greater than or equal to zero")
        raise Exception("Age must be greater than or equal to zero")


try:
    age = int(input("Enter your age: "))
    check_age(age)
# except ValueError as e:
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("valid age!")
