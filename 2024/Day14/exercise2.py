import re
from math import ceil, floor

data_path = "2024/Day14/"
data_file = "data.txt"
map_width = 101
map_height = 103

result: int = 0
robot_info_pattern = 'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
robots = []
seconds = 100


class Vector:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)


class RobotInfo:
    position: Vector
    velocity: Vector

    def __init__(self, parameters):
        self.position = Vector(int(parameters[0]), int(parameters[1]))
        self.velocity = Vector(int(parameters[2]), int(parameters[3]))

    def move(self):
        self.position = self.position.add(self.velocity)
        self.position = Vector(self.position.x % map_width, self.position.y % map_height)

    def to_string(self):
        return (
            f'pos:({self.position.x},{self.position.y}) vel:({self.velocity.x},{self.velocity.y})'
        )


def print_map():
    map = []
    for i in range(map_height):
        map.append([])
        for _ in range(map_width):
            map[i].append('.')

    for robot in robots:
        if map[robot.position.y][robot.position.x] == '.':
            map[robot.position.y][robot.position.x] = '1'
        else:
            map[robot.position.y][robot.position.x] = str(
                int(map[robot.position.y][robot.position.x]) + 1
            )

    print("-- MAP " + "-" * (map_width - 7))
    for row in map:
        print("".join(row))
    print("-" * map_width)


def tree_found():
    map = []
    count_multiple_in_pos = 0
    for i in range(map_height):
        map.append([])
        for _ in range(map_width):
            map[i].append('.')

    for robot in robots:
        if map[robot.position.y][robot.position.x] == '.':
            map[robot.position.y][robot.position.x] = '1'
        else:
            map[robot.position.y][robot.position.x] = str(
                int(map[robot.position.y][robot.position.x]) + 1
            )
            count_multiple_in_pos += 1

    return count_multiple_in_pos < 2


with open(data_path + "/" + data_file, "r") as file:
    lines = file.read()
    robot_info_matches = re.findall(robot_info_pattern, lines)
    for robot_info_match in robot_info_matches:
        robots.append(RobotInfo(robot_info_match))

seconds = 0
while True:
    seconds += 1
    for robot in robots:
        robot.move()
    if tree_found():
        break

print_map()
result = seconds

print(f'Result: {result}')
