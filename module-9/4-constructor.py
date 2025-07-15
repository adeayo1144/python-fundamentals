#/usr/bin/python3
"""a module that make use of s constructor to assign valuess"""
class Person:
    
   def __init__(self, name, age)
        self.name = name
        self.age = age

    def greet(self):
        print("Good morning {}". format(self.name))

if __name__ == '__main__':
    person = Person("john" , 30)
    person.name = "john"
    person.greet()