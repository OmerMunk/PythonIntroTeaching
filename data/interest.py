import csv

csv_file_path ='export (1).csv'

data_list = []

with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_list = list(csv_reader)

# print(data_list[-365::30])
for row in data_list[-3650::365]:
    print("\n")
    for key, value in row.items():
        if value != "ריבית בנק ישראל" and key != "Time":
            print(f'key:{key}, value:{value}')
