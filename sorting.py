import os
import numpy as np
import csv

def selection_sort(sorting_list,direction):
    if direction:
        for i in range(0,len(sorting_list)):
          index_min = np.argmin(sorting_list[i:])
          sorting_list[0+i], sorting_list[index_min+i] = sorting_list[index_min+i], sorting_list[0+i]
    
    else:
      for i in range(0,len(sorting_list)):
          index_max = np.argmax(sorting_list[:len(sorting_list)-i-1])
          sorting_list[len(sorting_list)-i-1], sorting_list[index_max-i] = sorting_list[index_max-i], sorting_list[len(sorting_list)-i-1]

    return sorting_list

def bubble_sort(sorting_list,direction):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(0,len(sorting_list)-1):
            if direction and int(sorting_list[i])>int(sorting_list[i+1]) or not direction and int(sorting_list[i])<int(sorting_list[i+1]):
                sorting_list[i+1], sorting_list[i] = sorting_list[i], sorting_list[i+1] 
                not_sorted = True
    return sorting_list

def insertion_sort(sorting_list,direction):
    for i in range(0,len(sorting_list)):
        print(i)
        for i_sorted in range(0,i):
            if sorting_list[i_sorted]>sorting_list[i]:
                item = sorting_list[i]
                sorting_list[1:] = sorting_list[:len(sorting_list)len(sorting_list)
                sorting_list[0]= item
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
    sort_list = read_data("numbers.csv")["series_2"]
    print(insertion_sort(sort_list,True))
    


if __name__ == '__main__':
    main()
