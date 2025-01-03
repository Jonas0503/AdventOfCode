import re


def get_all_valid_multiplications_part1():
    file = open('./input/input3.txt', 'r')
    s = file.readline()
    valid_multiplications = []

    while s:
        valid_multiplications.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)', s))
        s = file.readline()

    return valid_multiplications


# TODO: Not working
def get_all_valid_multiplications_part2():
    file = open('./input/input3.txt', 'r')
    s = file.readline()
    valid_multiplications = []
    all_substrings = []

    while s:
        all_substrings.extend(re.split(r'(don\'t\(\).*?do\(\)|don\'t\(\).*?$)', s))
        s = file.readline()

    print(all_substrings)

    for substring in all_substrings:
        valid_multiplications.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)', substring))

    return valid_multiplications


def calculate_sum(valid_multiplications: list):
    sum = 0

    for multipilcation in valid_multiplications:
        n1, n2 = re.search(r'\((\d{1,3}),(\d{1,3})\)', multipilcation).groups()
        sum += (int(n1) * int(n2))

    return sum


print(calculate_sum(get_all_valid_multiplications_part2()))
