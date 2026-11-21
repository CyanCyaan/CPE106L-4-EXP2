import json

# Student records
students = [
    {
        "Student ID": "2024010203",
        "Name": "Mark Joseph Barbosa",
        "Course": "BS Computer Engineering"
    },
    {
        "Student ID": "2024010204",
        "Name": "Joseph Estrada",
        "Course": "BS Computer Engineering"
    },
    {
        "Student ID": "2024010205",
        "Name": "Bong Revilla",
        "Course": "BS Computer Engineering"
    },
    {
        "Student ID": "2024010206",
        "Name": "Jinggoy Estrada",
        "Course": "BS Computer Engineering"
    },
    {
        "Student ID": "2024010207",
        "Name": "Zaldy Co",
        "Course": "BS Computer Engineering"
    }
]

# Create and write JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully!")

# Read the JSON file
with open("students.json", "r") as file:
    data = json.load(file)

# Display student records
print("\nStudent Records:")
for student in data:
    print("\nStudent ID:", student["Student ID"])
    print("Name:", student["Name"])
    print("Course:", student["Course"])