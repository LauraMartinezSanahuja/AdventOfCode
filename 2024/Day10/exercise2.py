data_path = "2024/Day10/"
data_file = "example2-1trail-score3.txt"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
topographic_map = []
topographic_map_height = 0
topographic_map_width = 0
trailheads = []


def print_topographic_map():
    print("-- TOPOGRAPHIC MAP --")
    for row in topographic_map:
        print("    " + "".join(row))
    print("---------------------")


def print_trailheads():
    print("---- TRAILHEADS -----")
    print(f"    {trailheads}")
    print("---------------------")


def get_possible_ortogonal_positions(current_position):
    ortogonal_positions = set()
    if current_position[0] - 1 >= 0:
        ortogonal_positions.add((current_position[0] - 1, current_position[1]))
    if current_position[0] + 1 <= topographic_map_height:
        ortogonal_positions.add((current_position[0] + 1, current_position[1]))

    if current_position[1] - 1 >= 0:
        ortogonal_positions.add((current_position[0], current_position[1] - 1))
    if current_position[1] + 1 <= topographic_map_width:
        ortogonal_positions.add((current_position[0], current_position[1] + 1))

    return ortogonal_positions


def look_for_next_number_ortogonal(current_position, current_value, visited_tops):
    ortogonal_positions = get_possible_ortogonal_positions(current_position)
    for position in ortogonal_positions:
        value = topographic_map[position[0]][position[1]]
        if value != ".":
            value = int(value)
            if current_value + 1 == value:
                if value == 9:
                    visited_tops.append(position)
                else:
                    look_for_next_number_ortogonal(position, value, visited_tops)


with open(data_path + "/" + data_file, "r") as file:
    for row, line in enumerate(file):
        line_list = list(line.strip())
        for col, value in enumerate(line_list):
            if value == "0":
                trailheads.append((row, col))
            if topographic_map_width < col:
                topographic_map_width = col
        topographic_map.append(list(line.strip()))
        topographic_map_height = row

print_topographic_map()

print_trailheads()

for trailhead in trailheads:
    print(f"TRAILHEAD: {trailhead}")
    visited_tops = []
    look_for_next_number_ortogonal(trailhead, 0, visited_tops)
    print(f"\tVISITED TOPS: {len(visited_tops)} -> {visited_tops}")
    result += len(visited_tops)

print()
print(f'Result: {result}')
