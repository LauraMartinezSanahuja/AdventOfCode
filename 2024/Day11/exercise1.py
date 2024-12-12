data_path = "2024/Day11/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
stones = []


def do_blink():
    global stones
    result_stones = []
    for stone in stones:
        if stone == "0":
            result_stones.append("1")
        elif len(stone) % 2 == 0:
            result_stones.append(str(int(stone[0 : int(len(stone) / 2)])))
            result_stones.append(str(int(stone[int(len(stone) / 2) : int(len(stone))])))
        else:
            result_stones.append(str(int(stone) * 2024))
    stones = result_stones


with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        stones = line.split(" ")

print(stones)

BLINKS = 25
for blink in range(BLINKS):
    #print(f"BLINK {blink+1}")
    do_blink()

result = len(stones)
print(f'Result: {result}')
