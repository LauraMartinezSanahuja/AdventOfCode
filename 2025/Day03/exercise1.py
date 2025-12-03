data_file = "example.txt"
data_file = "data.txt"

result: int = 0

with open(data_file, "r") as file:
    for line in file:
        digits = []
        for digit in line.strip():
            digits.append(digit)

        digits_combinations = []
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                digits_combinations.append(digits[i] + digits[j])

        highest_combination = "00"
        for combination in digits_combinations:
            if int(combination) > int(highest_combination):
                highest_combination = combination
                
        print(f'For line: {line.strip()} -- highest_combination: {highest_combination}')
        result += int(highest_combination)

print(f'Result: {result}')
