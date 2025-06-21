#!/usr/bin/python3
"""a module that performs membership test on a dictionary"""
laptop = dict(
    brand = "hp",
    model =" ROG sTRIX" , 
    year = "2021" , 
    price = "150000" , 
    color = " pink" , 
    processor = "intel 15" , 
    ram = "4" , 
    storage = "500" ,
    gpu = "GEOFORCE",
    battery = "4 cell",
)
print ("color" in laptop)
print ("probook" in laptop)
print ("age" in laptop)