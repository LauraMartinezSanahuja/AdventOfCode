import copy

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


def print_room(map):
    print("ROOM")
    for row in map:
        column = ""
        for col in row:
            column += col
        print(column)
    print()


def move_guard(map):
    guard_row = guard_initial_row
    guard_column = guard_initial_column
    guard_direction = 0
    is_guard_moving = True
    is_guard_in_loop = False
    visited_tiles = []
    visited_tiles_directions = {}
    visited_tiles_directions_not_visited_yet = [False, False, False, False]

    map[guard_row][guard_column] = directions_sign[guard_direction]
    visited_tiles.append([guard_row, guard_column])
    guard_position = str(guard_row) + "," + str(guard_column)
    visited_tiles_directions[guard_position] = copy.deepcopy(
        visited_tiles_directions_not_visited_yet
    )
    visited_tiles_directions[guard_position][guard_direction] = True

    while is_guard_moving and not is_guard_in_loop:
        next_column = guard_column + directions[guard_direction][0]
        next_row = guard_row + directions[guard_direction][1]
        if next_row < 0 or next_row >= room_height or next_column < 0 or next_column >= room_width:
            is_guard_moving = False
            break

        if map[next_row][next_column] == "#" or map[next_row][next_column] == "O":
            guard_direction = (guard_direction + 1) % 4
            map[guard_row][guard_column] = directions_sign[guard_direction]
        else:
            if map[next_row][next_column] == ".":
                map[next_row][next_column] = directions_sign[guard_direction]
            guard_column = next_column
            guard_row = next_row
            guard_position = str(guard_row) + "," + str(guard_column)
            if [guard_row, guard_column] in visited_tiles and (
                visited_tiles_directions[guard_position][guard_direction]
            ) == True:
                is_guard_in_loop = True
            else:
                visited_tiles.append([guard_row, guard_column])
                if guard_position not in visited_tiles_directions:
                    visited_tiles_directions[guard_position] = copy.deepcopy(
                        visited_tiles_directions_not_visited_yet
                    )
                visited_tiles_directions[guard_position][guard_direction] = True

    if is_guard_in_loop and "data" not in data_file:
        print_room(map)
    return visited_tiles, is_guard_in_loop


with open(data_path + "/" + data_file, "r") as file:
    current_row = 0
    for line in file:
        line = line.replace("\n", "")
        current_column = 0
        room_width = len(line)
        room_height += 1
        room.append([])
        for char in line:
            if char == "^":
                guard_initial_row = current_row
                guard_initial_column = current_column
            room[current_row].append(char)
            current_column += 1
        current_row += 1

visited_tiles, not_important = move_guard(copy.deepcopy(room))

for i in range(0, room_height):
    for j in range(0, room_width):
        if [i, j] in visited_tiles:
            print([i, j])
            if room[i][j] == ".":
                fake_room = copy.deepcopy(room)
                fake_room[i][j] = "O"
                not_important, is_guard_in_loop = move_guard(fake_room)
                if is_guard_in_loop:
                    result += 1

print(f'Result: {result}')
