"""Read data from text file and display to user"""

full_names = []
date_of_births = []
try:
    with open('DOB.txt', 'r', encoding='utf-8') as file:
        lines_list = file.readlines()
        for line in lines_list:
            # Append names and birthdates into separate lists
            full_names.append(line.split()[0:2])
            date_of_births.append(line.split()[2:5])
except FileNotFoundError:
    print("Error:Ensure you are in the correct directory in your terminal")


print("Name")
# Iterate list and display each name
for name in full_names:
    print(" ".join(name))

print("\nBirthdate")
# Iterate array and display each date of birth
for birthday in date_of_births:
    print(" ".join(birthday))
