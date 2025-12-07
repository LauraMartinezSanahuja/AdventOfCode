data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid: list[list[str]] = []

with open(data_file, "r") as file:
    for line in file:
        grid.append([value for value in line if value != "" and value != "\n"])

    for row in grid:
        print(row)

    all_spaces_col_ids = []
    for col in range(len(grid[0])):
        all_spaces = True
        for row in grid:
            if row[col] != " ":
                all_spaces = False
                break
        if all_spaces:
            all_spaces_col_ids.append(col)

    print(all_spaces_col_ids)

    values: list[str] = []
    operator = ""
    for col in range(len(grid[0])):
        if col in all_spaces_col_ids:
            if operator == "+":
                for val in values:
                    result += int(val)
            elif operator == "*":
                prod = 1
                for val in values:
                    prod *= int(val)
                result += prod
            values = []
            operator = ""
            continue
        if grid[-1][col] == "+":
            operator = "+"
        elif grid[-1][col] == "*":
            operator = "*"

        partial_value = ""
        for row in range(len(grid) - 1):
            if grid[row][col] != " ":
                partial_value += grid[row][col]
        values.append(partial_value)

    if operator == "+":
        for val in values:
            result += int(val)
    elif operator == "*":
        prod = 1
        for val in values:
            prod *= int(val)
        result += prod


print(f'Result: {result}')
