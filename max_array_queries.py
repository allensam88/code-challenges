def queryMax(arr_len, queries):
    arr = [0] * arr_len
    curr_query = 0

    while curr_query < len(queries):
        for index in range(queries[curr_query][0], queries[curr_query][1]):
            arr[index] = queries[curr_query][2]

        curr_query += 1

    return max(arr)


# -----TEST-----
qA = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(queryMax(10, qA))
