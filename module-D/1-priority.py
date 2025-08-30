#!/usr/bin/python3
"""a module that handle priority queue"""
from queue import PriorityQueue
task=PriorityQueue()
task.put((2, "task1"))
task.put((1, "task2"))
print(task.get())
