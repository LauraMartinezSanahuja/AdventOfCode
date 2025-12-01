data_file = "example.txt"
data_file = "data.txt"

result: int = 0
dial: int = 50

with open(data_file, "r") as file:
    for line in file:
        direction = line[0]
        clicks = int(line[1:].strip())

        result += clicks // 100
        clicks = clicks % 100

        if direction == "L":
            if clicks <= dial:
                dial -= clicks
                if dial == 0:
                    result += 1
            else:
                for i in range(clicks):
                    dial -= 1
                    if dial < 0:
                        dial = 99
                    if dial == 0:
                        result += 1

        else:
            if clicks + dial < 100:
                dial += clicks
                if dial == 0:
                    result += 1
            else:
                for i in range(clicks):
                    dial += 1
                    if dial > 99:
                        dial = 0
                    if dial == 0:
                        result += 1


print(f'Result: {result}')
if data_file.startswith("data") and result != 6616:
    print("    [ERROR] Result is not correct.")
