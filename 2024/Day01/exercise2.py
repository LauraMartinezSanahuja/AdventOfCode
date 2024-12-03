import os

data_path = "2024/Day01/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
list1 = []
dict2 = {}

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        list1.append(int(line.split("   ")[0]))
        value_list2 = int(line.split("   ")[1])
        if value_list2 in dict2.keys():
            dict2[value_list2] = dict2[value_list2] + 1
        else:
            dict2[value_list2] = 1

print(dict2)
list1.sort()

for i in range(0, len(list1)):
    value = list1[i]
    if value in dict2.keys():
        result += value * dict2[value]

print(f'Result: {result}')
