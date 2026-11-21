import csv

# Create and write student records
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Student ID", "Name", "Course"])
    writer.writerow(["2024010203", "Mark Joseph Barbosa", "BS Computer Engineering"])
    writer.writerow(["2024010204", "Joseph Estrada", "BS Computer Engineering"])
    writer.writerow(["2024010205", "Bong Revilla", "BS Computer Engineering"])
    writer.writerow(["2024010206", "Jinggoy Estrada", "BS Computer Engineering"])
    writer.writerow(["2024010207", "Zaldy Co", "BS Computer Engineering"])

print("CSV file created successfully!")

# Read and display records
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("\nStudent Records:")
    for row in reader:
        print(" | ".join(row))