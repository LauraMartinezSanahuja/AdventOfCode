import re
from concurrent.futures import ProcessPoolExecutor, as_completed, TimeoutError
from z3 import Int, Optimize, Sum, sat  # pip install z3-solver

data_file = "example.txt"
data_file = "data.txt"

line_regex = r"\[(.*)\]\s\((.*)\)\s{(.*)}"

lights: list[list[list[int]]] = []  # parsed but not used in the math
buttons: list[list[list[int]]] = []
joltage_levels: list[list[int]] = []


def debug(msg: str) -> None:
    if "example" in data_file:
        print(msg)


def press_buttons(joltage: list[int], button_list: list[list[int]]) -> int:
    """
    Use Z3 to solve:
      - Variables: x_j (how many times to press button j), integers >= 0
      - Constraints: for each position i:
            sum_j button_list[j][i] * x_j == joltage[i]
      - Objective: minimize sum_j x_j
    """
    target = joltage
    n = len(target)
    m = len(button_list)

    # Trivial case
    if all(v == 0 for v in target):
        return 0

    # Early infeasibility: if some index > 0 and no button ever touches it
    for i in range(n):
        if target[i] > 0 and not any(btn[i] == 1 for btn in button_list):
            raise ValueError("Target configuration is unreachable")

    # Convert buttons to tuples for convenience
    buttons_t = [tuple(b) for b in button_list]

    opt = Optimize()

    # Variables x_0..x_{m-1}
    xs = [Int(f"x_{j}") for j in range(m)]

    # Bounds: x_j >= 0 and x_j <= static_max_k_j
    for j in range(m):
        opt.add(xs[j] >= 0)

        # static upper bound: can't press more than min(target[i]) for positions it touches
        max_k = None
        for i in range(n):
            if buttons_t[j][i] == 1:
                if max_k is None:
                    max_k = target[i]
                else:
                    max_k = min(max_k, target[i])
        if max_k is not None:
            opt.add(xs[j] <= max_k)
        else:
            # button never used (no positions): force x_j = 0
            opt.add(xs[j] == 0)

    # For each position i, sum_j button_j[i] * x_j == target[i]
    for i in range(n):
        coeffs = []
        for j in range(m):
            if buttons_t[j][i] == 1:
                coeffs.append(xs[j])
        if coeffs:
            opt.add(Sum(coeffs) == target[i])
        else:
            # no button touches this position; we already handled target[i] > 0 above
            opt.add(target[i] == 0)

    # Objective: minimize total presses
    total_presses = Sum(xs)
    opt.minimize(total_presses)

    if opt.check() != sat:
        raise ValueError("Target configuration is unreachable")

    model = opt.model()
    presses_value = 0
    for j in range(m):
        val = model[xs[j]].as_long()
        presses_value += val

    return presses_value


def solve_one(args: tuple[list[int], list[list[int]], int]) -> tuple[int, int | None]:
    joltage, button_list, index = args
    print(f"[worker] starting row {index}")
    try:
        min_buttons = press_buttons(joltage, button_list)
        print(f"[worker] finished row {index} -> {min_buttons}")
        return index, min_buttons
    except Exception as e:
        print(f"[worker] ERROR on row {index}: {e}")
        return index, None


def main() -> None:
    global lights, buttons, joltage_levels

    # Parse input
    with open(data_file, "r") as file:
        for line in file:
            matches = re.match(line_regex, line.strip())
            if matches:
                # Lights (not used anymore, but we keep parsing)
                line_lights = matches[1]
                line_lights_list: list[int] = []
                for ch in line_lights:
                    line_lights_list.append(0 if ch == '.' else 1)
                lights.append(line_lights_list)

                lights_width = len(line_lights)

                # Buttons: build 0/1 mask for each button
                line_buttons = matches[2]
                button_list: list[list[int]] = []
                for buttons_values in line_buttons.split(') ('):
                    button_values_list: list[int] = [0] * lights_width
                    button_values = buttons_values.split(',')
                    for button_value in button_values:
                        button_values_list[int(button_value)] = 1
                    button_list.append(button_values_list)
                buttons.append(button_list)

                # Joltage vector
                line_joltage_levels = matches[3]
                joltage_level_list: list[int] = []
                for joltage_level in line_joltage_levels.split(','):
                    joltage_level_list.append(int(joltage_level))
                joltage_levels.append(joltage_level_list)

    debug(f'Lights: {lights}')
    debug(f'Buttons: {buttons}')
    debug(f'Joltage Levels: {joltage_levels}')
    debug('---------------------')

    # Build tasks (one per row)
    tasks: list[tuple[list[int], list[list[int]], int]] = []
    for idx, joltage in enumerate(joltage_levels):
        tasks.append((joltage, buttons[idx], idx))

    # Optional: still sort by "easier" first (not required, but can help)
    tasks.sort(key=lambda t: (sum(t[0]), len(t[1])))

    results_per_index: dict[int, int] = {}

    # Parallel execution
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(solve_one, task): task[2] for task in tasks}

        for future in as_completed(futures):
            idx = futures[future]
            try:
                row_idx, min_buttons = future.result()
            except TimeoutError:
                print(f"[main] row {idx} timed out")
                continue

            joltage = joltage_levels[idx]
            if min_buttons is None:
                print(f'Joltage {joltage}: ERROR, no solution found')
                continue

            print(f'Joltage {joltage}: need min buttons: {min_buttons}')
            results_per_index[idx] = min_buttons

    # Sum all found results
    total_result = sum(results_per_index.values())
    print(f'Result: {total_result}')


if __name__ == "__main__":
    main()
