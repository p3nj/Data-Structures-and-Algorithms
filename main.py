import argparse
import logging
import os
import pickle
import time

from alogrithm import simulation
from lib import rand_names as mock
from lib.logger import mylogger as logger
from utils import fib
from config import Config as cfg


def preload(reset):
    problems_lst = []
    databases_lst = []
    if reset is True:
        logging.debug("Delete Problem size bin file")
        os.remove(cfg.PROBLEM_SIZE_FILE)
        logging.debug("Delete Database size bin file")
        os.remove(cfg.DATABASE_SIZE_FILE)

    if os.path.exists(cfg.PROBLEM_SIZE_FILE) is not True:
        # Preset problem sizes using fibonacci algorithm
        logging.debug("Generating mock data using fibonacci")
        for i in [fib(j + cfg.FIBONACCI_LEVEL) for j in range(cfg.SAMPLE_SIZE)]:
            problems_lst.append(mock.rand_name(i))
        logging.debug("Save the problem size file as {}".format(cfg.PROBLEM_SIZE_FILE))
        with open(cfg.PROBLEM_SIZE_FILE, "wb") as f:
            pickle.dump(problems_lst, f)
    else:
        logging.debug("Loading the problem size file from {}".format(cfg.PROBLEM_SIZE_FILE))
        with open(cfg.PROBLEM_SIZE_FILE, "rb") as f:
            problems_lst = pickle.load(f)

    if os.path.exists(cfg.DATABASE_SIZE_FILE) is not True:
        # Preset database sizes using fibonacci algorithm
        logging.debug("Generating mock data using fibonacci")
        db_set = ([None] * fib(i + cfg.FIBONACCI_LEVEL) for i in range(cfg.SAMPLE_SIZE))
        databases_lst = [*db_set]
        logging.debug("Save the database size file as {}".format(cfg.PROBLEM_SIZE_FILE))
        with open(cfg.DATABASE_SIZE_FILE, "wb") as f:
            pickle.dump(databases_lst, f)
    else:
        logging.debug("Loading the Database size file from {}".format(cfg.PROBLEM_SIZE_FILE))
        with open(cfg.DATABASE_SIZE_FILE, "rb") as f:
            databases_lst = pickle.load(f)
            logging.debug("File loaded... data length: {}".format(len(databases_lst)))

    return problems_lst, databases_lst


if '__main__' == __name__:
    reset_data = False
    parser = argparse.ArgumentParser(
        description='This little program demonstrated simple algorithm implemented as python.')

    parser.add_argument('-l', '--fibonacci-level',
                        help='set the level of fibonacci when generate data starts (def: 20)')
    parser.add_argument('-s', '--sample-size', help='Set the amount of samples should generated.\n'
                                                    'Change this value will trigger reset (def: 5)')
    parser.add_argument('-n', '--numbers', help='How many times you want to test the algorithms. (def: 10)')
    parser.add_argument('-o', '--output', help='Output report as csv inside YY-MM-DD directory.', action='store_true')
    parser.add_argument('-r', '--reset', help='Reset .bin files and regenerate a new one.\n'
                                              'With this value will trigger reset', action='store_true')
    parser.add_argument('-v', '--verbose', help='noisy program', action='store_true')
    args = parser.parse_args()

    args.reset = reset_data

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("DEBUG ENABLED!!! I WILL BE NOISY!!!")

    if args.sample_size:
        SAMPLE_SIZE = args.sample_size
        reset_data = True
    if args.fibonacci_level:
        FIBONACCI_LEVEL = args.fibonacci_level
        reset_data = True
    if args.numbers:
        TEST_ROUND = args.numbers

    logger.info("\nArguments Loaded!!\n"
                "Reset: {}\n"
                "Fibonacci Level: {}\n"
                "Sample Size: {}\n"
                "Test Rounds: {}\n"
                "Output to CSV: {}".format(reset_data,
                                           cfg.FIBONACCI_LEVEL,
                                           cfg.SAMPLE_SIZE,
                                           cfg.TEST_ROUND,
                                           args.output))

    time.sleep(1)
    print("Press any key to continue...")
    input()

    problem_lst, database_lst = preload(reset_data)
    simulation(database_lst, problem_lst, cfg.TEST_ROUND, args.output)
