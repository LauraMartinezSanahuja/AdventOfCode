import re

data_path = "2024/Day13/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
machine_info_pattern = (
    'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
)
machine_info = []


class MachineInfo:
    button_A_tokens: int = 3
    button_B_tokens: int = 1
    max_clicks_button_A: int = 100
    max_clicks_button_B: int = 100
    button_A_X: int
    button_A_Y: int
    button_B_X: int
    button_B_Y: int
    prize_X: int
    prize_Y: int

    def __init__(self, parameters):
        self.button_A_X = int(parameters[0])
        self.button_A_Y = int(parameters[1])
        self.button_B_X = int(parameters[2])
        self.button_B_Y = int(parameters[3])
        self.prize_X = int(parameters[4])
        self.prize_Y = int(parameters[5])

    def max_press_button_A(self):
        return min(
            min(int(self.prize_X / self.button_A_X), self.max_clicks_button_A),
            min(int(self.prize_Y / self.button_A_Y), self.max_clicks_button_A),
        )

    def max_press_button_B(self):
        return min(
            min(int(self.prize_X / self.button_B_X), self.max_clicks_button_B),
            min(int(self.prize_Y / self.button_B_Y), self.max_clicks_button_B),
        )

    def max_tokens(self):
        return (
            self.max_clicks_button_A * self.button_A_tokens
            + self.max_clicks_button_B * self.button_B_tokens
        )

    def id(self):
        return f"Prize: X={self.prize_X}, Y={self.prize_Y}"

    def to_string(self):
        return f"Button A: X+{self.button_A_X}, Y+{self.button_A_Y}\nButton B: X+{self.button_B_X}, Y+{self.button_B_Y}\nPrize: X={self.prize_X}, Y={self.prize_Y}"


def is_prize_possible(machine):
    if (
        machine.button_A_X * machine.max_clicks_button_A
        + machine.button_B_X * machine.max_clicks_button_B
        < machine.prize_X
    ) and (
        machine.button_A_Y * machine.max_clicks_button_A
        + machine.button_B_Y * machine.max_clicks_button_B
        < machine.prize_Y
    ):
        # print("\tImpossible to reach prize in X and Y")
        return False
    if (
        machine.button_A_X * machine.max_clicks_button_A
        + machine.button_B_X * machine.max_clicks_button_B
        < machine.prize_X
    ):
        # print("\tImpossible to reach prize in X")
        return False
    if (
        machine.button_A_Y * machine.max_clicks_button_A
        + machine.button_B_Y * machine.max_clicks_button_B
        < machine.prize_Y
    ):
        # print("\tImpossible to reach prize in Y")
        return False
    return True


def get_tokens(machine):
    # print(f"\n{machine.to_string()}")
    click_B = (machine.button_A_X * machine.prize_Y - machine.button_A_Y * machine.prize_X) / (
        machine.button_A_X * machine.button_B_Y - machine.button_A_Y * machine.button_B_X
    )
    if click_B.is_integer():
        click_B = int(click_B)
        # print(f"\tB: {click_B}")
        click_A = (machine.prize_X - machine.button_B_X * click_B) / (machine.button_A_X)
        if click_A.is_integer():
            click_A = int(click_A)
            # print(f"\tA: {click_A}")
            return int(click_A * machine.button_A_tokens) + int(click_B * machine.button_B_tokens)

    return 0


with open(data_path + "/" + data_file, "r") as file:
    lines = file.read()
    machine_info_matches = re.findall(machine_info_pattern, lines)
    for machine_info_match in machine_info_matches:
        machine_info.append(MachineInfo(machine_info_match))

for machine in machine_info:
    if is_prize_possible(machine):
        result += get_tokens(machine)


print(f'Result: {result}')
