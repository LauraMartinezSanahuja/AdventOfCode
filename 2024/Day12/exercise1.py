data_path = "2024/Day12/"
data_file = "example01.txt"
data_file = "example02.txt"
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
                    # print(f"{(plant, position)} is connected with {area_id}")

    if connected_area_ids:
        area_id = connected_area_ids.pop()
        for connected_area_id in connected_area_ids:
            areas[area_id].update(areas[connected_area_id])
            areas.pop(connected_area_id)

            fences[area_id] = fences[area_id] + fences[connected_area_id]
            fences.pop(connected_area_id)

    if area_id not in areas:
        areas[area_id] = set()
    areas[area_id].add(position)
    return area_id


def add_fence_to_area_id(area_id):
    if area_id not in fences:
        fences[area_id] = 0
    fences[area_id] = fences[area_id] + 1


def get_adjacent_plants(row, col):
    adjacent_plants = []
    if row - 1 >= 0:
        adjacent_plants.append(garden[row - 1][col])
    if row + 1 < garden_height:
        adjacent_plants.append(garden[row + 1][col])
    if col - 1 >= 0:
        adjacent_plants.append(garden[row][col - 1])
    if col + 1 < garden_width:
        adjacent_plants.append(garden[row][col + 1])
    return adjacent_plants


def put_fences():
    for i in range(garden_height):
        for j in range(garden_width):
            plant = garden[i][j]
            # print(f"{plant} -> [{i}, {j}]")
            area_id = add_plant_to_area(plant, (i, j))
            if i == 0 or i == garden_height - 1:
                # print(f"\tBorder fence i={i}")
                add_fence_to_area_id(area_id)
            if j == 0 or j == garden_width - 1:
                # print(f"\tBorder fence j={j}")
                add_fence_to_area_id(area_id)
            adjacent_plants = get_adjacent_plants(i, j)
            # print(f"\t{adjacent_plants}")
            for adjacent_plant in adjacent_plants:
                if plant != adjacent_plant:
                    # print(f"\tBorder fence adjacent_plant={adjacent_plant}")
                    add_fence_to_area_id(area_id)


def get_fences_price():
    # print(areas)
    price = 0
    for area_plant, area_position in areas:
        area_id = (area_plant, area_position)
        # print(f"{area_plant} -> {len(areas[area_id])} * {fences[area_id]} = {len(areas[area_id]) * fences[area_id]}")
        price += len(areas[area_id]) * fences[area_id]
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
