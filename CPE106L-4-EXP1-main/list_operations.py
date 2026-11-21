
# List Operations Program

# Create an empty list for grades
grades = []

# Accept five grades
for i in range(5):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

# Calculate average
average = sum(grades) / len(grades)

# Display results
print("\nGrades:", grades)
print("Average:", average)
print("Highest grade:", max(grades))
print("Lowest grade:", min(grades))

# Sort grades in ascending order
grades.sort()
print("Sorted grades:", grades)
