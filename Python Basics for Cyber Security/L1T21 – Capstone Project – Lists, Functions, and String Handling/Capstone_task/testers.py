def get_valid_str(user_input_mess):
    """Ensures input consists of alphanumeric characters"""
    while True:
        user_input = input(f"{user_input_mess}: ")
        if user_input == "":
            print("Please enter valid data. No empty spaces")
            continue
        return user_input

# input2 = input("Enter name")
get_valid_str("Enter your name")
            
# while True:
#     input2 = input("Enter name")
#     if get_valid_str(input2):
#         break


