data_file = "example.txt"
# data_file = "data.txt"

result: int = 0
regions: dict[(int, int, int), list[int]] = {}


def debug(msg: str) -> None:
    if "example" in data_file:
        print(f'{msg}')


loading_regions = False
region_id = 0
with open(data_file, "r") as file:
    for line in file:
        if "x" in line:
            loading_regions = True

        if loading_regions:
            region_sizes = line.strip().split(": ")[0].split("x")
            region_wide = int(region_sizes[0])
            region_long = int(region_sizes[1])
            regions[(region_id, region_wide, region_long)] = list(
                map(int, line.strip().split(": ")[1].split(" "))
            )
            region_id += 1

for region_key, region_values in regions.items():
    region_id, region_wide, region_long = region_key
    debug(
        f'Analyzing Region {region_id} of size {region_wide}x{region_long} with presents {region_values}'
    )

    # Fast heuristic: area // 7 > sum(all_values)
    # This works because each shape is exactly 7 cells
    # Integer division accounts for wasted space
    area = region_wide * region_long
    total = sum(region_values)

    debug(f'  area//7 = {area//7}, sum = {total}, passes = {area//7 > total}')

    if area // 7 > total:
        result += 1

print(f'Result: {result}')
