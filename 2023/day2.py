MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class Hand:
    red: int
    green: int
    blue: int

    def load_values(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def is_valid(self):
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE

    def to_string(self):
        return f"RED:{self.red}, GREEN:{self.green}, BLUE:{self.blue}"


class Game:
    id: int = 0
    hands = []

    def load_game(self, line):
        self.hands = []
        self.id = int(line.split(": ")[0].split(" ")[1])
        for hand_line in line.split(": ")[1].split("; "):
            cubes = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
            for cube_set in hand_line.split("\n")[0].split(", "):
                cubes[cube_set.split(" ")[1]] = int(cube_set.split(" ")[0])
            hand = Hand()
            hand.load_values(red=cubes['red'], green=cubes['green'], blue=cubes['blue'])
            self.hands.append(hand)

    def is_valid(self):
        for hand in self.hands:
            if not hand.is_valid():
                print(f"Game {self.id} is not valid. Hand: {hand.to_string()}")
                return False
        return True

    def min_cubes(self):
        max_red = 0
        max_green = 0
        max_blue = 0
        for hand in self.hands:
            if max_red < hand.red:
                max_red = hand.red
            if max_green < hand.green:
                max_green = hand.green
            if max_blue < hand.blue:
                max_blue = hand.blue
        return max_red, max_green, max_blue


with open("AoC2023/day2.txt", "r") as file:
    result: int = 0
    for line in file:
        game = Game()
        game.load_game(line)
        # if game.is_valid():
        #    result += game.id
        r, g, b = game.min_cubes()
        result += r * g * b

    print(f'Result: {result}')
