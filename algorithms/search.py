
def search_option_a(arr, customer):
    for i in range(len(arr)):
        if arr[i] == customer:
            return i
    return -1


def search_option_b(arr, n, customer):
    i = 0
    r = n - 1
    while i <= r:
        m = int((i+r) / 2)
        print("Current Positions: {}".format(m))
        if arr[m] == customer:
            return m
        elif arr[m] > customer:
            r = m - 1
        else:
            i = m + 1
    return -1
