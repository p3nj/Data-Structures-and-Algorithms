import random
import string


def rand_name(count):
    return [' '.join([rand_string(True), rand_string(True)]) for i in range(count)]


def rand_string(capped):
    letters = string.ascii_uppercase if capped else string.ascii_lowercase
    return ''.join(random.choices(letters, k=random.randint(3, 7)))

