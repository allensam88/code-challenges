def roman_convert(input):
    numerals = input.lower()
    dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

    total = dict[numerals[0]]

    for index in range(len(numerals) - 1):
        curr_val = dict[numerals[index]]
        next_val = dict[numerals[index + 1]]

        if len(numerals) > 3:
            third_val = dict[numerals[index + 2]]
            fourth_val = dict[numerals[index + 3]]

            if curr_val == next_val and next_val == third_val and third_val == fourth_val:
                return 'Invalid input: Repeating values more than 3 times in a row.'

        if curr_val >= next_val:
            total += next_val

        elif curr_val < next_val:
            if curr_val == 1 or curr_val == 10 or curr_val == 100:
                total -= next_val
            else:
                print('Invalid input: Cannot subtract 5, 50, or 500.')

    return abs(total)


# -----VALID TESTS-----
print(roman_convert('iV'))  # 4
print(roman_convert('VI'))  # 6
print(roman_convert('iii'))  # 3
print(roman_convert('IX'))  # 9
print(roman_convert('XIi'))  # 12
print(roman_convert('Ci'))  # 101
print(roman_convert('Md'))  # 1500
print(roman_convert('clx'))  # 160
# ----INVALID TESTS-----
# print(roman_convert('iVi'))  #
# print(roman_convert('VI'))  #
# print(roman_convert('iiii'))  # too many repeats
# print(roman_convert('IX'))  #
# print(roman_convert('XIi'))  #
# print(roman_convert('Ci'))  #
# print(roman_convert('dM'))  #
# print(roman_convert('clx'))  #
