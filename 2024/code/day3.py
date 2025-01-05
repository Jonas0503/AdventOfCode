import re


def get_all_valid_multiplications_part1():
    file = open('./input/input3.txt', 'r')
    s = file.readline()
    valid_multiplications = []

    while s:
        valid_multiplications.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)', s))
        s = file.readline()

    return valid_multiplications


# remove all new lines to get one long string; a don't() can effect the next line too
def get_all_valid_multiplications_part2():
    # remove new lines
    content = open('./input/input3.txt', 'r').read()
    updated_content = content.replace('\n', '')

    # remove and write content
    updated_file = open('./input/input3.txt', 'w')
    updated_file.truncate(0)
    updated_file.write(updated_content)
    updated_file.close()

    # read updated content
    updated_file = open('./input/input3.txt', 'r')

    content = updated_file.readline()
    valid_multiplications = []
    all_substrings = []

    # remove all content with a starting don't() and an ending do() or line end
    all_substrings = re.split(r'don\'t\(\).*?do\(\)|don\'t\(\).*?$', content)

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
