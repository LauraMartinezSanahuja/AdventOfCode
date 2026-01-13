import itertools

data_file = "example.txt"
# data_file = "data.txt"

result: int = 0
red_tiles: set[tuple[int, int]] = set()

grid_size_x = 0
grid_size_y = 0
grid: list[list[str]] = []

with open(data_file, "r") as file:
    for line in file:
        y, x = line.strip().split(',')
        red_tiles.add((int(x), int(y)))
        if grid_size_x < int(x):
            grid_size_x = int(x)
        if grid_size_y < int(y):
            grid_size_y = int(y)

grid_size_y += 2
grid_size_x += 1

for x in range(grid_size_x + 1):
    grid.append([])
    for y in range(grid_size_y + 1):
        if (x, y) in red_tiles:
            grid[x].append('#')
        else:
            grid[x].append('.')

for row in grid:
    print(''.join(row))

for i in range(len(red_tiles) - 1):
    red_tile1 = red_tiles[i]
    red_tile2 = red_tiles[i + 1]
    # put the Xs

max_rectangle_size = 0

all_pairs = itertools.combinations(red_tiles, 2)
for pair in all_pairs:
    min_x = min(pair[0][0], pair[1][0])
    max_x = max(pair[0][0], pair[1][0])
    min_y = min(pair[0][1], pair[1][1])
    max_y = max(pair[0][1], pair[1][1])

    has_outside_tile = False
    for red_tile in red_tiles:
        if red_tile != pair[0] and red_tile != pair[1]:
            if (red_tile[0] == min_x - 1 or red_tile[0] == max_x + 1) and (
                red_tile[1] == min_y - 1 or red_tile[1] == max_y + 1
            ):
                has_outside_tile = True
                break
    if has_outside_tile:
        continue

    this_rectangle_size = abs(pair[1][0] - pair[0][0] + 1) * abs(pair[1][1] - pair[0][1] + 1)
    # print(f'Found rectangle: {pair}, size: {this_rectangle_size}')
    max_rectangle_size = max(max_rectangle_size, this_rectangle_size)

result = max_rectangle_size
print(f'Result: {result}')
