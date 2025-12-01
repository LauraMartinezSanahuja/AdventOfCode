data_file = "example.txt"
data_file = "data.txt"

result: int = 0
dial: int = 50

with open(data_file, "r") as file:
    for line in file:
        if line.startswith("L"):
            dial -= int(line[1:])
        elif line.startswith("R"):
            dial += int(line[1:])
        dial %= 100
        if dial == 0:
            result += 1

print(f'Result: {result}')
