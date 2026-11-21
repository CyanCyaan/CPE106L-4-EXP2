# Text File Operations

# Create and write to the file
with open("students.txt", "w") as file:
    file.write("Student ID: 2024740301\n")
    file.write("Name: Mark Joseph Barbosa\n")
    file.write("Course: BS Computer Engineering\n")

print("File created and data written successfully!")

# Read the file
with open("students.txt", "r") as file:
    print("\nStudent Records:")
    print(file.read())

# Append another record
with open("students.txt", "a") as file:
    file.write("\nStudent ID: 2020102030\n")
    file.write("Name: Abraham Lincoln\n")
    file.write("Course: BS Computer Engineering\n")

print("New student record added!")

# Display updated contents
with open("students.txt", "r") as file:
    print("\nUpdated Student Records:")
    print(file.read())