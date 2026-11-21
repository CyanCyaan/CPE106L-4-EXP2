
# Student Management System
# Activity 3 - Object-Oriented Programming

# Parent Class with Encapsulation
class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    # Getter methods
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print("Name:", self.__name)
        print("Email:", self.__email)


# Student Class
class Student(Person):
    def __init__(self, name, email, student_id, course):
        super().__init__(name, email)
        self.__student_id = student_id
        self.__course = course

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    # Setter method
    def set_course(self, course):
        self.__course = course

    def display_info(self):
        print("\nStudent Information")
        print("Student ID:", self.__student_id)
        super().display_info()
        print("Course:", self.__course)

    def update_record(self, course):
        self.__course = course
        print("\nStudent record updated!")


# Instructor Class (inherits from Person)
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


# Create Student Object
student1 = Student(
    "Maria Maroa",
    "maria@example.com",
    "2024010203",
    "BSCpE"
)

# Display Student Information
student1.display_info()

# Update Student Record
student1.update_record("BS Computer Engineering")

# Display Updated Information
student1.display_info()

# Encapsulation Test
print("\n--- Encapsulation Example ---")

print("Student Name:", student1.get_name())
print("Student Course:", student1.get_course())

student1.set_course("Computer Engineering")

print("Updated Course:", student1.get_course())


# Inheritance Test
print("\n--- Inheritance Example ---")

instructor1 = Instructor(
    "Dr. Maria Reyes",
    "maria@example.com",
    "INS-001",
    "Computer Engineering"
)

instructor1.display_info()


# Polymorphism Test
print("\n--- Polymorphism Example ---")

# Store different objects in one list
people = [student1, instructor1]

# Call the same method for different objects
for person in people:
    person.display_info()
