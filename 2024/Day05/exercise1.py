data_path = "2024/Day05/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
rules_after_before = {}
updates = []
rules_section = True

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        if line == "\n":
            rules_section = False
        else:
            line = line.replace("\n", "")
            if rules_section:
                page_before = line.split("|")[0]
                page_after = line.split("|")[1]
                if page_after not in rules_after_before.keys():
                    rules_after_before[page_after] = []
                rules_after_before[page_after].append(page_before)
            else:
                updates.append(line.split(","))

print(f"RULES (after:list[before])\n{rules_after_before}\n")

for update in updates:
    print(update)
    is_valid = True
    for page_index in range(0, len(update)):
        if page_index + 1 == len(update):
            if is_valid:
                print(f"\tCorrect update: {int(update[int(len(update) / 2)])}")
                result += int(update[int(len(update) / 2)])
            break
        page = update[page_index]
        update_to_check = update[page_index + 1 : len(update)]
        if page in rules_after_before:
            matches_found = set(update_to_check) & set(rules_after_before[page])
            if matches_found:
                print(f"\tUpdate broken\n\t\t{page} is before {matches_found}")
                is_valid = False
                break

print(f'Result: {result}')
