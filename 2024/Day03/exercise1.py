import re

data_path = "2024/Day03/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
#regex="mul\((?P<value1>\d+),(?P<value2>\d+)\)"
regex = "mul\((\d+),(\d+)\)"

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        muls = re.findall(regex, line)
        for mul in muls:
            result += int(mul[0]) * int(mul[1])

print(f'Result: {result}')
