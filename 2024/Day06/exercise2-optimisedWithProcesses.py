from concurrent.futures import ProcessPoolExecutor
from math import ceil

data_path = "2024/Day06/"
data_file = "example.txt"
data_file = "data.txt"

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # UP, RIGHT, DOWN, LEFT


def move_guard(room, guard_initial_row, guard_initial_column, room_height, room_width):
    guard_row = guard_initial_row
    guard_column = guard_initial_column
    guard_direction = 0
    is_guard_moving = True
    is_guard_in_loop = False
    visited_tiles = set()
    visited_tiles_directions = {}

    visited_tiles.add((guard_row, guard_column))
    visited_tiles_directions[(guard_row, guard_column)] = [False] * 4
    visited_tiles_directions[(guard_row, guard_column)][guard_direction] = True

    while is_guard_moving and not is_guard_in_loop:
        next_column = guard_column + directions[guard_direction][0]
        next_row = guard_row + directions[guard_direction][1]
        if next_row < 0 or next_row >= room_height or next_column < 0 or next_column >= room_width:
            is_guard_moving = False
            break

        if room[next_row][next_column] == "#" or room[next_row][next_column] == "O":
            guard_direction = (guard_direction + 1) % 4
            continue

        guard_column = next_column
        guard_row = next_row
        if (guard_row, guard_column) in visited_tiles and (
            visited_tiles_directions[(guard_row, guard_column)][guard_direction]
        ):
            is_guard_in_loop = True
        else:
            visited_tiles.add((guard_row, guard_column))
            if (guard_row, guard_column) not in visited_tiles_directions:
                visited_tiles_directions[(guard_row, guard_column)] = [False] * 4
            visited_tiles_directions[(guard_row, guard_column)][guard_direction] = True

    return visited_tiles, is_guard_in_loop


def process_chunk(args):
    """Process a chunk of tiles and room."""
    chunk, room, guard_initial_row, guard_initial_column, room_height, room_width = args
    local_result = 0
    local_room = [row[:] for row in room]  # Create a local copy of the room for this chunk
    for tile in chunk:
        r, c = tile
        if local_room[r][c] == ".":
            local_room[r][c] = "O"
            _, is_guard_in_loop = move_guard(local_room, guard_initial_row, guard_initial_column, room_height, room_width)
            if is_guard_in_loop:
                local_result += 1
            local_room[r][c] = "."  # Reset the tile
    return local_result


def chunkify(data, num_chunks):
    """Split data into chunks."""
    chunk_size = ceil(len(data) / num_chunks)
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


if __name__ == "__main__":
    # Initialize variables
    room = []
    room_height = 0
    room_width = 0
    guard_initial_row = -1
    guard_initial_column = -1

    with open(f"{data_path}/{data_file}", "r") as file:
        for current_row, line in enumerate(file):
            line = line.strip()
            room_width = len(line)
            room_height += 1
            room.append(list(line))
            if "^" in line:
                guard_initial_row, guard_initial_column = current_row, line.index("^")

    visited_tiles, _ = move_guard([row[:] for row in room], guard_initial_row, guard_initial_column, room_height, room_width)

    # Split visited_tiles into chunks
    num_processes = 16  # Adjust based on your CPU cores
    chunks = chunkify(list(visited_tiles), num_processes)

    # Prepare arguments for multiprocessing
    args = [
        (chunk, room, guard_initial_row, guard_initial_column, room_height, room_width)
        for chunk in chunks
    ]

    # Use multiprocessing to process chunks in parallel
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(process_chunk, args))

    result = sum(results)
    print(f"Result: {result}")
