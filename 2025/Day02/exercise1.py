data_file = "example.txt"
data_file = "data.txt"

result: int = 0
ids = list()

def is_invalid(id: int) -> bool:
    pattern = str(id)[0:len(str(id)) // 2]
    repeated_pattern = pattern * 2
    if repeated_pattern == str(id):
        print(f'    [INVALID] ID {id} is invalid due to pattern {pattern}')
        return True
    return False

with open(data_file, "r") as file:
    for line in file:
        id_patterns = line.strip().split(',')
        for id_pattern in id_patterns:
            first_id, second_id = map(int, id_pattern.split('-'))
            for id in range(first_id, second_id + 1):
                if len(str(id)) %2 == 0:
                    ids.append(id)

        print(ids)

        for id in ids:
            if is_invalid(id):
                result += id

print(f'Result: {result}')
