data_file = "example.txt"
data_file = "data.txt"

result: int = 0
valid_id_ranges: [tuple[int, int]] = []
ids: list[int] = []
valid_ids_end = False

with open(data_file, "r") as file:
    for line in file:
        if line.strip() == "":
            valid_ids_end = True
            continue
        if not valid_ids_end:
            initial_id = int(line.strip().split("-")[0])
            final_id = int(line.strip().split("-")[1])
            valid_id_ranges.append((initial_id, final_id))
        else:
            ids.append(int(line.strip()))

    for id in ids:
        for id_range in valid_id_ranges:
            if id_range[0] <= id <= id_range[1]:
                result += 1
                break

print(f'Result: {result}')
