#!/usr/bin/python3
"""a module that set queue limits"""
import queue
q= queue.Queue(maxsize=3)
q.put("a")
q.put("b")
q.put("c")
print(q.full())
print(q.size())

