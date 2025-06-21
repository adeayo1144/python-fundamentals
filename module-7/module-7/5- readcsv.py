#!/usr/bin/python3
"""Read a CSV file and print its contents."""
import csv

with open("eggs.csv", "r" ) as csvfile:
    reader = csv . reader(csvfile, delimiter=",")
    for row in reader:
        print(' '.join (row))