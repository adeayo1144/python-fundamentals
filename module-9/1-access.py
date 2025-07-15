#/usr/bin/python3
"""a module that access the attribute of a class"""
class Person:
    """A class that handle the persons information
    using a public attribute
    """
    name = "hey why"
    age = 29

if __name__ =='__main__':
    person = Person()
    print(person.name)
    print(person.age)