import random
import string
import uuid


def rand_name(count):
    return [gen_uuid() for i in range(count)]


def gen_uuid():
    guid = uuid.uuid4()
    return guid.hex.replace('-', '')

