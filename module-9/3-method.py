#/usr/bin/python3
"""a module that adds a method to class"""
class Person:
    
    name = ""
    age = 0

    def greet(self):
        print("Good morning {}". format(self.name))


if __name__ =="__main__":
    person = Person()
   # person.name = "joshua"

    person.greet()