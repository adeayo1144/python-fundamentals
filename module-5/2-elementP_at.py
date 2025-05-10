#!/usr/bin/python3
"""Write a function that retrieves an element from a list"""
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    car = ["toyota" , "benz", "ferarri"]
    result= element_at(car,3)
    print(result)

 