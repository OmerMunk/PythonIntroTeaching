#  zip(*iterables)
# list1, list2, list3
# zip(list1, list2)
# zip(list1, list2, list3)

# how to zip elements together
names = ["Abraham", "Yitshak", "Yaakov", "Metushelah"]
ages = [137, 185, 147, 969]
properties = ["Yazam", "Leader", "Fighter", "Zaken"]
combined = list(zip(names, ages))
combined_extra = list(zip(names, ages, properties))
print(combined)
print(combined_extra)


#this is how to unzip
unzipped_names, unzipped_ages, unzipped_properties = zip(*combined_extra)
print(f"unzipped names: {unzipped_names}")
print(f"unzipped unzipped_ages: {unzipped_ages}")
print(f"unzipped unzipped_properties: {unzipped_properties}")
