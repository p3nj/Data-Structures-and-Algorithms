import sys
from datetime import datetime

import numpy as np
from tabulate import tabulate

from utils import create_result_dir


class DataTable:
    def __init__(self):
        self.headers = None
        self.rows = None

    def build(self, headers, rows):
        self.headers = headers
        self.rows = rows

    def print(self):
        data_array = np.array(self.rows)
        table = tabulate(data_array, self.headers, tablefmt="fancy_grid")
        print(table)

    def save(self, header):
        dir = create_result_dir(header.split("_")[:2])
        data_array_with_header = np.vstack((self.headers, np.asarray(self.rows)))
        timestamp = datetime.now().strftime("%H-%M-%S")
        np.savetxt(dir + "/" + timestamp + "_" + header + ".csv", data_array_with_header, fmt='%s', delimiter=',')

        # def print(self):
    #     widths = [max(len(str(self.headers[i])) for row in self.rows) for i in range(len(self.rows[0]))]
    #     # print the header
    #     for i in range(len(self.headers)):
    #         print(self.headers[i].ljust(widths[i]), end="  ")
    #     print()
    #     # inert row data
    #     for row in self.rows:
    #         for i in range(len(row)):
    #             # Left-align string, right for numbers
    #             if isinstance(row[i], str):
    #                 print(row[i].ljust(widths[i]), end="  ")
    #             else:
    #                 print(str(row[i]).rjust(widths[i]), end="  ")
    #         print()