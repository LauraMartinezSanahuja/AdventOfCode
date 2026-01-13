data_file = "example.txt"
# data_file = "data.txt"

result: int = 0


def debug(msg: str) -> None:
    if "example" in data_file:
        print(f'{msg}')


with open(data_file, "r") as file:
    for line in file:
        pass  # LOGIC HERE

print(f'Result: {result}')
