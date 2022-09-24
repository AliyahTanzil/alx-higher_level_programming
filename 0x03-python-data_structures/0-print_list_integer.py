#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(10):
        my_list.append(i)
        print("{}".format(i), sep="\n")

print_list_integer(my_list)
