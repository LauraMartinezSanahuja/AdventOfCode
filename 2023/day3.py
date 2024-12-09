grid = []

with open("AoC2023/day3.txt", "r") as file:
    for line in file:
        grid_line = []
        for character in line:
            grid_line.append(character)
        grid.append(grid_line)
    print(grid)

part_number = []

for i in range(0, len(grid)):
    number = ''
    for j in range(0, len(grid[i])):
        value = grid[i][j]
        if value == ".":
            continue