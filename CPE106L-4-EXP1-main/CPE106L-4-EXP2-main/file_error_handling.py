try:
    with open("missing_file.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist!")