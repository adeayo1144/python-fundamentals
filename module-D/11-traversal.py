#!/usr/bin/python3
"""a module that traverse a tree"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data, end="-->")
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data, end="--> ")
        pass
    
    def preOrder(self):
        print(self.data, end="-->")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2) 
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("preOrder Traversal")
    root.preOrder()
    print("Post Order Traversal")
    root.postOrder()
    print("InOrder Traversal") 
    root.inOrder  
