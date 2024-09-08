# tuple
# set
# frozen set


"""
tuple
like list but immutable
"""

names = ("omer", "avi", "gadi", "shlomi")
print(names[0])
# names.append("aron") # error!!!


# create empty tuple
list1 = [1, 2, 3]
print(list1)
# נניח שעשינו מלא דברים ובא לנו עכשיו לקבע
final_result = tuple(list1)
print(final_result)


#one element
one1 = (4)
one2 = (4,)

print(type(one1))
print(type(one2))
print(type(tuple([])))


# we can do concatination:
tp1 = (1,2,3)
tp2 = (4,5,6)
print(tp1+tp2)

# we can multiply
print(tp1*4)

# we can slice [4:]
print(2 in tp1)
print(2 in tp2)

my_list = [1, 2, 3, 4, 4, 1, 1, 1, 1, 1]
print(my_list)
my_set = {1, 2, 3, 4, 4, 1, 1, 1, 1, 1}
print(my_set)

my_set2= set()
my_set2.add(4)

fronzen = frozenset()


