
# String Manipulation Program

# Accept user's full name
full_name = input("Enter your full name: ")

# Convert name to uppercase and lowercase
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())

# Count total characters (including spaces)
print("Total characters:", len(full_name))

# Display initials
initials = "".join(name[0].upper() for name in full_name.split())
print("Initials:", initials)
