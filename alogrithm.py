import random

from algorithms.delete import delete_option_a, delete_option_b
from algorithms.insertion import insert_option_a, insert_option_b
from algorithms.search import search_option_a, search_option_b
from lib import rand_names as mock
from lib import timer as t
from utils import headlines, array_length

if '__main__' == __name__:
    t.Timer.stopwatch(t.Timer(True, "Generate fixed array length: 100_000"))
    customers = [None] * 100_000
    t.Timer.stopwatch(t.Timer(False))

    # Generate random names

    new_customers = []
    t.Timer.stopwatch(t.Timer(True, "Generate 5_000 random names"))
    for i in range(int(5_000)):
        new_customers.append(mock.rand_name())
    t.Timer.stopwatch(t.Timer(False))

    # Option A
    # Insertion
    headlines("Insertion", '#')
    headlines("Benchmarking option A", '-')

    data_length = array_length(customers)
    t.Timer.stopwatch(t.Timer(True, "Insertion Option A. 5_000 items."))
    for item in new_customers:
        customers, data_length = insert_option_a(customers, data_length, item)
    t.Timer.stopwatch(t.Timer(False))

    # Searching
    headlines("Searching", '#')
    data_length = array_length(customers)
    name_list = random.choices(customers[0:data_length], k=10)

    for i in range(10):
        name_list.append(mock.rand_name())

    for count, item in enumerate(name_list):
        t.Timer.stopwatch(t.Timer(True, "[{}]. Search {} ".format(count, item)))
        search_option_a(customers, item)
        t.Timer.stopwatch(t.Timer(False))

    # Delete
    headlines("Delete", '#')
    name_list = random.choices(customers[0:data_length], k=10)
    for i in range(10):
        name_list.append(mock.rand_name())

    for count, item in enumerate(name_list):
        t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
        delete_option_a(customers, data_length, item)
        t.Timer.stopwatch(t.Timer(False))

    headlines("Cleaning customers database", '@')

    customers = [None if x is not None else None for x in customers]
    data_length = array_length(customers)

    print(data_length)

    # Option B
    headlines("Benchmarking option B", '-')
    t.Timer.stopwatch(t.Timer(True, "Generate 5_000 random names to array using Option B"))
    for item in new_customers:
        customers, data_length = insert_option_b(customers, data_length, item)
    t.Timer.stopwatch(t.Timer(False))

    # Searching
    headlines("Searching", '#')
    data_length = array_length(customers)
    name_list = random.choices(customers[0:data_length], k=10)

    for i in range(10):
        name_list.append(mock.rand_name())

    print(data_length)
    for count, item in enumerate(name_list):
        t.Timer.stopwatch(t.Timer(True, "[{}]. Search {} ".format(count, item)))
        search_option_b(customers, data_length, item)
        t.Timer.stopwatch(t.Timer(False))

    # Delete
    headlines("Delete", '#')
    name_list = random.choices(customers[0:data_length], k=10)
    for i in range(10):
        name_list.append(mock.rand_name())

    for count, item in enumerate(name_list):
        t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
        delete_option_b(customers, data_length, item)
        t.Timer.stopwatch(t.Timer(False))
