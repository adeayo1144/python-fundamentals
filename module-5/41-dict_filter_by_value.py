#!/usr/bin/python3
def filter_dict_by_value(dictionary, threshold):
    return {key: value for key, value in dictionary.items() if value > threshold}
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(filter_dict_by_value(my_dict, 2))
