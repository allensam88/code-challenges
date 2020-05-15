# Three pointer solution with sorted array, lowest to highest
# i => current index, n => next index, l => last index
#
#  i
#     n
# [1, 2, 3, 6, 7, 8, 9, 15]
#                        l


def sum_triplet(arr, target):
    arr.sort()
    stack = []
    length = len(arr)

    for index in range(length - 2):
        next_index = index + 1
        last_index = length - 1

        while next_index < last_index:
            sum = arr[index] + arr[next_index] + arr[last_index]

            if sum == target:
                stack.append((arr[index], arr[next_index], arr[last_index]))
                next_index += 1

            elif sum < target:
                next_index += 1

            else:  # sum > target
                last_index -= 1

    # triplets are found, return them, else return -1
    if stack:
        return stack
    else:
        return -1


# -----TEST-----
test1 = [1, 2, 3, 6, 7, 8, 9, 15]
print(sum_triplet(test1, 30))
# expected output -> [(6, 9 , 15), (7, 8, 15)]
