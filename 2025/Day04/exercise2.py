data_file = "example.txt"
data_file = "data.txt"

result: int = 0
grid = []
max_rows = 0
max_cols = 0
resulting_grid = []
roll_chars = ["@", "x"]
debug = False


def count_adjacent(row: int, col: int) -> int:
    count = 0
    if row > 0 and grid[row - 1][col] in roll_chars:
        count += 1
    if row < max_rows - 1 and grid[row + 1][col] in roll_chars:
        count += 1
    if col > 0 and grid[row][col - 1] in roll_chars:
        count += 1
    if col < max_cols - 1 and grid[row][col + 1] in roll_chars:
        count += 1
    if row > 0 and col > 0 and grid[row - 1][col - 1] in roll_chars:
        count += 1
    if row > 0 and col < max_cols - 1 and grid[row - 1][col + 1] in roll_chars:
        count += 1
    if row < max_rows - 1 and col > 0 and grid[row + 1][col - 1] in roll_chars:
        count += 1
    if row < max_rows - 1 and col < max_cols - 1 and grid[row + 1][col + 1] in roll_chars:
        count += 1
    return count


with open(data_file, "r") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)
    max_rows = len(grid)
    max_cols = len(grid[0]) if grid else 0

    has_removed = True

    while has_removed:
        has_removed = False

        resulting_grid = grid.copy()

        for row in range(max_rows):
            for col in range(max_cols):
                if grid[row][col] not in roll_chars:
                    continue
                if count_adjacent(row, col) < 4:
                    result += 1
                    resulting_grid[row][col] = "x"
                    has_removed = True

        if debug:
            print("Resulting Grid:")
            for row in resulting_grid:
                print("".join(row))

        for row in range(max_rows):
            for col in range(max_cols):
                if resulting_grid[row][col] == "x":
                    grid[row][col] = "."
        

print(f'Result: {result}')
