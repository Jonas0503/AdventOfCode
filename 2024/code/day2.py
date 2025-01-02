def number_of_save_reports():
    file = open('./input/input2.txt', 'r')

    number_of_save_reports = 0
    s = file.readline()

    while s:
        numbers_list = s.split()
        numbers_list = [int(number) for number in numbers_list]
        numbers_list_original = numbers_list.copy()

        is_decr_initial_value = level_difference_and_is_decreasing(numbers_list[0], numbers_list[1])[1]
        save_with_removed_number = False
        is_save = True

        # iterate over one line
        for i in range(0, len(numbers_list)-1):
            difference, is_decr = level_difference_and_is_decreasing(numbers_list[i], numbers_list[i+1])

            # one error
            if (difference >= 4 or difference <= 0) or (is_decr_initial_value != is_decr):
                is_save = False
                list_of_numbers = []
                # all possibilities with one removed number
                for i in range(0, len(numbers_list_original)):
                    numbers_list.pop(i)
                    list_of_numbers.append(numbers_list)
                    numbers_list = numbers_list_original.copy()

                # iterate over the possibilities with one removed number
                for l in list_of_numbers:
                    save_with_removed_number = True
                    is_decr_initial_value = level_difference_and_is_decreasing(l[0], l[1])[1]

                    # iterate over the numbers; if one is succesful break all loops and add 1 to the sum
                    for i in range(0, len(l)-1):
                        difference, is_decr = level_difference_and_is_decreasing(l[i], l[i+1])

                        if (difference >= 4 or difference <= 0) or (is_decr_initial_value != is_decr):
                            save_with_removed_number = False
                            break

                    if save_with_removed_number:
                        break

            if save_with_removed_number:
                break

        if save_with_removed_number or is_save:
            number_of_save_reports += 1

        s = file.readline()

    return number_of_save_reports


def level_difference_and_is_decreasing(n1: int, n2: int):
    is_decreasing = True
    difference = n1-n2

    if difference < 0:
        difference *= -1
        is_decreasing = False

    return difference, is_decreasing


print(number_of_save_reports())
