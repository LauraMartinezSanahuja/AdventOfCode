data_path = "2024/Day05/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
rules_after_before = {}
updates = []
rules_section = True


def is_valid_update(update):
    for page_index in range(0, len(update)):
        if page_index + 1 == len(update):
            return True, "", ""
        page = update[page_index]
        update_to_check = update[page_index + 1 : len(update)]
        if page in rules_after_before:
            matches_found = set(update_to_check) & set(rules_after_before[page])
            if matches_found:
                return False, page, matches_found


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
    is_valid, page, matches_found = is_valid_update(update)
    print(is_valid_update(update))
    if is_valid:
        continue
    fixed_update = update
    print(update)
    while not is_valid:
        print(f"\tUpdate broken\n\t\t{page} is before {matches_found}")
        max_match_index = 0
        for match in matches_found:
            match_index = fixed_update.index(match)
            if match_index > max_match_index:
                max_match_index = match_index
        print(f"\t\t\tPREV: {fixed_update}")
        fixed_update.remove(page)
        fixed_update.insert(max_match_index, page)
        print(f"\t\t\tAFTE: {fixed_update}")
        is_valid, page, matches_found = is_valid_update(fixed_update)
    print(f"\tCorrected update: {fixed_update}")
    result += int(fixed_update[int(len(update) / 2)])

print(f'Result: {result}')
