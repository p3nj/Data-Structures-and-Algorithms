import os
import pickle

from alogrithm import option_a
from lib import rand_names as mock
from lib import timer as t
from utils import headlines, fib, array_length, flatten

PROBLEM_SIZE_FILE = "prob_sizes.bin"
DATABASE_SIZE_FILE = "databases.bin"
TEST_ROUND = 1000


def preload():
    problems_lst = []
    databases_lst = []
    if os.path.exists(PROBLEM_SIZE_FILE) is not True:
        t.Timer.stopwatch(t.Timer(True, "Prefixing problem size..."))
        # Preset problem sizes using fibonacci algorithm
        for i in [fib(j + 25) for j in range(5)]:
            problems_lst.append(mock.rand_name(i))
        t.Timer.stopwatch(t.Timer(False))
        with open(PROBLEM_SIZE_FILE, "wb") as f:
            pickle.dump(problems_lst, f)
    else:
        with open(PROBLEM_SIZE_FILE, "rb") as f:
            problems_lst = pickle.load(f)

    if os.path.exists(DATABASE_SIZE_FILE) is not True:
        t.Timer.stopwatch(t.Timer(True, "Prefixing database size..."))
        # Preset database sizes using fibonacci algorithm
        db_set = ([None] * fib(i + 25) for i in range(5))
        databases_lst = [*db_set]
        t.Timer.stopwatch(t.Timer(False))
        with open(DATABASE_SIZE_FILE, "wb") as f:
            pickle.dump(databases_lst, f)
    else:
        with open(DATABASE_SIZE_FILE, "rb") as f:
            databases_lst = pickle.load(f)

    return problems_lst, databases_lst


if '__main__' == __name__:
    problem_lst, database_lst = preload()
    option_a(database_lst, problem_lst)
