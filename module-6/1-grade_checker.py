#/usr/bin/python3

# Ask the user to enter a score between 0 and 100
score_input = input("Enter your score (0–100): ")

try:
    # Convert input to an integer
    score = int(score_input)

    # Check if the score is within the valid range
    if 0 <= score <= 100:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a number.")
