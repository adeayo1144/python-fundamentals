#!/usr/bin/python3
"""a module on how to create a queue"""
import queue
task=queue.Queue()
task.put("task1")
task.put("task2")
print(task.get())
