#!/usr/bin/python3
"""" a module that create a binary tree"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Binarytree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value < root.value:
            if root.left == None:
                root.left = Node(value)
            else:
                self._insert(root.left, value)
        else:
            if root.right == None:
                root.right = Node(value)
            else:
                self._insert(root.right, value)

    def printtree(self, current):
        if current:
            self.printtree(current.left)
            print(current.value)
            self.printtree(current.right)




if __name__ == "__main__":
    binary = Binarytree()
    binary.insert(2)
    binary.insert(3)
    binary.insert(4)
    binary.insert(5)
    print(binary.root.right.value)
    print(binary.root.right.right.value)
    print(binary.root.right.right.right.value)
    

    #binary.printtree(binary)




    


