from itertools import groupby

data = [
    ("TerroristA", "18:40", (12, 17)),
    ("TerroristB", "12:40", (18, 17)),
    ("TerroristC", "19:40", (20, 7)),
    ("TerroristA", "11:40", (300, -17)),
    ("TerroristB", "17:40", (350, -17))
]

sorted_data = sorted(data, key=lambda terrorist: terrorist[0])

print(sorted_data)



for key, group in groupby(sorted_data, key=lambda terrorist: terrorist[0]):
    print(f"key: {key}, group: {list(group)}")