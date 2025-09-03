#!/usr/bin/python3
""" a module that retrieve sorted order without modifying the original heap"""
import heapq
heap = [10,20,15,30,40]
heapq.heapify(heap)

sorted_heap = heapq.nsmallest(len(heap), heap)
print(sorted_heap)


print(heap)
