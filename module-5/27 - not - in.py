#!/usr/bin/python3
""" a module that check for memebership test on a dictionary"""
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
print ("color" not in laptop)
print ("probook" not in laptop)
print ("age" not in laptop)