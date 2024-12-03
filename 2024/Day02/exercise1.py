data_path = "2024/Day02/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0

with open(data_path + "/" + data_file, "r") as file:
    for report in file:
        print(report.split("\n")[0])
        levels = report.split(" ")
        prev_level = -1
        is_level_increasing = None
        increase_result = True
        for level in levels:
            level = int(level)
            if prev_level != -1:
                if prev_level == level:
                    print(f"\tSame value between levels: {prev_level} {level}")
                    increase_result = False
                    break
                if is_level_increasing == None:
                    if level > prev_level:
                        is_level_increasing = True
                    else:
                        is_level_increasing = False
                if is_level_increasing and level < prev_level:
                    print(f"\tLevel should be increasing: {prev_level} {level}")
                    increase_result = False
                    break
                elif not is_level_increasing and level > prev_level:
                    print(f"\tLevel should be decreasing: {prev_level} {level}")
                    increase_result = False
                    break
                if abs(level - prev_level) > 3:
                    print(f"\tLevel difference is greater than 3: {prev_level} {level}")
                    increase_result = False
                    break
            prev_level = level
        if increase_result:
            print("\tOK")
            result += 1


print(f'Result: {result}')
