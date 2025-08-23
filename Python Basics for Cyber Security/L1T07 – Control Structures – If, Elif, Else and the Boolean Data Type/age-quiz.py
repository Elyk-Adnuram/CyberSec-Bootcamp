"""Module to quiz the user on their age."""

# Request user age and save it in age variable
age = int(input("Please enter your age: "))

# Use if/elif/else structure to control flow of program
if age > 100:
    print("Sorry, you're dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st")
elif age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")
