data_path = "2024/Day04/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid = []
grid_height = -1
grid_width = -1


def get_valid_directions(i, j):
    valid_directions = []
    if i - 1 >= 0:
        # UP
        valid_directions.append([-1, 0])
        if j - 1 >= 0:
            # UP-LEFT
            valid_directions.append([-1, -1])
        if j + 1 < grid_width:
            # UP-RIGHT
            valid_directions.append([-1, 1])
    if i + 1 < grid_height:
        # DOWN
        valid_directions.append([1, 0])
        if j - 1 >= 0:
            # DOWN-LEFT
            valid_directions.append([1, -1])
        if j + 1 < grid_width:
            # DOWN-RIGHT
            valid_directions.append([1, 1])
    if j - 1 >= 0:
        # LEFT
        valid_directions.append([0, -1])
    if j + 1 < grid_width:
        # RIGHT
        valid_directions.append([0, 1])
    return valid_directions


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
        if grid[i][j] == "X":
            valid_directions = get_valid_directions(i, j)
            for valid_direction in valid_directions:
                if grid[i + valid_direction[0]][j + valid_direction[1]] == "M":
                    valid_directions_M = get_valid_directions(
                        i + valid_direction[0], j + valid_direction[1]
                    )
                    if (
                        valid_direction in valid_directions_M
                        and grid[i + 2 * valid_direction[0]][j + 2 * valid_direction[1]] == "A"
                    ):
                        valid_directions_A = get_valid_directions(
                            i + 2 * valid_direction[0], j + 2 * valid_direction[1]
                        )
                        if (
                            valid_direction in valid_directions_A
                            and grid[i + 3 * valid_direction[0]][j + 3 * valid_direction[1]] == "S"
                        ):
                            result += 1

print(f'Result: {result}')
