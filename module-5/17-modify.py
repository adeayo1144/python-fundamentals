#!/usr/bin/python3
def modify_tuple(tupl,elem):
    my_list = list(tupl)
    my_list.append(elem)
    
    return tuple(my_list)
    
result = modify_tuple((1,2,3), 4)
print(result)
    