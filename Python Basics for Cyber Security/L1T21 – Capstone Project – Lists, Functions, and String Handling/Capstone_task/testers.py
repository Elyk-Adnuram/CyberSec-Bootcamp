def get_valid_str(user_input_mess):
    """Ensures input consists of alphanumeric characters"""
    while True:
        user_input = input(f"{user_input_mess}: ")
        if user_input == "":
            print("Please enter valid data. No empty spaces")
            continue
        return user_input


def get_valid_date_str(date_input_message: str = "Enter due date of task in this format (YYYY-MM-DD): "):
    """Ensure string is entered in this format YYYY-MM-DD"""
    while True:
        try:
            task_due_date = input(date_input_message: ).strip()
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break
        except ValueError:
             print("""Invalid datetime format. Please use the format
specified""")
             


   