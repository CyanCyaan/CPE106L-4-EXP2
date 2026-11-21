# Student Class

class Student:
    def __init__(self, student_id, name, course, grades):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = grades

    def compute_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "course": self.course,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["course"],
            data["grades"]
        )