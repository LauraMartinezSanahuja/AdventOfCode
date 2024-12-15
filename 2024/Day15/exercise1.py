data_path = "2024/Day15/"
data_file = "example-small.txt"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
warehouse = []
warehouse_width = 0
warehouse_heigth = 0
movements = []
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
robot_position = (-1, -1)


def print_map():
    print("-" * warehouse_width)
    for row in warehouse:
        print("".join(row))
    print("-" * warehouse_width)
    print()


def get_next_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def get_warehouse_element(position):
    global warehouse
    return warehouse[position[0]][position[1]]


def set_warehouse_element(position, value):
    global warehouse
    warehouse[position[0]][position[1]] = value


def move_box(position, direction):
    next_pos = get_next_position(position, direction)
    next_pos_element = get_warehouse_element(next_pos)
    if next_pos_element == "#":
        return False
    if next_pos_element == ".":
        set_warehouse_element(next_pos, "O")
        set_warehouse_element(position, ".")
        return True
    if next_pos_element == "O":
        can_move = move_box(next_pos, direction)
        if can_move:
            set_warehouse_element(next_pos, "O")
            set_warehouse_element(position, ".")
        return can_move


def do_move(direction):
    global robot_position
    next_pos = get_next_position(robot_position, direction)
    next_pos_element = get_warehouse_element(next_pos)
    # print(f"R:{robot_position} d:{direction} -> next:{next_pos} ({next_pos_element})")
    if next_pos_element == "#":
        return
    if next_pos_element == "." or move_box(next_pos, direction):
        set_warehouse_element(robot_position, ".")
        set_warehouse_element(next_pos, "@")
        robot_position = next_pos


def get_gps():
    gps = 0
    for i in range(warehouse_heigth):
        for j in range(warehouse_width):
            if warehouse[i][j] == "O":
                gps += 100 * i + j
    return gps


load_map = True
with open(data_path + "/" + data_file, "r") as file:
    for row, line in enumerate(file):
        if line == "\n":
            load_map = False
        else:
            line = line.replace('\n', '')
            if load_map:
                line = line.strip()
                warehouse_width = len(line)
                warehouse_heigth += 1
                warehouse.append(list(line))
                if robot_position == (-1, -1) and "@" in line:
                    for col in range(warehouse_width):
                        if warehouse[row][col] == "@":
                            robot_position = (row, col)
                            break
            else:
                movements.extend(line.strip())

for move in movements:
    do_move(directions[move])
    # print_map()

result = get_gps()

print(f'Result: {result}')
