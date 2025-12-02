data_file = "example.txt"
data_file = "data.txt"

result: int = 0
ids = []


def is_invalid(id: int) -> bool:
    for i in range(1, len(str(id)) // 2 + 1):
        pattern = str(id)[0:i]
        repeated_pattern = pattern * (len(str(id)) // len(pattern))
        if len(repeated_pattern) < len(str(id)):
            continue
        if repeated_pattern == str(id):
            return True
    return False


with open(data_file, "r") as file:
    for line in file:
        id_patterns = line.strip().split(',')
        for id_pattern in id_patterns:
            first_id, second_id = map(int, id_pattern.split('-'))
            for id in range(first_id, second_id + 1):
                ids.append(id)

        for id in ids:
            if is_invalid(id):
                result += id

print(f'Result: {result}')
