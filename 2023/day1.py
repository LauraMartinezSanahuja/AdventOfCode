# for each line in the code obtain the number formed by the first and the last numbers (a1s2d3f -> 13, o4k -> 44) and then add all the results

import re

# Mapping text numbers to digits
text_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_first_number(line):
    lower_index = 2000
    first_number = ''
    for word, digit in text_to_digit.items():
        word_index = line.find(word)
        if word_index == -1:
            continue
        if word_index < lower_index:
            lower_index = word_index
            first_number = digit
    for number in numbers:
        number_index = line.find(number)
        if number_index == -1:
            continue
        if number_index < lower_index:
            lower_index = number_index
            first_number = number
    return first_number


def get_last_number(line):
    higher_index = -1
    last_number = ''
    for word, digit in text_to_digit.items():
        word_index = line.rfind(word)
        if word_index > higher_index:
            higher_index = word_index
            last_number = digit
    for number in numbers:
        number_index = line.rfind(number)
        if number_index > higher_index:
            higher_index = number_index
            last_number = number
    return last_number


total_sum = 0

with open("AoC2023/day1.txt", "r") as file:
    for line in file:
        # Remove any surrounding whitespace from the line
        line = line.strip()
        first_num = get_first_number(line)
        last_num = get_last_number(line)
        # Form a new number by concatenating first and last number
        formed_number = int(first_num[0] + last_num[-1])
        total_sum += formed_number

print("Total Sum:", total_sum)
