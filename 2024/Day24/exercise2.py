data_path = "2024/Day24/"
data_file = "example.txt"
# data_file = "data.txt"

result: int = 0

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        pass  # LOGIC HERE

print(f'Result: {result}')
