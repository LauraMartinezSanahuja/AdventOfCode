data_path = "2024/Day09/"
data_file = "example-basic.txt"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
disk_map = []
individual_blocks = []


def load_individual_blocks():
    global individual_blocks
    for index, value in enumerate(disk_map):
        if index % 2 != 0:
            for _ in range(value):
                individual_blocks.append(".")
        else:
            file_index = str(int(index / 2))
            for _ in range(value):
                individual_blocks.append(file_index)

    print(individual_blocks)


def move_blocks():
    global individual_blocks
    indexes_free_spaces = [int(i) for i, x in enumerate(individual_blocks) if x == "."]
    indexes_values = [int(i) for i, x in enumerate(individual_blocks) if x != "."]

    for free_space in indexes_free_spaces:
        value = indexes_values.pop()
        if free_space < value:
            individual_blocks[free_space] = individual_blocks[value]
            individual_blocks[value] = "."

    print(individual_blocks)


def get_checksum():
    checksum = 0
    global individual_blocks
    for index, value in enumerate(individual_blocks):
        if value == ".":
            break
        checksum += index * int(value)
    return checksum


with open(data_path + "/" + data_file, "r") as file:
    disk_map = list(file.read().replace("\n", ""))
    disk_map = (int(x) for x in disk_map)

load_individual_blocks()
move_blocks()
result = get_checksum()

print(f'Result: {result}')
