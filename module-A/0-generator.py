#/usr/bin/python3
""" a module that generates a number between and 5"""

def generate_number(start,end):
    """a function that generates a number between start and end"""
    while start <= end:
        yield start
        start +=1
    return start



if __name__ == "__main__":
    print(list(generate_number(1, 5)))
    #for number in generate_number(1,5):
        #print(number)