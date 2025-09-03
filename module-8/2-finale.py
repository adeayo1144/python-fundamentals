#!/usr/bin/python3
"""a module that handles a final statement"""
try:
    with open ("newfile.txt", 'w+r') as f:
        f.write("in the domain of mobile edge computer security, significant stripes as been made through the integration of artificial intelligence and machine learning")
        print(f.read())
except Exception as e:
    print (e)
finally:
    print ("file close" )


