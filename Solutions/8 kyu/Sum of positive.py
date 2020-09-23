def positive_sum(arr):
    res = 0
    for x in arr:
        if x > 0:
            res += x
    return res
