import random
import string


def rand_name():

    strs = []
    for i in range(2):
        strs.append(rand_string(True))
    return ' '.join(strs)


def rand_string(capped):
    name = ""

    if capped:
        name = string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase) - 1)]

    for i in range(3, 8):
        name += string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)]

    return name

