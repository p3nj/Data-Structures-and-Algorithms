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

solutions = ["OptionA", "OptionB"]

res_headers = {
    'Insertion': ["Problem Size", "Database Size", "Database Usage", "%", "Elapsed (ms)"],
    'Search': ["Customer Size", "Database Size", "Search Keyword", "Found", "Elapsed (ms)"],
    'Delete': ["Customer Size", "Database Size", "Delete Keyword", "Delete", "Elapsed (ms)"],
}
res_rows = {'Insertion': [],
            'Search': [],
            'Delete': []}
total_results = {'Insertion': [],
                 'Search': [],
                 'Delete': []}


def simulation(database_lst, problem_lst, test_rounds, output):
    # Option A
    # Insertion
    headlines("Insertion", '#')
    for solution in solutions:
        headlines("Benchmarking {}".format(solution), '-')
        for i in database_lst:
            for j in problem_lst:
                data_length = array_length(i)
                # Insertion
                if solution == solutions[0]:
                    t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
                    for k in j:
                        i, data_length = insert_option_a(i, data_length, k)
                    elapsed_time = t.Timer.stopwatch(t.Timer(False))

                else:
                    t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
                    for k in j:
                        i, data_length = insert_option_b(i, data_length, k)
                    elapsed_time = t.Timer.stopwatch(t.Timer(False))

                res_rows['Insertion'].append([str(len(j)), str(len(i)),
                                              str(array_length(i)) + '/' + str(len(i)),
                                              str("{:.2f}".format(((array_length(i) / len(i)) * 100))),
                                              str("{:.5f}".format(elapsed_time))])

                # Search
                # Pick names from database
                name_list = mock.rand_name(5)
                name_list += choices(i[0:data_length], k=5)

                if solution == solutions[0]:
                    for k in name_list:
                        t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
                        found = search_option_a(i, k)
                        result = t.Timer.stopwatch(t.Timer(False))
                        res_rows['Search'].append([str(len(j)), str(len(i)),
                                                   str(k),
                                                   found > 0,
                                                   str("{:.5f}".format(result))])
                else:
                    for k in name_list:
                        t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
                        found = search_option_b(sort_array(i), data_length, k)
                        result = t.Timer.stopwatch(t.Timer(False))
                        res_rows['Search'].append([str(len(j)), str(len(i)),
                                                   str(k),
                                                   found > 0,
                                                   str("{:.5f}".format(result))])



                # Delete
                # Pick names from database
                name_list = mock.rand_name(5)
                name_list += choices(i[0:data_length], k=5)
                if solution == solutions[0]:
                    for count, item in enumerate(name_list):
                        t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
                        delete, data_length = delete_option_a(i, data_length, item)
                        result = t.Timer.stopwatch(t.Timer(False))
                        res_rows['Delete'].append([str(len(j)), str(len(i)),
                                                   str(item),
                                                   delete == 0,
                                                   str("{:.5f}".format(result))])
                else:
                    for count, item in enumerate(name_list):
                        t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
                        delete, data_length = delete_option_b(sort_array(i), data_length, item)
                        result = t.Timer.stopwatch(t.Timer(False))
                        res_rows['Delete'].append([str(len(j)), str(len(i)),
                                                   str(item),
                                                   delete == 0,
                                                   str("{:.5f}".format(result))])

                i = [None for _ in i]

            for j in res_rows.keys():
                total_results[j].append(res_rows[j])

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