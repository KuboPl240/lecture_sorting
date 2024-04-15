import os
import numpy as np
import csv

def selection_sort(sorting_list,direction):
    for i in range(0,len(sorting_list)):
        index_min = np.argmin(sorting_list[i:])
        sorting_list[0+i], sorting_list[index_min+i] = sorting_list[index_min+i], sorting_list[0+i]
    return sorting_list

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    return_dict = dict()
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, encoding="windows-1250", newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for key in data.fieldnames:
            return_dict[key] = list()
        for row in data.reader:
            for i in range(0,len(row)):
                return_dict[data.fieldnames[i]].append(row[i])
    return return_dict


def main():
    sort_list = read_data("numbers.csv")["series_1"]
    print(selection_sort(sort_list,True))
    


if __name__ == '__main__':
    main()
