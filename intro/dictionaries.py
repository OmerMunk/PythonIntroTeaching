# Dictionary acts like in c#
# iterable, unordered, collection of KEY-VALUE pairs
# each key must be unique

# Creating a dictionary
# 1
student1 = {
    "name": "Avi",
    "age": 45,
    "course": "Python"
}

# 2
student2 = dict(name="Shubu", age=40, course="HTML")

print(student1)
print(student2)

# creating an empty dicitonary
#
dict1 = {}
dict2 = dict()

# access values:
# 1
print(student1["name"])
print(student2["age"])
# print(student2["bla"]) # error

# 2
print(student1.get("course"))
print(student1.get("bla"))
print(student1.get("bla", "N/A"))

# add or modify
print(student1)
student1["address"] = "Lod"
student1["age"] = 20
print(student1)

# delete from dictionary
course = student1.pop("course")
print(student1)
del student1["age"]
print(student1)

# num1 = 5
# num1 = 6
# print(num1)
# del num1
# print(num1)

for key in student1.keys():
    print(key)

for value in student1.values():
    print(value)

for key, value in student1.items():
    print(f"{key}: {value}")

person1 = {
    "name": "Avi",
    "age": 30
}

person2 = {
    # "name": "Oren",
    # "age": 35,
    "city": "Metula"
}

person1.update(person2)
print(person1)

person1.clear()
print(person1)

person2_copy = person2.copy()

# nested dictionaries

students = {
    "omer": {
        "age": 29,
        "grade": 0
    },
    "beni": {
        "age": 10,
        "grade": 97
    }
}

# print(students["beni"]["age"])
for student in students.values():
    for key, value in student.items():
        if key == "age":
            print(value)


# TASK!!!!
"""
Write a function count_frequencies, that gets a list of elements and returns a dictionary
containing the frequency of each element.
example:
input = [10, 20, 35, 14, 10, 20, 15, 17, 20]
output:
{
    10: 2,
    20: 3,
    35: 1
    ...
}
"""
