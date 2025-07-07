#/usr/bin/python3
def collect_student_scores():
    scores = {}

    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == "done":
            break

        try:
            score_input = input(f"Enter score for {name} (0–100): ").strip()
            score = float(score_input)

            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue

            scores[name] = score

        except ValueError:
            print("Invalid input. Please enter a numeric value for the score.")

    return scores

def write_scores_to_file(scores, filename="scores.txt"):
    try:
        with open(filename, "w") as file:
            for name, score in scores.items():
                file.write(f"{name}: {score}\n")
        print(f"Scores saved to {filename}.")
    except IOError:
        print("An error occurred while writing to the file.")

