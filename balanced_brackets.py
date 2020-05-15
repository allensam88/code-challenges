def balanced_brackets(string):
    balance = []
    pipe_check = False
    opposite = {')': '(', ']': '[', '}': '{', '>': '<'}

    for character in string:
        # replace pipes with '<' or '>' depending on pipe check sequence
        if character == '|' and pipe_check is False:
            character = '<'
            pipe_check = True
        elif character == '|' and pipe_check is True:
            character = '>'
            pipe_check = False

        # if left side character, record balance
        if character in opposite.values():
            balance.append(character)

        # if right side character
        elif character in opposite.keys():
            # check to see if it matches opposite, then remove from balance
            if opposite[character] == balance[-1]:
                balance.pop()
            # if not a match, return false
            else:
                return False

    # if final balance is zero, then true
    if len(balance) == 0:
        return True
    # otherwise, remaining balance has unmatched character, return false
    else:
        return False


# -----TRUE TEST CASES-----
print(balanced_brackets('{}()||[]'))
print(balanced_brackets('I (bid) you [fond] farewell, |my| friend.'))
print(balanced_brackets('({[||]})'))
print(balanced_brackets('{A [hero] never} (gives |up|)'))
# -----FALSE TEST CASES-----
print(balanced_brackets('[(){}||{}()'))
print(balanced_brackets('I (bid) you [fond farewell, |my| friend.'))
print(balanced_brackets('({[|]})'))
print(balanced_brackets('{A [hero] never (gives |up|)'))
