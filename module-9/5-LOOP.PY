#/usr/bin/python3
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

# Create multiple Person instances
person1 = Person("jOHN")
person2 = Person("HENRY")
person3 = Person("AYOMIDE")

# Store them in a list
people = [person1, person2, person3]

# Loop through the list and call greet() for each person
for person in people:
    person.greet()
