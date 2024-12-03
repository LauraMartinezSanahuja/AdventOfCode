import os

data_path = "2024/Day01/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
list1 = []
list2 = []

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        list1.append(int(line.split("   ")[0]))
        list2.append(int(line.split("   ")[1]))

list1.sort()
list2.sort()

for i in range(0, len(list1)):
    result += abs(list2[i] - list1[i])

print(f'Result: {result}')
