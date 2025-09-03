#!/usr/bin/python3
""" A module that prints the top 3 finisher in women 100metres olympic race"""
import heapq
result = ["christiana williams 11.80", "marie-josee ta 10.86", "elaina thompson 10.71", "torie bowie 10.71", 
"shelly ann 10.86", "english 10.94", "michelle 10.92", "dafne 10.90"]
top3 = heapq.nsmallest(3, result, key = lambda x: float(x.split()[-1]))
print(top3)
