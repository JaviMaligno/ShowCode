def find_balance_point(lst):
    left_sum = 0
    right_sum = sum(lst)

    for i in range(len(lst)):
        right_sum -= lst[i]

        if left_sum == right_sum:
            return i

        left_sum += lst[i]

    return -1
