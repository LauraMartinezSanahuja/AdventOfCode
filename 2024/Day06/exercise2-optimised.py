data_path = "2024/Day06/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
room = []
room_height = 0
room_width = 0
guard_initial_row = -1
guard_initial_column = -1
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # UP, RIGHT, DOWN, LEFT
directions_sign = ["^", ">", "v", "<"]


def move_guard(map):
    guard_row = guard_initial_row
    guard_column = guard_initial_column
    guard_direction = 0
    is_guard_moving = True
    is_guard_in_loop = False
    visited_tiles = set()
    visited_tiles_directions = {}

    visited_tiles.add((guard_row, guard_column))
    visited_tiles_directions[(guard_row, guard_column)] = [False] * 4
    visited_tiles_directions[(guard_row, guard_column)][guard_direction] = True

    while is_guard_moving and not is_guard_in_loop:
        next_column = guard_column + directions[guard_direction][0]
        next_row = guard_row + directions[guard_direction][1]
        if next_row < 0 or next_row >= room_height or next_column < 0 or next_column >= room_width:
            is_guard_moving = False
            break

        if map[next_row][next_column] == "#" or map[next_row][next_column] == "O":
            guard_direction = (guard_direction + 1) % 4
            continue

        guard_column = next_column
        guard_row = next_row
        if (guard_row, guard_column) in visited_tiles and (
            visited_tiles_directions[(guard_row, guard_column)][guard_direction]
        ) == True:
            is_guard_in_loop = True
        else:
            visited_tiles.add((guard_row, guard_column))
            if (guard_row, guard_column) not in visited_tiles_directions:
                visited_tiles_directions[(guard_row, guard_column)] = [False] * 4
            visited_tiles_directions[(guard_row, guard_column)][guard_direction] = True

    return visited_tiles, is_guard_in_loop


with open(f"{data_path}/{data_file}", "r") as file:
    for current_row, line in enumerate(file):
        line = line.strip()
        room_width = len(line)
        room_height += 1
        room.append(list(line))
        if "^" in line:
            guard_initial_row, guard_initial_column = current_row, line.index("^")

visited_tiles, _ = move_guard([row[:] for row in room])

for tile in visited_tiles:
    r, c = tile
    print([r, c])
    if room[r][c] == ".":
        room[r][c] = "O"
        _, is_guard_in_loop = move_guard(room)
        if is_guard_in_loop:
            result += 1
        room[r][c] = "."

print(f'Result: {result}')