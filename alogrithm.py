from random import random, choices
from algorithms.delete import delete_option_a
from algorithms.insertion import insert_option_a
from algorithms.search import search_option_a
from lib import rand_names as mock
from utils import headlines, fib, array_length, flatten
from lib.datatable import DataTable
from lib import timer as t


def option_a(database_lst, problem_lst):
    # Option A
    # Insertion
    headlines("Insertion", '#')
    headlines("Benchmarking option A", '-')
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
    for i in database_lst:
        for j in problem_lst:
            data_length = array_length(i)

            # Insertion
            headlines("Insertion PS:{} DBS:{}".format(len(j), len(i)), '#')
            t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
            for k in j:
                customers, data_length = insert_option_a(i, data_length, k)
            result = t.Timer.stopwatch(t.Timer(False))

            res_rows['Insertion'].append([str(len(j)), str(len(i)),
                                          str(array_length(i)) + '/' + str(len(i)),
                                          str("{:.2f}".format(((array_length(i) / len(i)) * 100))),
                                          str("{:.5f}".format(result))])

            # Search
            # Pick names from database
            headlines("Search PS:{} DBS:{}".format(len(j), len(i)), '#')
            name_list = mock.rand_name(5)
            name_list += choices(i[0:data_length], k=5)

            for k in name_list:
                t.Timer.stopwatch(t.Timer(True, "PS:{}, DBS:{}".format(len(j), len(i))))
                found = search_option_a(i, k)
                result = t.Timer.stopwatch(t.Timer(False))

                res_rows['Search'].append([str(len(j)), str(len(i)),
                                           str(k),
                                           "True" if found != -1 else "False",
                                           str("{:.5f}".format(result))])

            # Delete
            headlines("Delete PS:{} DBS:{}".format(len(j), len(i)), '#')
            # Pick names from database

            for count, item in enumerate(name_list):
                t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
                delete = delete_option_a(i, data_length, item)
                if delete != -1:
                    delete = True
                else:
                    delete = False
                result = t.Timer.stopwatch(t.Timer(False))

                res_rows['Delete'].append([str(len(j)), str(len(i)),
                                           str(item),
                                           delete,
                                           str("{:.5f}".format(result))])

            i = [None for _ in i]

        for j in res_rows.keys():
            total_results[j].append(res_rows[j])
    export_report(total_results, res_headers)


def export_report(total_results, res_headers):
    table = DataTable()
    for i in total_results.keys():
        for count, j in enumerate(total_results[i]):
            headlines("building report: {}, {}".format(res_headers, j), '@')
            table.build(res_headers[i], j)
            table.save("OptionA_{}_{}".format(i, count))
    # for count, i in enumerate(total_results):
    #     table.build(res_headers, i)
    #     # table.print()
    #     table.save("OptionA_Insertion_{}".format(count))

    # t.Timer.stopwatch(t.Timer(True, "Insertion Option A. 5_000 items."))
    # for item in new_customers:
    #     customers, data_length = insert_option_a(customers, data_length, item)
    # t.Timer.stopwatch(t.Timer(False))

    # # Delete
    # headlines("Delete", '#')
    # name_list = random.choices(customers[0:data_length], k=10)
    # for i in range(10):
    #     name_list.append(mock.rand_name())

    # for count, item in enumerate(name_list):
    #     t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
    #     delete_option_a(customers, data_length, item)
    #     t.Timer.stopwatch(t.Timer(False))

    # headlines("Cleaning customers database", '@')

    # customers = [None if x is not None else None for x in customers]
    # data_length = array_length(customers)

    # print(data_length)

    # # Option B
    # headlines("Benchmarking option B", '-')
    # t.Timer.stopwatch(t.Timer(True, "Generate 5_000 random names to array using Option B"))
    # for item in new_customers:
    #     customers, data_length = insert_option_b(customers, data_length, item)
    # t.Timer.stopwatch(t.Timer(False))

    # # Searching
    # headlines("Searching", '#')
    # data_length = array_length(customers)
    # name_list = random.choices(customers[0:data_length], k=10)

    # for i in range(10):
    #     name_list.append(mock.rand_name())

    # print(data_length)
    # for count, item in enumerate(name_list):
    #     t.Timer.stopwatch(t.Timer(True, "[{}]. Search {} ".format(count, item)))
    #     search_option_b(customers, data_length, item)
    #     t.Timer.stopwatch(t.Timer(False))

    # # Delete
    # headlines("Delete", '#')
    # name_list = random.choices(customers[0:data_length], k=10)
    # for i in range(10):
    #     name_list.append(mock.rand_name())

    # for count, item in enumerate(name_list):
    #     t.Timer.stopwatch(t.Timer(True, "[{}]. Delete {} ".format(count, item)))
    #     delete_option_b(customers, data_length, item)
    #     t.Timer.stopwatch(t.Timer(False))
