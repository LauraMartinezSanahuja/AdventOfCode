import re


data_file = "example.txt"
data_file = "data.txt"

result: int = 0

line_regex = r"\[(.*)\]\s\((.*)\)\s{(.*)}"

lights: list[list[list[int]]] = []
buttons: list[list[list[int]]] = []
joltage_levels: list[list[int]] = []


def debug(msg: str) -> None:
    if "example" in data_file:
        print(f'{msg}')


"""
def press_button(
    resulting_light: list[int],
    current_light: list[int],
    obtained_results: dict[str, int],
    button_list: list[list[int]],
    pressed_buttons: int = 0,
) -> None:
    if resulting_light == current_light:
        debug(f'Found resulting light with {pressed_buttons} buttons pressed')
        return
    pressed_buttons += 1
    for button in button_list:
        new_light = [0] * len(resulting_light)
        for i in range(len(resulting_light)):
            new_light[i] = current_light[i] ^ button[i]
        # debug(f'current light {current_light}, Pressing button {button}, new light: {new_light}, pressed buttons: {pressed_buttons}')
        if (
            str(new_light) in obtained_results.keys()
            and obtained_results[str(new_light)] <= pressed_buttons
        ):
            continue
        obtained_results[str(new_light)] = pressed_buttons
        press_button(resulting_light, new_light, obtained_results, button_list, pressed_buttons)


def press_buttons(light: list[int], button_list: list[list[int]]) -> int:
    all_results: dict[list[int], int] = {}
    press_button(light, [0] * len(light), all_results, button_list)
    return all_results[str(light)]
"""

from collections import deque


def press_buttons(light: list[int], button_list: list[list[int]]) -> int:
    target = tuple(light)
    start = tuple(0 for _ in light)

    if start == target:
        return 0

    visited: dict[tuple[int, ...], int] = {start: 0}
    queue: deque[tuple[tuple[int, ...], int]] = deque()
    queue.append((start, 0))

    while queue:
        current_state, presses = queue.popleft()

        for button in button_list:
            new_state = tuple(c ^ b for c, b in zip(current_state, button))
            new_presses = presses + 1

            if new_state in visited and visited[new_state] <= new_presses:
                continue

            if new_state == target:
                debug(f'Found resulting light with {new_presses} buttons pressed')
                return new_presses

            visited[new_state] = new_presses
            queue.append((new_state, new_presses))

    raise ValueError("Target light configuration is unreachable")


with open(data_file, "r") as file:
    for line in file:
        matches = re.match(line_regex, line.strip())
        if matches:
            line_lights = matches[1]
            line_lights_list: list[int] = []
            for line_light in line_lights:
                if line_light == '.':
                    line_lights_list.append(0)
                else:
                    line_lights_list.append(1)
            lights.append(line_lights_list)

            lights_width = len(line_lights)

            line_buttons = matches[2]
            button_list: list[list[int]] = []
            for buttons_values in line_buttons.split(') ('):
                button_values_list: list[int] = [0] * lights_width
                button_values = buttons_values.split(',')
                for button_value in button_values:
                    button_values_list[int(button_value)] = 1
                button_list.append(button_values_list)
            buttons.append(button_list)

            line_joltage_levels = matches[3]
            joltage_level_list: list[int] = []
            for joltage_level in line_joltage_levels.split(','):
                joltage_level_list.append(int(joltage_level))
            joltage_levels.append(joltage_level_list)

debug(f'Lights: {lights}')
debug(f'Buttons: {buttons}')
debug(f'Joltage Levels: {joltage_levels}')
debug('---------------------')

for light_position, light in enumerate(lights):
    debug(f'Processing light: {light}')
    min_buttons = press_buttons(light, buttons[light_position])
    # print(f'Light {int("".join(map(str, light)),2)}: need min buttons: {min_buttons}')
    print(f'Light {light}: need min buttons: {min_buttons}')
    result += min_buttons


print(f'Result: {result}')
