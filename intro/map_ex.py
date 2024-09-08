# map

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)



ages = [16, 19, 20, 21, 14, 14, 18, 16, 17, 17, 16, 18, 20, 21, 21, 23, 22]
# result needed: can drink alcohol in israel only (21 >age >= 18)
# result needed: can drink alcohol in israel and us (age >= 21)
# result needed: cant drink alcohol(age < 18)

"""
person number 1 can drink alcohol in israel only
person number 2 can drink alcohol in israel and us
...
"""
MIN_AGE_ALCOHOL_US = 21
MIN_AGE_ALCOHOL_ISRAEL = 18

def alcohol_state(age):
    if MIN_AGE_ALCOHOL_US > age >= MIN_AGE_ALCOHOL_ISRAEL:
        return "can drink alcohol in israel only"
    elif age >= MIN_AGE_ALCOHOL_US:
        return "can drink alcohol in israel and us"
    else:
        return "cant drink alcohol"

results = list(map(alcohol_state ,ages))
# for i in range(len(results)):
#     print(f"person {i +1} {results[i]}")

for i, result in enumerate(results):
    print(f"person {i + 1} {result}")







