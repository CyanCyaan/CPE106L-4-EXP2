import json
from student import Student

FILE_NAME = "students.json"

def load_students():
    students = {}

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:
            student = Student.from_dict(item)
            students[student.student_id] = student

    except FileNotFoundError:
        print("No saved records found. Starting new file.")

    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty records.")

    return students


def save_students(students):
    try:
        data = [student.to_dict() for student in students.values()]

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Records saved successfully!")

    except (OSError, TypeError) as error:
        print("Error saving records:", error)