data_file = "example.txt"
data_file = "data.txt"

result: int = 0
valid_id_ranges: list[tuple[int, int]] = []
merged_ranges: list[tuple[int, int]] = []


with open(data_file, "r") as file:
    for line in file:
        if line.strip() == "":
            break
        initial_id = int(line.strip().split("-")[0])
        final_id = int(line.strip().split("-")[1])
        valid_id_ranges.append((initial_id, final_id))

    valid_id_ranges_sorted = sorted(valid_id_ranges, key=lambda x: x[0])

    for valid_id_range in valid_id_ranges_sorted:
        if merged_ranges == []:
            merged_ranges.append(valid_id_range)
            continue

        if merged_ranges[-1][1] < valid_id_range[0] - 1:
            merged_ranges.append(valid_id_range)
            continue

        last_range = merged_ranges.pop()
        new_range = (last_range[0], max(last_range[1], valid_id_range[1]))
        merged_ranges.append(new_range)

    for merged_range in merged_ranges:
        result += merged_range[1] - merged_range[0] + 1

print(f'Result: {result}')
if result >= 374773326015343:
    print("    [ERROR] Incorrect result")
