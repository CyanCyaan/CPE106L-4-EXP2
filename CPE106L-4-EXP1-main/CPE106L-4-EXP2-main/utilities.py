# Average Calculator
def calculate_average(grades):
    return sum(grades) / len(grades)

# Grade Evaluator
def evaluate_grade(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

# Student Information
def display_student(name, student_id, course):
    print("\nStudent Information")
    print("Name:", name)
    print("Student ID:", student_id)
    print("Course:", course)

def get_grades():
    while True:
        try:
            grades = input("Enter grades separated by commas: ")
            return [float(g.strip()) for g in grades.split(",")]
        except ValueError:
            print("Invalid grades. Please enter numbers only!")