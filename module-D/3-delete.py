#!/usr/bin/python3
"""a module that delete queue"""
import queue
q=queue.Queue()
q.put("a")
q.put("b")
q.put("c")
q.empty()

remove=q.get()
print(remove)
