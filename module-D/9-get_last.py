#!/usr/bin/python3
"""a module that get the last element in a linked list"""

Linkedlist = __import__("8-create-linkedlist").linkedList

if __name__ == "__main__":
    my_list = Linkedlist()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    
    my_list.print_list()
    print(my_list.print_last())