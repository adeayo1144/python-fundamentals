#/usr/bin/python3
class StudentNotFoundError(Exception):
    """Custom exception for student not found."""
    pass

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
]

def find_student_age(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student["age"]
    raise StudentNotFoundError

try:
    search_name = input("Enter the student's name: ")
    age = find_student_age(search_name)
    print(f"{search_name} is {age} years old.")
except StudentNotFoundError:
    print("Student not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
