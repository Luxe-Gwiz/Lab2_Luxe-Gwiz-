
import csv

class Assignment:
    def __init__(self, name, group, score, weight):
        self.name = name
        self.group = group
        self.score = score
        self.weight = weight
        self.status = None

    def classify_grade(self):
        if self.score >= 50:
            self.status = "PASSED"
        else:
            self.status = "FAILED"


class Student:
    def __init__(self, student_code, name):
        self.student_code = student_code
        self.name = name
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def save_results(self, total_grade, gpa, formative, summative,
                     decision, resubmissions):

        filename = "results_" + self.student_code.replace(" ", "_") + ".csv"

        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "Student Code",
                    "Student Name",
                    "Assignment",
                    "Group",
                    "Score",
                    "Weight",
                    "Assignment Status",
                    "Formative Performance",
                    "Summative Performance",
                    "Total Grade",
                    "GPA",
                    "Final Decision",
                    "Resubmission"
                ])

                for assignment in self.assignments:
                    resubmission_status = (
                        "YES" if assignment in resubmissions else "NO"
                    )

                    writer.writerow([
                        self.student_code,
                        self.name,
                        assignment.name,
                        assignment.group,
                        assignment.score,
                        assignment.weight,
                        assignment.status,
                        round(formative, 2),
                        round(summative, 2),
                        round(total_grade, 2),
                        round(gpa, 2),
                        decision,
                        resubmission_status
                    ])

            print("\nResults successfully saved to:", filename)

        except Exception as e:
            print("Error saving results:", e)


def get_valid_score():
    while True:
        try:
            score = float(input("Enter assignment score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter assignment weight: "))
            if weight > 0:
                return weight
            print("Weight must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_valid_group():
    while True:
        group = input("Enter group (Formative/Summative): ").strip().title()
        if group in ["Formative", "Summative"]:
            return group
        print("Please enter Formative or Summative.")


def validate_scores(assignments):
    for assignment in assignments:
        if not 0 <= assignment.score <= 100:
            print("Invalid score:", assignment.name)
            return False
    return True


def validate_weights(assignments):
    formative_weight = 0
    summative_weight = 0

    for assignment in assignments:
        if assignment.group == "Formative":
            formative_weight += assignment.weight
        elif assignment.group == "Summative":
            summative_weight += assignment.weight

    total_weight = formative_weight + summative_weight

    print("\n--- Weight Validation ---")
    print("Formative:", formative_weight)
    print("Summative:", summative_weight)
    print("Total:", total_weight)

    if (formative_weight == 60 and
            summative_weight == 40 and
            total_weight == 100):
        print("Weights are valid.")
        return True

    print("Invalid weights. Required: Formative 60, Summative 40.")
    return False


def calculate_grade(assignments):
    total_grade = 0

    for assignment in assignments:
        contribution = assignment.score * assignment.weight / 100
        total_grade += contribution

    gpa = (total_grade / 100) * 5.0
    return total_grade, gpa


def category_performance(assignments, group):
    category_grade = 0
    category_weight = 0

    for assignment in assignments:
        if assignment.group == group:
            category_grade += (
                assignment.score * assignment.weight / 100
            )
            category_weight += assignment.weight

    if category_weight == 0:
        return 0

    return (category_grade / category_weight) * 100


def evaluate_student(student):
    assignments = student.assignments

    if not validate_scores(assignments):
        return

    if not validate_weights(assignments):
        return

    for assignment in assignments:
        assignment.classify_grade()

    total_grade, gpa = calculate_grade(assignments)

    formative = category_performance(assignments, "Formative")
    summative = category_performance(assignments, "Summative")

    if formative >= 50 and summative >= 50:
        decision = "PASSED"
    else:
        decision = "FAILED"

    failed_formative = []

    for assignment in assignments:
        if (assignment.group == "Formative" and
                assignment.score < 50):
            failed_formative.append(assignment)

    resubmissions = []

    if failed_formative:
        highest_weight = max(
            assignment.weight
            for assignment in failed_formative
        )

        for assignment in failed_formative:
            if assignment.weight == highest_weight:
                resubmissions.append(assignment)

    print("\n--- STUDENT ASSIGNMENT RESULTS ---")
    print(
        f"{'Assignment':40} {'Group':12} "
        f"{'Score':10} {'Weight':10} {'Status'}"
    )

    for assignment in assignments:
        print(
            f"{assignment.name:40} "
            f"{assignment.group:12} "
            f"{assignment.score:<10} "
            f"{assignment.weight:<10} "
            f"{assignment.status}"
        )

    print("\n--- FINAL RESULTS ---")
    print("Student:", student.name)
    print("Student Code:", student.student_code)
    print("Formative Performance:", round(formative, 2), "%")
    print("Summative Performance:", round(summative, 2), "%")
    print("Total Grade:", round(total_grade, 2), "%")
    print("GPA:", round(gpa, 2), "/ 5.0")
    print("Final Decision:", decision)

    print("\n--- RESUBMISSION OPTIONS ---")
    if resubmissions:
        for assignment in resubmissions:
            print(assignment.name, "- Weight:", assignment.weight)
    else:
        print("No failed Formative assignments.")

    student.save_results(
        total_grade,
        gpa,
        formative,
        summative,
        decision,
        resubmissions
    )


def main():
    print("=== STUDENT GRADE EVALUATION SYSTEM ===")

    student_code = input("Enter student code: ").strip()
    student_name = input("Enter student name: ").strip()

    student = Student(student_code, student_name)

    while True:
        try:
            number = int(input("Enter number of assignments: "))
            if number > 0:
                break
            print("Enter at least one assignment.")
        except ValueError:
            print("Enter a valid whole number.")

    for i in range(number):
        print(f"\n--- Assignment {i + 1} ---")

        name = input("Enter assignment name: ").strip()
        group = get_valid_group()
        score = get_valid_score()
        weight = get_valid_weight()

        assignment = Assignment(name, group, score, weight)
        student.add_assignment(assignment)

    evaluate_student(student)


if __name__ == "__main__":
    main()
