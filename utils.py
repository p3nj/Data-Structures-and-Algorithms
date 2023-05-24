# Check the array length
import os
from datetime import datetime


def sort_array(arr):
    return sorted(arr, key=lambda x: (x is None, x))


def array_length(arr):
    count = 0
    for i in arr:
        if i is not None:
            count += 1
    return count


# Flat list
def flatten(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return [lst[0]] + flatten(lst[1:])


# display headlines
def headlines(content, char, end=True):
    if end is False:
        print(''.join([i * 30 for i in char]))
    print(content)
    if end is True:
        print(''.join([i * 30 for i in char]))


# High performance fibonacci
def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c
        return b


def create_result_dir(categories):
    timestamp = datetime.now().strftime("%d-%m-%y")
    directory = "{}/{}".format(timestamp, '/'.join(categories))

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory
