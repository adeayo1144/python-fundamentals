#/usr/bin/python3
def read_student_data(filename="data.txt"):
    students = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            try:
                name, age, score = line.split(",")
                student = {
                    "name": name.strip(),
                    "age": int(age.strip()),
                    "score": float(score.strip())
                }
                students.append(student)
            except ValueError:
                with open("error_log.txt", "a") as error_file:
                    error_file.write(f"Line {line_number}: Invalid format -> {line}\n")
    
    except FileNotFoundError:
        print("Data file not found.")
    
    return students

def print_students_table(students):
    if not students:
        print("No valid student records found.")
        return

    print("\nValid Student Records:")
    print("{:<10} {:<5} {:<6}".format("Name", "Age", "Score"))
    print("-" * 25)
