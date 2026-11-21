
# CPE106L Experiment 1 - POSTLAB
# Student Management System

# Fixed Course Information (Tuple)
COURSE_INFO = (
    "CPE106L-4",
    "Software Design Laboratory",
    "BSCpE"
)


# Parent Class
class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def display_info(self):
        print("Name:", self.__name)
        print("Email:", self.__email)


# Student Class
class Student(Person):
    def __init__(self, name, email, student_id, course, grades=None):
        super().__init__(name, email)
        self.__student_id = student_id
        self.__course = course
        self.__grades = grades if grades is not None else []

    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_grades(self):
        return self.__grades

    def set_grades(self, grades):
        self.__grades = grades

    def compute_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def display_info(self):
        print("\nStudent Information")
        print("Student ID:", self.__student_id)
        super().display_info()
        print("Course:", self.__course)
        print("Grades:", self.__grades)
        print(f"Average: {self.compute_average():.2f}")

# Instructor Class
class Instructor(Person):
    def __init__(self, name, email, instructor_id, department):
        super().__init__(name, email)
        self.__instructor_id = instructor_id
        self.__department = department

    def display_info(self):
        print("\nInstructor Information")
        print("Instructor ID:", self.__instructor_id)
        super().display_info()
        print("Department:", self.__department)


# Dictionary for Student Records
students = {}

# Instructor Object
instructor = Instructor(
    "Dr. Maria Reyes",
    "maria@example.com",
    "INS-001",
    "Computer Engineering"
)


# Polymorphism Helper
def display_person(person):
    person.display_info()


# Add Student
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    course = input("Enter Course: ")

    grades_input = input("Enter Grades (comma-separated): ")

    try:
        grades = [
            float(grade.strip())
            for grade in grades_input.split(",")
            if grade.strip()
        ]
    except ValueError:
        print("Invalid grade. Please enter numbers only.")
        return

    student = Student(name, email, student_id, course, grades)

    students[student_id] = student

    print("\nStudent added successfully!")


# Display Student Records
def display_students():
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students.values():
        student.display_info()


# Search Student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        students[student_id].display_info()
    else:
        print("Student not found!")


# Update Student
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\n1. Update Name")
    print("2. Update Email")
    print("3. Update Course")
    print("4. Update Grades")

    choice = input("Choose what to update: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        student.set_name(new_name)

    elif choice == "2":
        new_email = input("Enter new email: ")
        student.set_email(new_email)

    elif choice == "3":
        new_course = input("Enter new course: ")
        student.set_course(new_course)

    elif choice == "4":
        try:
            grades = [
                float(g.strip())
                for g in input("Enter new grades: ").split(",")
                if g.strip()
            ]
            student.set_grades(grades)
        except ValueError:
            print("Invalid grades!")
            return

    else:
        print("Invalid choice!")
        return

    print("Student record updated successfully!")


# Delete Student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Compute Average Grade
def compute_student_average():
    print("\n--- Compute Average Grade ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        student = students[student_id]
        average = student.compute_average()

        print("Student Name:", student.get_name())
        print(f"Average Grade: {average:.2f}")
    else:
        print("Student not found!")


# Display Course Information
def display_course_information():
    print("\n--- Course Information ---")

    print("Course Code:", COURSE_INFO[0])
    print("Course Name:", COURSE_INFO[1])
    print("Program:", COURSE_INFO[2])


# Main Program Menu
if __name__ == "__main__":

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. Display Student Records")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Compute Average Grade")
        print("7. Display Course Information")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            compute_student_average()

        elif choice == "7":
            display_course_information()

        elif choice == "8":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")
