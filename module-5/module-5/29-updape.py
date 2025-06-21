#!/usr/bin/python3
"""a module that updates a value of a dictionary"""
laptop = {
    "brand" : "Hp",
    "model" : "rog",
    "year" : 2021,
    "price" : 120000.00,
    "color" : "pink",
    "processor" : "Intel 15",
    "ram" :  4,
    "storage" : 500,
    "cpu" : "Geforce",
    "battery" : "4 - cell ",
}
laptop.update({"price" : 1500000.00})
laptop . update({"size" : "15.5 inchs"})
print(laptop)