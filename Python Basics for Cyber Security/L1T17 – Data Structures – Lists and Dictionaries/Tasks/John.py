"""Request user input until a specified string has been entered"""

specified_string = "john"
names_list = []
# Request user input until conditional statement is met
while True:
    user_input = input("Please enter a name: ").lower()
    if user_input != specified_string:
        names_list.append(user_input)
    else:
        break
# Display incorrect names
print(f"Incorrect names: {names_list}")
