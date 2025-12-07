import re

data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid: list[list[str]] = []

with open(data_file, "r") as file:
    for line in file:
        line = re.sub(r"\s", " ", line)
        values = line.split(" ")
        grid.append([value for value in values if value != ""])

    for col in range(len(grid[0])):
        if grid[-1][col] == "+":
            partial_result = 0
            for row in grid:
                if row[col] != "+":
                    partial_result += int(row[col])
        else:
            partial_result = 1
            for row in grid:
                if row[col] != "*":
                    partial_result *= int(row[col])
        result += partial_result


print(f'Result: {result}')
