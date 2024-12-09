data_path = "2024/Day09/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
disk_map = []
individual_blocks = []


def load_individual_blocks():
    global individual_blocks
    for index, value in enumerate(disk_map):
        value = int(value)
        if index % 2 != 0:
            for _ in range(value):
                individual_blocks.append(".")
        else:
            file_index = str(int(index / 2))
            for _ in range(value):
                individual_blocks.append(file_index)

    # print("".join(individual_blocks))


def move_blocks():
    global disk_map, individual_blocks
    size_free_spaces = disk_map[1::2]
    size_values = disk_map[0::2]
    print(f"SIZE FREE SPACES: {size_free_spaces}")
    print(f"SIZE VALUES: {size_values}")
    for value_index, value_size in enumerate(reversed(size_values)):
        value_size = int(value_size)
        print(f"Fitting {value_size} {str(len(size_values) -1 - value_index)}s")
        for free_space_index, free_space_size in enumerate(size_free_spaces):
            occupied_space = 0
            if ":" in free_space_size:
                occupied_space = int(free_space_size.split(":")[1])
                free_space_size = int(free_space_size.split(":")[0])
            free_space_size = int(free_space_size)
            if free_space_size >= value_size:
                first_position = int(size_values[0])
                for i in range(free_space_index):
                    if ":" in size_free_spaces[i]:
                        first_position += int(size_free_spaces[i].split(":")[0])
                        first_position += int(size_free_spaces[i].split(":")[1])
                    else:
                        first_position += int(size_free_spaces[i])
                    first_position += int(size_values[i + 1])
                first_position += occupied_space

                first_replace_position = 0
                for i in range(len(size_values) - 1 - value_index):
                    first_replace_position += int(size_values[i])
                    if ":" in size_free_spaces[i]:
                        first_replace_position += int(size_free_spaces[i].split(":")[0])
                        first_replace_position += int(size_free_spaces[i].split(":")[1])
                    else:
                        first_replace_position += int(size_free_spaces[i])

                if first_position > first_replace_position:
                    break

                for _ in range(value_size):
                    print(
                        f"\tWritting {str(len(size_values) - 1 - value_index)} in position {first_position} and replacing {first_replace_position}"
                    )
                    individual_blocks[first_position] = str(len(size_values) - 1 - value_index)
                    individual_blocks[first_replace_position] = "."
                    first_position += 1
                    first_replace_position += 1

                size_free_spaces[free_space_index] = (
                    str(free_space_size - value_size) + ":" + str(value_size + occupied_space)
                )
                break

    # print("".join(individual_blocks))


def get_checksum():
    checksum = 0
    global individual_blocks
    for index, value in enumerate(individual_blocks):
        if value != ".":
            checksum += index * int(value)
    return checksum


with open(data_path + "/" + data_file, "r") as file:
    disk_map = list(file.read().replace("\n", ""))
    print(disk_map)

load_individual_blocks()
move_blocks()
result = get_checksum()

print(f'Result: {result}')
