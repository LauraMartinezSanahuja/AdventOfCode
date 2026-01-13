import itertools

data_file = "example.txt"
data_file = "data.txt"

result: int = 0
red_tiles: set[tuple[int, int]] = set()

with open(data_file, "r") as file:
    for line in file:
        red_tiles.add(tuple(int(x) for x in line.strip().split(',')))
    red_tiles = sorted(red_tiles)

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
    #print(f'Found rectangle: {pair}, size: {this_rectangle_size}')
    max_rectangle_size = max(max_rectangle_size, this_rectangle_size)

result = max_rectangle_size
print(f'Result: {result}')
