data_path = "2024/Day02/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0


def is_report_safe(levels) -> bool:
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

    return increase_result


with open(data_path + "/" + data_file, "r") as file:
    for report in file:
        report = report.split("\n")[0]
        print(report)
        levels = report.split(" ")

        if is_report_safe(levels):
            print("\tOK")
            result += 1
        else:
            # iterate removing each time one level
            for i in range(0, len(levels)):
                if i == 0:
                    levels_reduced = levels[1 : len(levels)]
                elif i == len(levels):
                    levels_reduced = levels[0 : len(levels) - 1]
                else:
                    levels_reduced = levels[0:i] + levels[i + 1 : len(levels)]
                print(f"*{levels_reduced}")
                if is_report_safe(levels_reduced):
                    print(f"\tOK ignoring level {i+1} ({levels[i]})")
                    result += 1
                    break


print(f'Result: {result}')
