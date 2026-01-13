data_file = "example1.txt"
data_file = "data.txt"

result: int = 0
machine_outputs: dict[str, list[str]] = {}


def debug(msg: str) -> None:
    if "example" in data_file:
        print(f'{msg}')


with open(data_file, "r") as file:
    for line in file:
        key = line.strip().split(": ")[0]
        values = line.strip().split(": ")[1].split(" ")
        machine_outputs[key] = values

outputs = machine_outputs["you"]
while len(outputs) > 0:
    output = outputs.pop(0)
    if output == "out":
        result += 1
    else:
        outputs.extend(machine_outputs[output])


print(f'Result: {result}')
