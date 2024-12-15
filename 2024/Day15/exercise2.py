data_path = "2024/Day15/"
data_file = "example2-small.txt"
data_file = "example.txt"
# data_file = "test.txt"
data_file = "data.txt"

result: int = 0
warehouse = []
warehouse_width = 0
warehouse_heigth = 0
movements = []
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
directions_sign = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
robot_pos = (-1, -1)
invalid_elements = ["#"]
path_elements = ["."]


def print_map():
    print("-" * warehouse_width)
    for row in warehouse:
        print("".join(row))
    print("-" * warehouse_width)
    print()


def get_next_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def get_warehouse_elem(pos):
    global warehouse
    return warehouse[pos[0]][pos[1]]


def set_warehouse_elem(pos, value):
    global warehouse
    warehouse[pos[0]][pos[1]] = value


def can_move_box(pos, direction, move_next):
    move_next.add(pos)
    next_pos = get_next_pos(pos, direction)
    next_element = get_warehouse_elem(next_pos)

    current_elem = get_warehouse_elem(pos)
    if current_elem == "[":
        side_pos = get_next_pos(pos, directions[">"])
    elif current_elem == "]":
        side_pos = get_next_pos(pos, directions["<"])

    if side_pos != next_pos and side_pos not in move_next:
        if not can_move_box(side_pos, direction, move_next):
            return False

    if next_element in invalid_elements:
        return False
    if next_element in path_elements:
        return True
    if (next_element == "[" or next_element == "]") and next_pos not in move_next:
        return can_move_box(next_pos, direction, move_next)

    return True


def do_move(direction, debug=False):
    global robot_pos
    next_pos = get_next_pos(robot_pos, direction)
    next_elem = get_warehouse_elem(next_pos)
    if debug:
        print(f"R:{robot_pos} d:{directions_sign[direction]} -> next:{next_pos} ({next_elem})")
    if next_elem in invalid_elements:
        return
    if next_elem in path_elements:
        set_warehouse_elem(robot_pos, ".")
        set_warehouse_elem(next_pos, "@")
        robot_pos = next_pos
        return
    move_next = set()
    if can_move_box(next_pos, direction, move_next):
        while len(move_next) > 0:
            for pos in move_next:
                next_pos2 = get_next_pos(pos, direction)
                next_element = get_warehouse_elem(next_pos2)
                if next_element == ".":
                    set_warehouse_elem(next_pos2, get_warehouse_elem(pos))
                    set_warehouse_elem(pos, next_element)
                    move_next.remove(pos)
                    break
        set_warehouse_elem(robot_pos, ".")
        set_warehouse_elem(next_pos, "@")
        robot_pos = next_pos
        return


def get_gps():
    gps = 0
    for i in range(warehouse_heigth):
        for j in range(warehouse_width):
            if warehouse[i][j] == "[" or warehouse[i][j] == "X":
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
                line = line.replace('#', '##')
                line = line.replace('O', '[]')
                line = line.replace('.', '..')
                line = line.replace('@', '@.')
                line = line.strip()
                warehouse_width = len(line)
                warehouse_heigth += 1
                warehouse.append(list(line))
                if robot_pos == (-1, -1) and "@" in line:
                    for col in range(warehouse_width):
                        if warehouse[row][col] == "@":
                            robot_pos = (row, col)
                            break
            else:
                movements.extend(line.strip())

print_map()

for number, move in enumerate(movements):
    do_move(directions[move])  # , True)
    # print_map()

print_map()
result = get_gps()

print(f'Result: {result}')
