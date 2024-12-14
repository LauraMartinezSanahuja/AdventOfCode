import re
from math import ceil, floor

data_path = "2024/Day14/"
data_file = "example01.txt"
data_file = "example.txt"
map_width = 11
map_height = 7
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


with open(data_path + "/" + data_file, "r") as file:
    lines = file.read()
    robot_info_matches = re.findall(robot_info_pattern, lines)
    for robot_info_match in robot_info_matches:
        robots.append(RobotInfo(robot_info_match))

for second in range(seconds):
    #print_map()
    for robot in robots:
        robot.move()

print_map()

q1 = 0
q2 = 0
q3 = 0
q4 = 0
half_width = int(map_width / 2)
half_height = int(map_height / 2)
for robot in robots:
    if robot.position.x < half_width:
        if robot.position.y < half_height:
            q1 += 1
        elif robot.position.y > half_height:
            q3 += 1
    elif robot.position.x > half_width:
        if robot.position.y < half_height:
            q2 += 1
        elif robot.position.y > half_height:
            q4 += 1

result = q1 * q2 * q3 * q4

print(f'Result: {result}')
