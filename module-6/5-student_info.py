#/usr/bin/python3

# Create a tuple with student information
student_info = ("John Doe", 20, "Computer Science", 3.8)

# Print each element of the tuple
print("Student Information:")
print("Name:", student_info[0])
print("Age:", student_info[1])
print("Department:", student_info[2])
print("GPA:", student_info[3])

# Try changing the name (this will raise an error)
try:
    student_info[0] = "Jane Doe"
except TypeError as e:
    print("\nError when trying to change the name:")
    print(e)
