#!/usr/bin/python3
"""a module that handle the creation of a linkedlist"""

class Node:
    """This clss is the node in a linked list"""
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_last(self):
        if not self.head:
            return None
        while self.head.next:
            self.head = self.head.next
        return self.head.data

    def print_first(self):
        if not self.head:
            return None
        return self.head.data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " ->")
            current = current.next
        print("None")

if __name__ == "__main__":
    my_list = linkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.print_list()
