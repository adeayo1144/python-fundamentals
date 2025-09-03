#!/usr/bin/python3
""" a module that pops elements from smallest to largest"""
import heapq
heap = [10,20,15,30,40]
heapq.heapify(heap)

while heap:
    smallest = heapq.heappop(heap)
    print(smallest)

