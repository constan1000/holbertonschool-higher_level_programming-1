#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            list[i] = replace
        return list
