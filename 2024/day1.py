import re


def read_and_save_file_content():
    left = []
    right = []

    file = open('./input1.txt', 'r')

    s = file.readline()
    while s:
        left.append(int(re.search('\A\d{5}', s).group()))
        right.append(int(re.search('\d{5}$', s).group()))
        s = file.readline()

    return left, right


def distance():
    left, right = read_and_save_file_content()

    left.sort()
    right.sort()

    distance = 0

    for l, r in zip(left, right):
        res = l - r
        if res < 0:
            res *= -1
        distance += res

    return distance


def similarity_score():
    left, right = read_and_save_file_content()

    score = 0

    for left_number in left:
        occurrences = 0
        for right_number in right:
            if left_number == right_number:
                occurrences += 1
        score += left_number*occurrences

    return score


print(similarity_score())
