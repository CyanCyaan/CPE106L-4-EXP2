try:
    grade = float(input("Enter your grade: "))

    print("Your grade is:", grade)

except ValueError:
    print("Invalid input! Please enter numbers only.")