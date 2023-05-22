def array_length(arr):
    count = 0
    for i in arr:
        if i is not None:
            count += 1
    print(count)
    return count


def headlines(str, char):
    print(''.join([i*30 for i in char]))
    print(str)
    print(''.join([i*30 for i in char]))

