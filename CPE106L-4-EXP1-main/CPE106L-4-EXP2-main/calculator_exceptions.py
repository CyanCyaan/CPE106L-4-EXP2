try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operator!")

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

except Exception as e:
    print("An unexpected error occurred:", e)