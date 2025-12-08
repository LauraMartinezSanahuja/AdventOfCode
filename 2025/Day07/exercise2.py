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
            beam_cols_copy = beam_cols.copy()
            if col in beam_cols_copy:
                if grid[row][col] == "^":
                    beam_cols.remove(col)
                    beam_cols.add(col - 1)
                    beam_cols.add(col + 1)
                    if grid[row][col - 1] == ".":
                        grid[row][col - 1] = grid[row - 1][col]
                    else:
                        grid[row][col - 1] = str(int(grid[row - 1][col]) + int(grid[row][col - 1]))
                    if grid[row][col + 1] == ".":
                        grid[row][col + 1] = grid[row - 1][col]
                    else:
                        grid[row][col + 1] = str(int(grid[row - 1][col]) + int(grid[row][col + 1]))
                else:
                    if grid[row - 1][col] == "S":
                        grid[row][col] = "1"
                    elif grid[row][col] == ".":
                        grid[row][col] = grid[row - 1][col]
                    elif grid[row - 1][col] == ".":
                        continue
                    else:
                        grid[row][col] = str(int(grid[row - 1][col]) + int(grid[row][col]))

    for row in grid:
        print("".join(row))

    result = sum(int(cell) for cell in grid[-1] if cell.isdigit())

print(f'Result: {result}')
