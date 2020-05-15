# https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].

# Examples:
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


def decodeString(string):
    stack = []
    string_block = ''
    integer = 0

    for character in string:
        if character.isdigit():
            integer = integer*10 + int(character)

        elif character == '[':
            stack.append(string_block)
            stack.append(integer)
            string_block = ''
            integer = 0

        elif character == ']':
            multiplier = stack.pop()
            prev_str = stack.pop()
            string_block = prev_str + (string_block * multiplier)

        else:
            string_block += character

    return string_block

    # stack = []

    # for character in string:
    #     if character != ']':
    #         stack.append(character)
    #         continue

    #     temp_string = ''
    #     while stack and stack[-1] != '[':
    #         temp_string = stack.pop() + temp_string
    #     stack.pop()

    #     multiplier = ''
    #     while stack and stack[-1].isnumeric():
    #         multiplier = stack.pop() + multiplier
    #     stack.append(int(multiplier)*temp_string)

    # return ''.join(stack)

    # Passes 1st test, but fails all others
    # temp_list = string.split(']')
    # print(temp_list)
    # result = ''

    # for str_block in temp_list:
    #     for character in str_block:
    #         if character == '[':
    #             temp_str = str_block[2:]
    #             print(temp_str)
    #             mult_str = temp_str * multiplier
    #             print(mult_str)
    #             result += mult_str
    #             break
    #         else:
    #             multiplier = int(character)
    #             print(multiplier)

    # return result


# -----TESTS-----
print(decodeString("3[a]2[bc]"))  # aaabcbc
print(decodeString("3[a2[c]]"))  # accaccacc
print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
