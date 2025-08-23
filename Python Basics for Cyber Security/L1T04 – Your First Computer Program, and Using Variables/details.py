"""
This script will request the user to enter their name, age,
house number and street name, then print the details in a
single sentence.
"""
# Request user to enter name
# save the input to a variable called 'user_name'
# request user to enter age
# save the input to a variable called 'user_age'
# request user to enter house number
# save the input to a variable called 'house_number'
# request user to enter street name
# save the input to a variable called 'street_name'
# print the user's name, age, house number and street name

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")    
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")
print(f"The user's name is: {user_name}, the user's age is: {user_age},\
    and the user's house number is: {house_number}, and the user's \
    street name is: {street_name}.")
