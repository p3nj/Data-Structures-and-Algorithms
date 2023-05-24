import argparse
import os
import pickle

from alogrithm import simulation
from lib import rand_names as mock
from lib import timer as t
from utils import headlines, fib, array_length, flatten

PROBLEM_SIZE_FILE = "prob_sizes.bin"
DATABASE_SIZE_FILE = "databases.bin"
TEST_ROUND = 10


def preload(reset):
    problems_lst = []
    databases_lst = []
    if reset is True:
        os.remove(PROBLEM_SIZE_FILE)
        os.remove(DATABASE_SIZE_FILE)

    if os.path.exists(PROBLEM_SIZE_FILE) is not True:
        # Preset problem sizes using fibonacci algorithm
        for i in [fib(j + 20) for j in range(5)]:
            problems_lst.append(mock.rand_name(i))
        with open(PROBLEM_SIZE_FILE, "wb") as f:
            pickle.dump(problems_lst, f)
    else:
        with open(PROBLEM_SIZE_FILE, "rb") as f:
            problems_lst = pickle.load(f)

    if os.path.exists(DATABASE_SIZE_FILE) is not True:
        # Preset database sizes using fibonacci algorithm
        db_set = ([None] * fib(i + 20) for i in range(5))
        databases_lst = [*db_set]
        with open(DATABASE_SIZE_FILE, "wb") as f:
            pickle.dump(databases_lst, f)
    else:
        with open(DATABASE_SIZE_FILE, "rb") as f:
            databases_lst = pickle.load(f)

    return problems_lst, databases_lst


if '__main__' == __name__:
    parser = argparse.ArgumentParser(
        description='This little program demonstrated simple algorithm implemented as python.')

    parser.add_argument('-o', '--output', help='output report as csv inside YY-MM-DD directory.', action='store_true')
    parser.add_argument('-r', '--reset', help='reset .bin files and regenerate a new one.', action='store_true')
    args = parser.parse_args()

    problem_lst, database_lst = preload(args.reset)
    simulation(database_lst, problem_lst, TEST_ROUND, args.output)
