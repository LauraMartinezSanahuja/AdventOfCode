data_file = "example.txt"

result: int = 0

with open(data_file, "r") as file:
    for line in file:
        pass  # LOGIC HERE

print(f'Result: {result}')
