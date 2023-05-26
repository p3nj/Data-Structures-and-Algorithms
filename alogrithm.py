import timeit
from functools import partial
from random import choices
from algorithms.delete import delete_option_a, delete_option_b
from algorithms.insertion import insert_option_a, insert_option_b
from algorithms.search import search_option_a, search_option_b
from lib import rand_names as mock
from utils import headlines, array_length, sort_array
from lib.datatable import DataTable
from lib import timer as t
from lib.logger import mylogger as logger

solutions = ["OptionA", "OptionB"]

res_headers = {
    'Insertion': ["Problem Size", "Database Size", "Database Usage", "%", "Elapsed (ms)"],
    'Search': ["Customer Size", "Database Size", "Search Keyword", "Type", "Elapsed (ms)"],
    'Delete': ["Customer Size", "Database Size", "Delete Keyword", "Type", "Elapsed (ms)"]}

res_rows = {'Insertion': [],
            'Search': [],
            'Delete': []}
total_results = {'Insertion': [],
                 'Search': [],
                 'Delete': []}


def insertion_simulation(db_lst, prob_lst, solution, data_length):
    db_lst = [None for _ in db_lst]
    if solution == solutions[0]:
        t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(prob_lst), len(db_lst))))
        for k in prob_lst:
            db_lst, data_length = insert_option_a(db_lst, data_length, k)

    else:
        sorted_i = sort_array(db_lst)
        t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(prob_lst), len(db_lst))))
        for k in prob_lst:
            db_lst, data_length = insert_option_b(sorted_i, data_length, k)

    elapsed_time = t.Timer.stopwatch(t.Timer(False))

    res_rows['Insertion'].append([str(len(prob_lst)), str(len(db_lst)),
                                  str(array_length(db_lst)) + '/' + str(len(db_lst)),
                                  str("{:.2f}".format(((array_length(db_lst) / len(db_lst)) * 100))),
                                  str("{:.9f}".format(elapsed_time))])
    return db_lst, data_length


def search_simulation(db_lst, prob_lst, solution, data_length):
    search_list = {
        'GOOD': mock.rand_name(1000),
        'BAD': choices(db_lst[0:data_length], k=1000)
    }

    for key in search_list.keys():
        elapsed_time = 0
        if solution == solutions[0]:
            for k in search_list[key]:
                t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(prob_lst), len(db_lst))))
                search_option_a(db_lst, k)
        else:
            for k in search_list[key]:
                sorted_i = sort_array(db_lst)
                t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(prob_lst), len(db_lst))))
                search_option_b(sorted_i, data_length, k)

        result = t.Timer.stopwatch(t.Timer(False))
        elapsed_time += result
        res_rows['Search'].append([str(len(prob_lst)), str(len(db_lst)),
                                   len(search_list[key]),
                                   key,
                                   str("{:.9f}".format(elapsed_time))])


def delete_simulation(db_lst, prob_lst, solution, data_length):
    # Pick names from database
    delete_list = {
        'BAD': mock.rand_name(1000),
        'GOOD': choices(db_lst[0:data_length], k=1000)
    }

    for key in delete_list.keys():
        elapsed_time = 0
        if solution == solutions[0]:
            for count, item in enumerate(delete_list[key]):
                t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
                delete, data_length = delete_option_a(db_lst, data_length, item)
        else:
            for count, item in enumerate(delete_list[key]):
                sorted_i = sort_array(db_lst)
                t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
                delete, data_length = delete_option_b(sorted_i, data_length, item)

        result = t.Timer.stopwatch(t.Timer(False))
        elapsed_time += result
        res_rows['Delete'].append([str(len(prob_lst)), str(len(db_lst)),
                                   len(delete_list[key]),
                                   key,
                                   str("{:.9f}".format(elapsed_time))])


def simulation(database_lst, problem_lst, test_rounds, output):
    logger.info("Simulation started...")
    for solution in solutions:

        global res_rows
        global total_results

        res_rows = {'Insertion': [],
                    'Search': [],
                    'Delete': []}
        total_results = {'Insertion': [],
                         'Search': [],
                         'Delete': []}

        logger.info("Benchmarking {}".format(solution))
        for i in database_lst:
            for j in problem_lst:
                for count in range(test_rounds):
                    data_length = array_length(i)
                    logger.info("[{}] Insertion {} PS:{} DBS:{} DL:{}".format(count, solution, len(j), len(i),
                                                                              data_length))
                    db_lst, data_length = insertion_simulation(i, j, solution, data_length)

                    logger.info("[{}] Search {} PS:{}, DBS:{}, DL:{}".format(count, solution, len(j), len(db_lst),
                                                                             data_length))
                    search_simulation(db_lst, j, solution, data_length)

                    logger.info("[{}] Delete {} PS:{}, DBS:{}, DL:{}".format(count, solution, len(j), len(db_lst),
                                                                             data_length))
                    delete_simulation(db_lst, j, solution, data_length)

        for i in res_rows.keys():
            total_results[i].append(res_rows[i])

        export_report(solution, total_results, res_headers, output)


def export_report(solution, results, headers, output):
    table = DataTable()
    for i in results.keys():
        for count, j in enumerate(results[i]):
            headlines("Building Report:", '+', end=False)
            headlines("{}, {}".format(solution, i), '+')
            table.build(headers[i], j)
            if output:
                table.save("{}_{}_{}".format(solution, i, count))

            else:
                table.print()
