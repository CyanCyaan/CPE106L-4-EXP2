"""
import utilities

name = "Mark Joseph Barbosa"
student_id = "2024010203"
course = "BS Computer Engineering"

grades = [90, 85, 88]

utilities.display_student(name, student_id, course)

average = utilities.calculate_average(grades)

print("Grades:", grades)
print("Average:", round(average, 2))
print("Result:", utilities.evaluate_grade(average))
"""
from student import Student
from file_manager import load_students, save_students
from utilities import get_grades

students = load_students()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display Student Records")
    print("6. Save Records")
    print("7. Generate Summary Report")
    print("8. Exit")

    try:
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Student ID: ")

            if student_id in students:
                print("Student ID already exists!")
                continue

            name = input("Name: ")
            course = input("Course: ")
            grades = get_grades()

            students[student_id] = Student(
                student_id, name, course, grades
            )
            print("Student added successfully!")

        elif choice == "2":
            student_id = input("Enter Student ID: ")

            if student_id in students:
                student = students[student_id]
                student.name = input("New name: ")
                student.course = input("New course: ")
                student.grades = get_grades()
                print("Student updated successfully!")
            else:
                print("Student not found!")

        elif choice == "3":
            student_id = input("Enter Student ID: ")

            if student_id in students:
                del students[student_id]
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        elif choice == "4":
            student_id = input("Enter Student ID: ")

            if student_id in students:
                student = students[student_id]
                print("Name:", student.name)
                print("Course:", student.course)
                print("Grades:", student.grades)
                print("Average:", round(student.compute_average(), 2))
            else:
                print("Student not found!")

        elif choice == "5":
            for student in students.values():
                print("\nStudent ID:", student.student_id)
                print("Name:", student.name)
                print("Course:", student.course)
                print("Grades:", student.grades)
                print("Average:", round(student.compute_average(), 2))

        elif choice == "6":
            save_students(students)

        elif choice == "7":
            print("\nSUMMARY REPORT")
            print("Total Students:", len(students))

            for student in students.values():
                print(student.name, "-", round(student.compute_average(), 2))

        elif choice == "8":
            save_students(students)
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

    except (ValueError, KeyError) as error:
        print("Invalid input:", error)

    except Exception as error:
        print("An error occurred:", error)