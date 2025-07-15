#usr/bin/python3
"""A module for school catlog"""
class School:
    """ A CLASS THAT DEFINES a school by its name and list of corses"""

    def __init__ (self, name, address):
        """Initializes the school with empty lists for teachers, students and courses"""
        self.name = name
        self.address = address
        self.teachers = []
        self.students = []
        self.courses = []

    def add_teacher(self, teacher):
        """Adds a teahcer to the school's list of teachers"""
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        
    def add_student(self, student):
        """Adds a student to the school's list of students"""
        if student not in self.students:
            self.students.append(student)

    def add_course(self, course):
        """Adds a course to the school's list of courses."""
        if course not in self.courses:
            self.courses.append(course)

    def list_teacher(self):
        """a method that list all teachers in the school"""
        for teacher in self.teachers:
            print(f"Teacher: {teacher.name},Subject: {teacher.subject}")

    def list_student(self):
        """a method that list all students in the school"""
        for student in self.students:
            print(f"student: {student.name}, Age: {student.age}, ID: {student.student_id}")

    def list_courses(self):
        """a method that list all courses in the school"""
        for course in self.courses:
            print(f"Course: {course.course_name}, Code: {course.course_code}")

if __name__ == "__main__":
    from teacher import Teacher
    from student import Student
    from course import Course

    school = School("Capital City of Knowledge international School", " 3rd agate Kurudu, Abuja ")

    teacher = Teacher("Mr Idoko Christian", 40, "Mathematics")
    student = Student("Ayo John" , 19, "cckis214")
    course = Course("Agricultural Science" , "agric101")

    student.enroll(course)
    school.add_teacher(teacher)
    school.add_student(student)
    school.add_course(course)

    print(f"School Name: {school.name}, Address: {school.address}")
    print("\nTeachers in the school")
    school.list_teacher()
    print("\nstudents in the school:")
    school.list_student()
    print("\ncourses offered by the school:")
    school.list_courses()




