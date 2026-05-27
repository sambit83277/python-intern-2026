# Taking student information as input
name = input("Enter student name: ")
branch = input("Enter branch: ")
cgpa = input("Enter CGPA: ")

# Printing the formatted report using f-strings
print("\n--- Student Information Report ---")
print(f"Name:   {name}")
print(f"Branch: {branch}")
print(f"CGPA:   {cgpa}")
print("----------------------------------")