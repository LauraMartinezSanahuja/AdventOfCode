data_path = "2024/Day04/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid = []
grid_height = -1
grid_width = -1


def is_X_possible(i, j):
    up_right = False
    up_left = False
    down_right = False
    down_left = False
    if i - 1 >= 0:
        if j - 1 >= 0:
            # UP-LEFT
            up_left = True
        if j + 1 < grid_width:
            # UP-RIGHT
            up_right = True
    if i + 1 < grid_height:
        if j - 1 >= 0:
            # DOWN-LEFT
            down_left = True
        if j + 1 < grid_width:
            # DOWN-RIGHT
            down_right = True
    return up_right and up_left and down_right and down_left


with open(data_path + "/" + data_file, "r") as file:
    i = 0
    for line in file:
        grid.append([])
        j = 0
        for letter in line:
            grid[i].append(letter)
            j = j + 1
        grid_width = j
        i = i + 1
    grid_height = i

for i in range(0, grid_height):
    for j in range(0, grid_width):
        if grid[i][j] == "A" and is_X_possible(i, j):
            if (
                (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S")
                or (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M")
            ) and (
                (grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S")
                or (grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M")
            ):
                result += 1

print(f'Result: {result}')
