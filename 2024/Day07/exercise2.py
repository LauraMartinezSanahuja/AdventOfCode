data_path = "2024/Day07/"
data_file = "example.txt"
data_file = "data.txt"

result: int = 0
operators = ["+", "*", "||"]


def do_operation(operation_elements):
    value = ""
    operator = ""
    for element in operation_elements:
        if not operator:
            if element in operators:
                operator = element
            else:
                value = int(element)
        else:
            if operator == "+":
                value = value + int(element)
            elif operator == "*":
                value = value * int(element)
            elif operator == "||":
                value = int(str(value) + element)
            operator = ""
    return value


def find_operations(initial_operation_elements_len, operation_result, operation_elements):
    if len(operation_elements) < 2 * initial_operation_elements_len - 1:
        is_number = False
        for index, element in enumerate(operation_elements):
            if not is_number and element.isnumeric():
                is_number = True
            elif is_number and not element.isnumeric():
                is_number = False
            else:
                for operator in operators:
                    operation_elements_copy = [element for element in operation_elements]
                    operation_elements_copy.insert(index, operator)
                    if find_operations(
                        initial_operation_elements_len, operation_result, operation_elements_copy
                    ):
                        if len(operation_elements_copy) >= 2 * initial_operation_elements_len - 1:
                            print(f"{operation_elements_copy} = {operation_result}")
                        return True
                break
    else:
        return operation_result == do_operation(operation_elements)


operations = []

with open(data_path + "/" + data_file, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        operation_result = int(line.split(": ")[0])
        operation_elements = line.split(": ")[1].split(" ")
        operations.append((operation_result, operation_elements))

for operation in operations:
    if find_operations(len(operation[1]), operation[0], operation[1]):
        result += operation[0]


print(f'Result: {result}')
