# working with files

# open and close file
# file flags:
"""
r - read
w - write
a - append
r+ - read and write
"""

import os
import json

file_path = 'data.txt'
# open the file
file = open(file_path, 'r')

# closing
file.close()

#

with open(file_path, 'r') as f:
    print("opened the file")
    pass
    pass
    pass
    pass
    pass
    print("closing the file")

print("the file is closed")

try:
    pass
except:
    pass

print("23123")

with open(file_path, 'r') as file:
    # read the entire file
    content = file.read()
    print(content)

    print('-' * 100)
    # move to the start of the file
    file.seek(0)
    # read part
    part_of_content = file.read(10)
    print(part_of_content)
    print('-' * 100)
    part_of_content = file.read(10)
    print(part_of_content)

    # read one line at a time
    file.seek(0)
    line = file.readline()
    while line:
        print(f"line is: {line}")
        line = file.readline()

    # read all lline to a list
    file.seek(0)
    lines = file.readlines()
    print(lines)

output_path = 'output.txt'
with open(output_path, 'w') as file:
    file.write("This is the first line.\n")
    file.write("another line.\n")

# people = [("avi", 40), ('john', 35), ('beni', 10)]
# with open('people.csv', 'w') as file:
#     columns = ["name", "age"]
#     first_line = ",".join(columns)
#     file.write(f'{first_line}\n')
#     for person in people:
#         file.write(f'{person[0]},{person[1]}\n')
#     # for name, age in people:
#     #     file.write(f'{name},{age}\n')


with open('people.csv', 'a') as file:
    new_people = [("Omer", 29)]
    for person in new_people:
        file.write(f'{person[0]},{person[1]}\n')

# delete file

file_name_to_delete = 'people1.csv'
if os.path.exists(file_name_to_delete):
    os.remove(file_name_to_delete)
    print(f"deleted {file_name_to_delete}")
else:
    print(f"file {file_name_to_delete} does not exist")

# working with json:
people = {
    "person1": {
        "name": "avi",
        "money": -500
    },
    "person2": {
        "name": "davi",
        "money": 1_000_000
    }
}

list_people = [
     {
        "name": "avi",
        "money": -500
    },
     {
        "name": "davi",
        "money": 1_000_000
    }
]
with open('people.json', 'w') as file:
    json.dump(list_people, file)

# with open('people.json', 'r') as file:
#     people = json.load(file)
#     print(people)
#     print(type(people))
#
# people.update({"person3": {
#     "name": "shubulu",
#     "money": -100
# }})
# people.update({"person4": [1, 2, 3]})
#
# with open('people.json', 'w') as file:
#     json.dump(people, file)
