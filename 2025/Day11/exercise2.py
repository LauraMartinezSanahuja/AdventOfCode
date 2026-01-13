# data_file = "example2.txt"
data_file = "data.txt"

result: int = 0
graph: dict[str, list[str]] = {}

# Parse the graph
with open(data_file, "r") as file:
    for line in file:
        key = line.strip().split(": ")[0]
        values = line.strip().split(": ")[1].split(" ")
        graph[key] = values

# Use DFS with memoization to count paths
# Key optimization: Don't include visited in memo key!
# State: (current_node, has_fft, has_dac)
memo = {}


def count_paths(node: str, has_fft: bool, has_dac: bool, visited: frozenset) -> int:
    """Count paths from node to 'out' that pass through both 'fft' and 'dac'"""

    # If we reached 'out', check if we passed through both fft and dac
    if node == "out":
        return 1 if (has_fft and has_dac) else 0

    # Update flags if we're at fft or dac
    if node == "fft":
        has_fft = True
    if node == "dac":
        has_dac = True

    # Check memoization (without visited in the key!)
    state = (node, has_fft, has_dac)
    if state in memo:
        return memo[state]

    # If node not in graph, it's a dead end
    if node not in graph:
        memo[state] = 0
        return 0

    count = 0
    for next_node in graph[node]:
        # Avoid cycles in current path
        if next_node not in visited:
            new_visited = visited | {next_node}
            count += count_paths(next_node, has_fft, has_dac, new_visited)

    memo[state] = count
    return count


# Start from each node that 'svr' points to
total = 0
if "svr" in graph:
    for start_node in graph["svr"]:
        visited_set = frozenset({"svr", start_node})
        paths = count_paths(start_node, False, False, visited_set)
        print(f"Paths from svr -> {start_node}: {paths}")
        total += paths

print(f'Result: {total}')
