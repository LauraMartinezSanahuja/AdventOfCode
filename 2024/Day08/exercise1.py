data_path = "2024/Day08/"
data_file = "example-2antennas.txt"
data_file = "example-3antennas.txt"
data_file = "example-3+1antennas.txt"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
antennas = {}
rows = 0
cols = 0


def is_point_inside(point):
    return point[0] >= 0 and point[0] < rows and point[1] >= 0 and point[1] < cols


def get_distances(pointA, pointB):
    return (
        (pointA[0] - pointB[0], pointA[1] - pointB[1]),
        (pointB[0] - pointA[0], pointB[1] - pointA[1]),
    )


def add_distance(point, distance):
    return (point[0] + distance[0], point[1] + distance[1])


def get_antinodes(pointA, pointB):
    antinodes = set()
    distanceAB, distanceBA = get_distances(pointA, pointB)
    antinodeAB = add_distance(pointA, distanceAB)
    if is_point_inside(antinodeAB):
        antinodes.add(antinodeAB)
    antinodeBA = add_distance(pointB, distanceBA)
    if is_point_inside(antinodeBA):
        antinodes.add(antinodeBA)
    return antinodes


with open(data_path + "/" + data_file, "r") as file:
    for row, line in enumerate(file):
        cols = 0
        line = line.replace("\n", "")
        for col, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((row, col))
            cols += 1
        rows += 1

print(antennas)
visited_antinodes = set()

for freq in antennas.keys():
    all_freq_pairs = [
        (a, b) for idx, a in enumerate(antennas[freq]) for b in antennas[freq][idx + 1 :]
    ]
    for freq_pair in all_freq_pairs:
        pointA = freq_pair[0]
        pointB = freq_pair[1]
        antinodes = get_antinodes(pointA, pointB)
        for antinode in antinodes:
            if antinode not in visited_antinodes:
                visited_antinodes.add(antinode)
                result += 1

print(f'Result: {result}')
