
def insert_option_a(arr, n, new_customers):
    if n < len(arr):
        arr[n] = new_customers
        n += 1

    else:
        print("The array is already full")

    return arr, n


def insert_option_b(arr, n, new_customer):
    if n < len(arr):
        i = 0
        while arr[i] is not None and arr[i] < new_customer:
            i += 1
        j = n - 1
        while j >= i:
            arr[j+1] = arr[j]
            j -= 1
        arr[i] = new_customer
        n += 1
    else:
        print("THe array is already full")
    return arr, n


