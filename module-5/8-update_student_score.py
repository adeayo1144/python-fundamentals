def update_score(students, name, new_score):
    """
    Updates the score of a student in the dictionary. If the student does not exist, adds them.

    Args:
        students (dict): A dictionary of student names and scores.
        name (str): The name of the student.
        new_score (int): The new score of the student.

    Returns:
        dict: The updated dictionary of student names and scores.
    """
    # Update the score of the student if the name exists; otherwise, add the student
    students[name] = new_score
    
    return students
students = {"Ali": 80, "Tobi": 90}
print(update_score(students, "Ali", 95))  # Output: {'Ali': 95, 'Tobi': 90}
print(update_score(students, "Sarah", 88))
