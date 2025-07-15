#usr/bin/python3
"""A module for the teacher"""
from person import Person

class Teacher(Person):
    """ A class that defines a teacher by its name, aage and subject"""
    def __init__ (self, name, age, subject):
        super(). __init__(name, age)
        self.subject = subject


    def teach(self):
        """Print a message indicating the teacher is teaching their subject."""
        print(f" {self.name} is teaching {self.subject}.")