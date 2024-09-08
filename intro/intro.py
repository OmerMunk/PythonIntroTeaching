# prints
from string import printable

print("Hello I love python")
print('Hello I love python')
name = "Omer"
print("Hi, I am ", name)

# string interpolation
print(f"Hi i am {name}")

# by default, print() function does \n at the end of a print
# it goes down 1 line.
print("line 1")
print("line 2")

# optional parameter of the print function
print("Hi i am ", end="")
print(name)

# print names with | between them
name1 = "Avi"
name2 = "Tsachi"
name3 = "Jake"
print(name1, end="|")
print(name2, end="|")
print(name3)

initial_text = "My name is "
name = "Shuki"
final_string = initial_text + name
print(final_string)

initial_string = ""
initial_string += "1"
initial_string += "2"
print(initial_string)


# print(5 + 5) # 10
# print(2+ 3 + "5") # Error
# print("5" + 5 + 7) # Error
# print("5" + "5") # 55

print(12/3) # when we divide 2 integers - we will get float
print(5/2)
print(5//2)
print(5*2) # multiplication
print(5**2) # power

# new line: \n
# tab: \t
# ": \"
print("omer omer")
print("omer\nomer")
print("omer\tomer")

# output: Hi my name is "omer"
print("Hi my name is \"omer\"")
print('Hi my name is "omer"')
print("Hi my name is 'omer'")


x = 5
print(x)
x = "omer"
print(x)

# bool
t1 = True
t2 = False



# typing in python



x = 25
y = "Shubuli"
z = False
print(f"the type of x is: {type(x)}")
print(f"the type of y is: {type(y)}")
print(f"the type of z is: {type(z)}")


# casting
num1 = 457
str1 = str(num1)

str2 = "0056"
print(int(str2))

# error!
# str3 = "7omer3"
# print(int(str3))

# error
# str3 = "3.78"
# print(int(str3))

str3 = "3.78"
print(float(str3))


# slicing
word = "Rabbit"
print(word[0])
print(word[4])

# length of word
print(len(word))
print(word[len(word)-1])

# in python we can access indexes from the end by -
print(word[-2])



str4 = "Hello! I love Python becasue it was so hard on C#"
# [start:] from the start we gave - to the nd
print(str4[1:])

# [:end] from the start, to the end we gave
print(str4[:10])

#[start:end] from the start we gave, to the end we gave
print(str4[15:20])

print(str4[1:20])
print(str4[1:20:3]) #1, 4, 7, 10, 13, 16, 19


str5 = "shubulu"
print(str5[-1::-1])

#upper, lower, split, replace, strip

test_string = "          Hello      I     am omer      "
print(test_string.upper())
print(test_string.lower())
print(test_string.split())
print(test_string.replace("e", "!"))
print(test_string.strip())


name = input("hi what is your name?")
print(f"hi {name}")
age = int(input("hi what is your age?"))
print(f"wow! next year you will be {age+1}")












