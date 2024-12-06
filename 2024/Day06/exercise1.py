data_path = "2024/Day06/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
room = []
room_height = 0
room_width = 0
guard_row = -1
guard_column = -1
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # UP, RIGHT, DOWN, LEFT
guard_direction = 0
is_guard_moving = True

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
                guard_row = current_row
                guard_column = current_column
            room[current_row].append(char)
            current_column += 1
        current_row += 1


result += 1
room[guard_row][guard_column] = "X"

while is_guard_moving:
    next_column = guard_column + directions[guard_direction][0]
    next_row = guard_row + directions[guard_direction][1]
    if next_row < 0 or next_row >= room_height or next_column < 0 or next_column >= room_width:
        is_guard_moving = False
        break

    if room[next_row][next_column] == "#":
        guard_direction = (guard_direction + 1) % 4
    else:
        if room[next_row][next_column] == ".":
            result += 1
            room[next_row][next_column] = "X"
        guard_column = next_column
        guard_row = next_row

print(f'Result: {result}')
