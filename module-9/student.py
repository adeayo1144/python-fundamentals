#usr/bin/python3
from person import Person

class Student(Person):
    """ A class that defines a student by its name, aGE AND STUDENT ID"""
    def __init__ (self, name, age, student_id):
        super(). __init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        """Enrolls the student in a course."""
        if course not in self.courses:
            self.courses.append(course)