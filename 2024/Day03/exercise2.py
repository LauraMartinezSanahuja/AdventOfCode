import re

data_path = "2024/Day03/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
regex = "mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)"
do = True

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        muls = re.findall(regex, line)
        print(muls)
        for mul in muls:
            if mul[2] == "do":
                do = True
            elif mul[3] == "don't":
                do = False
            elif do:
                result += int(mul[0]) * int(mul[1])

print(f'Result: {result}')
