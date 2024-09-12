arr = []

for i in range(5):
    print(i)

for i in range(15, 21):
    print(i)

for i in range(17, 50, 10):
    print(i)


for i in range(5000, 2000, -250):
    print(i)


grades_list = []
num_of_students = 10

for i in range(num_of_students):
    num = int(input("enter a grade: "))
    grades_list.append(num)

avg = sum(grades_list) / len(grades_list)
print(f"grades list is {grades_list}")
print(f"avg is {avg}")