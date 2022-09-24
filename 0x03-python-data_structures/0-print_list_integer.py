#!/usr/bin/python3
<<<<<<< HEAD
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
=======

def print_list_integer(my_list=[]):
    for i in range(10):
        my_list.append(i)
        print("{}".format(i), sep="\n")

my_list=[]
print_list_integer(my_list)
>>>>>>> 7cd2028ca2a03ce1e9367abe7eeb1024f0ee06b1
