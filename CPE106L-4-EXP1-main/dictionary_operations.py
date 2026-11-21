
# Dictionary Operations Program

# Create student dictionary
student = {
    "StudentID": "20230001",
    "Name": "Juan Dela Cruz",
    "Course": "BSCpE"
}

# Display original dictionary
print("Original Student Information:", student)

# Add a new key-value pair
student["Year"] = "1st Year"
print("\nAfter adding Year:", student)

# Update existing data
student["Course"] = "BS Computer Engineering"
print("\nAfter updating Course:", student)

# Retrieve information
print("\nStudent Name:", student["Name"])
print("Student ID:", student["StudentID"])
print("Course:", student["Course"])

# Delete an item
del student["Year"]
print("\nAfter deleting Year:", student)
