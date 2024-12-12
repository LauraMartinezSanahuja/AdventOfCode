data_path = "2024/Day11/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
stones = {}
to_add = {}
to_remove = {}


def stone_to_add(stone, qty):
    global to_add
    if stone not in to_add:
        to_add[stone] = 0
    to_add[stone] = to_add[stone] + qty


def stone_to_remove(stone, qty):
    global to_remove
    if stone not in to_remove:
        to_remove[stone] = 0
    to_remove[stone] = to_remove[stone] + qty


def add_stones():
    global to_add
    for stone in to_add:
        if stone not in stones:
            stones[stone] = 0
        stones[stone] = stones[stone] + to_add[stone]
    to_add = {}


def remove_stones():
    global to_remove
    for stone in to_remove:
        stones[stone] = stones[stone] - to_remove[stone]
        if stones[stone] == 0:
            stones.pop(stone)
    to_remove = {}


def do_blink():
    global stones, to_add, to_remove
    for stone in stones:
        stone_to_remove(stone, stones[stone])
        if stone == 0:
            stone_to_add(1, stones[stone])
        elif len(str(stone)) % 2 == 0:
            stone_to_add(int(str(stone)[0 : int(len(str(stone)) / 2)]), stones[stone])
            stone_to_add(
                int(str(stone)[int(len(str(stone)) / 2) : int(len(str(stone)))]), stones[stone]
            )
        else:
            stone_to_add(stone * 2024, stones[stone])

    add_stones()
    remove_stones()


stone_values = []

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        stone_values = line.split(" ")

for stone_value in stone_values:
    stones[int(stone_value)] = 1


BLINKS = 75
for blink in range(BLINKS):
    #print(f"BLINK {blink+1}")
    do_blink()

result = sum(stones.values())
print(f'Result: {result}')
