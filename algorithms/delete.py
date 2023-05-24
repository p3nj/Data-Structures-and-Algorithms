def delete_option_a(arr, n, customer):
    i = 0
    while i < n and arr[i] != customer:
        i += 1
    if i == n:
        return -1, n
    else:
        while i < n - 1:
            arr[i] = arr[i+1]
            i += 1
        n -= 1
        return 0, n


def delete_option_b(arr, n, customer):
    i = 0
    r = n - 1
    while i < r:
        m = int((i+r) / 2)
        try:
            if arr[m] == customer:
                while m < n - 1:
                    arr[m] = arr[m+1]
                    m += 1
                n -= 1
                return 0, n
            elif arr[m] > customer:
                r = m - 1
            else:
                i = m + 1
        except TypeError:
            continue
    return -1, n


