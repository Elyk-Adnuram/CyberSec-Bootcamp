"""Obtain user input and write data to a text file"""

# Get user input
num_of_students = int(input("Advise how many students are registering: "))
student_id_list = []
# Iterate number of students and append id's to list
for i in range(num_of_students):
    student_id = input("Please enter student ID number: ")
    student_id_list.append(student_id)
    # Open and write to text file
    with open('reg_form.txt', 'a+', encoding='utf-8') as file:
        # Iterate list and write data to file 
        for index, id_num in enumerate(student_id_list):
            file.write(f"{index+1}. {id_num} ............\n")
