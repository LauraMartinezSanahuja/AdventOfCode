data_file = "example.txt"
data_file = "data.txt"

result = 0
max_combination_length = 12


def brute_force(line_number, line):
    highest_combination = "100000000000"
    for a in range(len(digits) - max_combination_length + 1):
        initial_digit = digits[a]
        if int(initial_digit) <= int(highest_combination[0]):
            continue
        highest_combination = initial_digit + "0" * (max_combination_length - 1)
        for b in range(a + 1, len(digits) - max_combination_length + 2):
            initial_digit = digits[a] + digits[b]
            if int(initial_digit) <= int(highest_combination[:2]):
                continue
            highest_combination = initial_digit + "0" * (max_combination_length - 2)
            for c in range(b + 1, len(digits) - max_combination_length + 3):
                initial_digit = digits[a] + digits[b] + digits[c]
                if int(initial_digit) <= int(highest_combination[:3]):
                    continue
                highest_combination = initial_digit + "0" * (max_combination_length - 3)
                for d in range(c + 1, len(digits) - max_combination_length + 4):
                    initial_digit = digits[a] + digits[b] + digits[c] + digits[d]
                    if int(initial_digit) <= int(highest_combination[:4]):
                        continue
                    highest_combination = initial_digit + "0" * (max_combination_length - 4)
                    for e in range(d + 1, len(digits) - max_combination_length + 5):
                        initial_digit = digits[a] + digits[b] + digits[c] + digits[d] + digits[e]
                        if int(initial_digit) <= int(highest_combination[:5]):
                            continue
                        highest_combination = initial_digit + "0" * (max_combination_length - 5)
                        for f in range(e + 1, len(digits) - max_combination_length + 6):
                            initial_digit = (
                                digits[a]
                                + digits[b]
                                + digits[c]
                                + digits[d]
                                + digits[e]
                                + digits[f]
                            )
                            if int(initial_digit) <= int(highest_combination[:6]):
                                continue
                            highest_combination = initial_digit + "0" * (max_combination_length - 6)
                            for g in range(f + 1, len(digits) - max_combination_length + 7):
                                initial_digit = (
                                    digits[a]
                                    + digits[b]
                                    + digits[c]
                                    + digits[d]
                                    + digits[e]
                                    + digits[f]
                                    + digits[g]
                                )
                                if int(initial_digit) <= int(highest_combination[:7]):
                                    continue
                                highest_combination = initial_digit + "0" * (
                                    max_combination_length - 7
                                )
                                for h in range(g + 1, len(digits) - max_combination_length + 8):
                                    initial_digit = (
                                        digits[a]
                                        + digits[b]
                                        + digits[c]
                                        + digits[d]
                                        + digits[e]
                                        + digits[f]
                                        + digits[g]
                                        + digits[h]
                                    )
                                    if int(initial_digit) <= int(highest_combination[:8]):
                                        continue
                                    highest_combination = initial_digit + "0" * (
                                        max_combination_length - 8
                                    )
                                    for i in range(h + 1, len(digits) - max_combination_length + 9):
                                        initial_digit = (
                                            digits[a]
                                            + digits[b]
                                            + digits[c]
                                            + digits[d]
                                            + digits[e]
                                            + digits[f]
                                            + digits[g]
                                            + digits[h]
                                            + digits[i]
                                        )
                                        if int(initial_digit) <= int(highest_combination[:9]):
                                            continue
                                        highest_combination = initial_digit + "0" * (
                                            max_combination_length - 9
                                        )
                                        for j in range(
                                            i + 1, len(digits) - max_combination_length + 10
                                        ):
                                            initial_digit = (
                                                digits[a]
                                                + digits[b]
                                                + digits[c]
                                                + digits[d]
                                                + digits[e]
                                                + digits[f]
                                                + digits[g]
                                                + digits[h]
                                                + digits[i]
                                                + digits[j]
                                            )
                                            if int(initial_digit) <= int(highest_combination[:10]):
                                                continue
                                            highest_combination = initial_digit + "0" * (
                                                max_combination_length - 10
                                            )
                                            for k in range(
                                                j + 1, len(digits) - max_combination_length + 11
                                            ):
                                                initial_digit = (
                                                    digits[a]
                                                    + digits[b]
                                                    + digits[c]
                                                    + digits[d]
                                                    + digits[e]
                                                    + digits[f]
                                                    + digits[g]
                                                    + digits[h]
                                                    + digits[i]
                                                    + digits[j]
                                                    + digits[k]
                                                )
                                                if int(initial_digit) <= int(
                                                    highest_combination[:11]
                                                ):
                                                    continue
                                                highest_combination = initial_digit + "0" * (
                                                    max_combination_length - 11
                                                )
                                                for l in range(k + 1, len(digits)):
                                                    final_combination = (
                                                        digits[a]
                                                        + digits[b]
                                                        + digits[c]
                                                        + digits[d]
                                                        + digits[e]
                                                        + digits[f]
                                                        + digits[g]
                                                        + digits[h]
                                                        + digits[i]
                                                        + digits[j]
                                                        + digits[k]
                                                        + digits[l]
                                                    )
                                                    if int(final_combination) <= int(
                                                        highest_combination
                                                    ):
                                                        continue
                                                    highest_combination = final_combination

    print(f'({line_number})For line: {line.strip()} -- highest_combination: {highest_combination}')
    return int(highest_combination)


def the_good_way(line_number, line):
    battery_slots = ["0" for _ in range(max_combination_length)]
    min_start_index = 0
    for i in range(len(battery_slots)):
        for j in range(min_start_index, len(digits) - (max_combination_length - 1 - i)):
            current_digit = digits[j]
            if int(current_digit) > int(battery_slots[i]):
                battery_slots[i] = current_digit
                min_start_index = j + 1

    print(
        f'({line_number})For line: {line.strip()} -- highest_combination: {"".join(battery_slots)}'
    )
    return int("".join(battery_slots))


with open(data_file, "r") as file:
    for line_number, line in enumerate(file, start=1):
        digits = []
        for digit in line.strip():
            digits.append(digit)

        # highest_combination= brute_force(line_number, line)
        highest_combination = the_good_way(line_number, line)

        result += int(highest_combination)


print(f'Result: {result}')
if data_file.startswith("example") and result != 3121910778619:
    print(f"    [ERROR] Expected 3121910778619 but got {result}")
elif data_file.startswith("data") and result != 168627047606506:
    print(f"    [ERROR] Expected 168627047606506 but got {result}")
