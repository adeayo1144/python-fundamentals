#/usr/bin/python3
"""a module that can write information in the public attribute"""
class Person:
    
    name = ""
    age = 30

if __name__ =='__main__':
    person = Person()
    person.name = "joseph"
   # person.age = 29
    print(person.name,person.age)