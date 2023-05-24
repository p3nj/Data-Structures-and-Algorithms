def delete_option_a(arr, n, customer):
    i = 0
    while i < len(arr) and arr[i] != customer:
        i += 1
    if i == len(arr):
        return -1
        #print("This customer is not in the array")
    else:
        while i < len(arr) - 2:
            arr[i] = arr[i+1]
            i += 1
        n -= 1


def delete_option_b(arr, n, customer):
    i = 0
    r = n - 1
    while i <= r:
        m = int((i+r) / 2)
        if arr[m] == customer:
            while m < n - 1:
                arr[m] = arr[m+1]
            n -= 1
        elif arr[m] > customer:
            r = m - 1
        else:
            i = m + 1
    return -1
    #print("This customer is not in the array")

