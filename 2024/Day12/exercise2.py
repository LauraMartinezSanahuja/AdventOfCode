data_path = "2024/Day12/"
data_file = "example01.txt"
data_file = "example02.txt"
data_file = "example03.txt"
data_file = "example04.txt"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
garden = []
garden_height = 0
garden_width = 0
fences = {}
areas = {}


def add_plant_to_area(plant, position):
    area_id = (plant, position)
    connected_area_ids = set()
    for area_plant, area_initial_position in areas:
        if plant == area_plant:
            for area_position in areas[(area_plant, area_initial_position)]:
                if (
                    (area_position[0] - 1, area_position[1]) == position
                    or (area_position[0] + 1, area_position[1]) == position
                    or (area_position[0], area_position[1] - 1) == position
                    or (area_position[0], area_position[1] + 1) == position
                ):
                    connected_area_ids.add((area_plant, area_initial_position))

    if connected_area_ids:
        area_id = connected_area_ids.pop()
        for connected_area_id in connected_area_ids:
            areas[area_id].update(areas[connected_area_id])
            areas.pop(connected_area_id)

            fences[area_id].update(fences[connected_area_id])
            fences.pop(connected_area_id)

    if area_id not in areas:
        areas[area_id] = set()
    areas[area_id].add(position)
    return area_id


def add_fence_to_area_id(area_id, position, direction):
    if area_id not in fences:
        fences[area_id] = {}

    fence_id = (position, direction)
    connected_fence_ids = set()
    #print(f"FENCES: {fences[area_id]}")
    for fence_initial_position, fence_direction in fences[area_id]:
        if direction == fence_direction:
            for fence_position in fences[area_id][(fence_initial_position, fence_direction)]:
                if (
                    (fence_position[0] - 1, fence_position[1]) == position
                    or (fence_position[0] + 1, fence_position[1]) == position
                    or (fence_position[0], fence_position[1] - 1) == position
                    or (fence_position[0], fence_position[1] + 1) == position
                ):
                    connected_fence_ids.add((fence_initial_position, fence_direction))
                    #print(f"{(position, direction)} is connected with {(fence_initial_position, fence_direction)}")

    if connected_fence_ids:
        fence_id = connected_fence_ids.pop()
        for connected_fence_id in connected_fence_ids:
            fences[area_id][fence_id].update(fences[area_id][connected_fence_id])
            fences[area_id].pop(connected_fence_id)

    if fence_id not in fences[area_id]:
        fences[area_id][fence_id] = set()
    fences[area_id][fence_id].add(position)


def get_adjacent_plants(row, col):
    adjacent_plants = []
    if row - 1 >= 0:
        adjacent_plants.append((garden[row - 1][col], "UP"))
    if row + 1 < garden_height:
        adjacent_plants.append((garden[row + 1][col], "DOWN"))
    if col - 1 >= 0:
        adjacent_plants.append((garden[row][col - 1], "LEFT"))
    if col + 1 < garden_width:
        adjacent_plants.append((garden[row][col + 1], "RIGHT"))
    return adjacent_plants


def put_fences():
    for i in range(garden_height):
        for j in range(garden_width):
            position = (i, j)
            plant = garden[i][j]
            area_id = add_plant_to_area(plant, (i, j))
            if i == 0 or i == garden_height - 1:
                add_fence_to_area_id(area_id, position, "UP" if i == 0 else "DOWN")
            if j == 0 or j == garden_width - 1:
                add_fence_to_area_id(area_id, position, "LEFT" if j == 0 else "RIGHT")
            adjacent_plants = get_adjacent_plants(i, j)
            for adjacent_plant, direction in adjacent_plants:
                if plant != adjacent_plant:
                    add_fence_to_area_id(area_id, position, direction)


def get_fences_price():
    price = 0
    for area_plant, area_position in areas:
        area_id = (area_plant, area_position)
        print(
            f"{area_plant} -> {len(areas[area_id])} * {len(fences[area_id])} = {len(areas[area_id]) * len(fences[area_id])}"
        )
        price += len(areas[area_id]) * len(fences[area_id])
    return price


with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        line = line.strip()
        garden_width = len(line)
        garden_height += 1
        garden.append(list(line))

put_fences()
result = get_fences_price()

print(f'Result: {result}')
