data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid: list[list[str]] = []
beam_cols: set[int] = set()

with open(data_file, "r") as file:
    for line in file:
        grid.append(list(line.strip()))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0 and grid[row][col] == "S":
                beam_cols.add(col)
                continue
            if col in beam_cols:
                if grid[row][col] == "^":
                    result += 1
                    beam_cols.remove(col)
                    beam_cols.add(col - 1)
                    beam_cols.add(col + 1)
                    grid[row][col - 1] = "|"
                    grid[row][col + 1] = "|"
                elif grid[row][col] == ".":
                    grid[row][col] = "|"

    for row in grid:
        print("".join(row))

print(f'Result: {result}')
