def generate_report_card(data):
    """
    Generates a report card for each student in the input dictionary.

    Args:
        data (dict): A dictionary where the key is a student's name and the value is a list of their scores.

    Returns:
        dict: A dictionary showing each student's total score, average score, and grade.
    """
    report_card = {}
    
    for student, scores in data.items():
        total_score = sum(scores)
        average_score = total_score / len(scores)
        
        if average_score >= 70:
            grade = "A"
        elif average_score >= 60:
            grade = "B"
        elif average_score >= 50:
            grade = "C"
        elif average_score >= 40:
            grade = "D"
        else:
            grade = "F"
        
        report_card[student] = {
            "total_score": total_score,
            "average_score": round(average_score, 2),
            "grade": grade
        }
    
    return report_card
students = {
    "Aliyu": [75, 80, 68],
    "Zainab": [55, 60, 58],
    "Emeka": [30, 42, 35]
}

result = generate_report_card(students)
print(result)
