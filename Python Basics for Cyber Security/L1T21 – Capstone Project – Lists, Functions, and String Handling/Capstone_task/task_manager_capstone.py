"""
Task Manager program
Enables user to manage tasks assigned to them and other users
Functionality includes:
- Registering a user (admin only)
- Adding a task
- View all tasks
- View my tasks
- Generate reports (admin only)
- Display statistics (admin only)
"""

# Import of libraries
import os
from datetime import datetime
import uuid  # generate a random ID


# Global constant variables
DATETIME_STRING_FORMAT = "%Y-%m-%d"
CURRENT_DATE = datetime.today()
USERNAME_PASSWORD = {}
TASK_LIST = []
CURRENT_USER = ""


def create_tasks():
    """Create tasks.txt file if it doesn't exist and load tasks into TASK_LIST"""   

    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w", encoding="utf-8") as default_file:
            pass

    with open("tasks.txt", 'r', encoding="utf-8") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [task for task in task_data if task != ""]

    for task in task_data:
        current_task = {}

        # Split by semicolon and manually add each component
        task_components = task.split(";")
        current_task['task_id'] = task_components[0]
        current_task['username'] = task_components[1]
        current_task['title'] = task_components[2]
        current_task['description'] = task_components[3]
        current_task['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        current_task['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        current_task['completed'] = task_components[6] == "Yes"
        
        TASK_LIST.append(current_task)


#====Login Section====
# This code reads usernames and password from the user.txt file to
# allow a user to login.

def login():
    """Handles user login"""
    global CURRENT_USER
    # If no user.txt file, write one with a default account
    if not os.path.exists("user.txt"):
        with open("user.txt", "w", encoding="utf-8") as default_file:
            default_file.write("admin;password")

    # Read in user_data
    with open("user.txt", 'r', encoding="utf-8") as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary

    for user in user_data:
        username, password = user.split(';')
        USERNAME_PASSWORD[username] = password

    while True:
        print("LOGIN")
        CURRENT_USER = input("Username: ")
        current_pass = input("Password: ")
        if CURRENT_USER not in USERNAME_PASSWORD:
            print("User does not exist")
            continue
        if USERNAME_PASSWORD[CURRENT_USER] != current_pass:
            print("Wrong password")
            continue
        print("Login Successful!")
        break


# Helper functions
def get_valid_str(user_input_mess: str = "Enter valid data"):
    """Ensures input is not an empty string"""
    while True:
        user_input = input(f"{user_input_mess}: ").strip().lower()
        if user_input == "":
            print("Please enter valid data. No empty spaces")
            continue
        return user_input


def get_valid_date_str(date_input_message: str = "Enter date in this format (YYYY-MM-DD): "):
    """
    Ensure string is entered in correct format
    Args: date_input_message (str): The message that will be displayed to user
    Returns: None
    """
    while True:
        due_date = input(f"{date_input_message}: ").strip()
        try:
            task_due_date = datetime.strptime(due_date, DATETIME_STRING_FORMAT)
            return task_due_date
        except ValueError:
            print("""Invalid datetime format. Please use the format
specified""")


def append_task(display_message: str = "Task successfully added"):
    """
    Add a task to the TASK_LIST list
    Args: display_message (str): The message displayed to the user
    Returns: None
    """
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        TASK_LIST_to_write = []
        for task in TASK_LIST:
            str_attrs = [
                task['task_id'],
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DATETIME_STRING_FORMAT),
                task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task['completed'] else "No"
            ]
            TASK_LIST_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(TASK_LIST_to_write))
    print(display_message)


# Functionality section
def reg_user():
    '''
    Register a user in the application and prevent username duplication
    Args: None
    Returns: None
    '''
    # Request details of new user
    while True:
        new_username = get_valid_str("New Username: ")
        new_password = get_valid_str("New Password: ")
        confirm_password = get_valid_str("Confirm Password: ")   
        if new_username in USERNAME_PASSWORD:
            print("Username already exists. Please enter a different username")    
        else:
            while True:
                # Check that new password and confirmed password are the same.
                if new_password == confirm_password:
                    # If they are the same, add them to the user.txt file,
                    print("New user added successfully")
                    USERNAME_PASSWORD[new_username] = new_password

                    with open("user.txt", "w", encoding="utf-8") as out_file:
                        user_data = []
                        for username, password in USERNAME_PASSWORD.items():
                            user_data.append(f"{username};{password}")
                        out_file.write("\n".join(user_data))
                        return
                # Otherwise you present a relevant message.
                else:
                    print("Passwords do no match. Re-enter password")
                    confirm_password = get_valid_str("Confirm Password: ") 


def add_task():
    """
    Prompt a user for task details
    Args: None
    Returns: None
    """
    while True:
        # Check if user exists
        task_username = get_valid_str("Name of person assigned to task: ")
        if task_username not in USERNAME_PASSWORD:
            print("User does not exist. Please enter a valid username")
        else:
            task_title = get_valid_str("Title of Task: ")
            task_description = get_valid_str("Description of Task: ")
            # ensure due date is formatted correctly
            task_due_date = get_valid_date_str()

            # Add the data to the file task.txt and
            # Include 'No' to indicate if the task is complete.
            new_task = {
                "task_id": uuid.uuid4().hex[:3],
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": task_due_date,
                "assigned_date": CURRENT_DATE,
                "completed": False,
            }
            TASK_LIST.append(new_task)
            append_task()
            break


def view_all():
    """
    Display all tasks
    Args: None
    Returns: None"""
    for task in TASK_LIST:
        display = (
            f"Task ID: \t\t {task['task_id']}\n"
            f"Task Title: \t\t {task['title']}\n"
            f"Assigned to: \t {task['username']}\n"
            f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Task Description: \n {task['description']}\n"
        )
        print(display)


def display_curr_user_tasks():
    """
    Display the tasks of the logged in user
    Args: None
    Returns: None
    """ 
    print(f"\n These are {CURRENT_USER}'s tasks:")  
    for task in TASK_LIST:        
        if task['username'] == CURRENT_USER:
            display = (
                f"Task ID: \t{task['task_id']}\n"
                f"Task Title: \t{task['title']}\n"
                f"Assigned to: \t{task['username']}\n"
                f"Date Assigned: \t{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Due Date: \t{task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Task Description: \n{task['description']}\n"
                f"Task Completed: \t{'Yes' if task['completed'] else 'No'}\n"
            )
            print(display)


def view_mine():
    """Display tasks of current user and enable editing of a task"""
    display_curr_user_tasks()
    select_task = get_valid_str("""Select task to edit by entering the Task ID or -1 to return to main menu: """)
    if select_task == "-1":
        return
    elif len(select_task) != 3:
        print("Task ID not found. Please try again")
        return
    else:
        for task in TASK_LIST:
            if task['username'] == CURRENT_USER and task['task_id'] == select_task:
                mark_complete = get_valid_str("Enter 'yes' to mark task complete or 'no' to leave task as incomplete")
                if mark_complete == 'no':
                    edit_task = get_valid_str("Enter 'yes' to edit task or 'no' to return to main menu")
                    if edit_task == "no":
                        return
                    # update the due_date and username properties 
                    elif edit_task == "yes":
                        updated_username = get_valid_str("Enter a new username for task")
                        updated_due_date = get_valid_date_str("Enter a new due date for task")
                        task["due_date"] = updated_due_date
                        task["username"] = updated_username
                        append_task("Task has been updated")
                # update the completed property to True 
                elif mark_complete == 'yes':
                    task["completed"] = True
                    append_task("Task has been marked as complete")
                return
        

def generate_task_overview():
    """
    Generate two text files: task_overview.txt
    Args: None
    Returns: none
    """
    total_tasks = len(TASK_LIST)
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    total_uncompleted_overdue_tasks = 0
    percent_tasks_incomplete = 0
    percent_tasks_overdue = 0 
    # iterate TASK_LIST to obtain below values   
    for tasks in TASK_LIST:
        if tasks['completed']:
            total_completed_tasks += 1
        elif not tasks['completed']:
            total_uncompleted_tasks += 1
            if tasks['due_date'] < CURRENT_DATE:
                total_uncompleted_overdue_tasks += 1
    if total_tasks > 0:
        percent_tasks_incomplete = (total_uncompleted_tasks / total_tasks) * 100
        percent_tasks_overdue = (total_uncompleted_overdue_tasks / total_tasks) * 100 
       
    with open("task_overview.txt", "w", encoding="utf-8") as task_over_file:
        task_over_file.write(f"Total number of tasks: {total_tasks}\n")
        task_over_file.write(f"""Total number of completed tasks:
{total_completed_tasks}\n""")
        task_over_file.write(f"""Total number of uncompleted tasks: 
{total_uncompleted_tasks}\n""")
        task_over_file.write(f"""Total number of overdue tasks: 
{total_uncompleted_overdue_tasks}\n""")
        task_over_file.write(f"""Percentage of tasks incomplete:
{percent_tasks_incomplete:.2f}%\n""")
        task_over_file.write(f"""Percentage of tasks overdue:
{percent_tasks_overdue:.2f}%\n""")    


def generate_user_overview():
    """
    Generate user_overview.txt file
    Args: None
    Returns: None
    """
    total_registered_users = len(USERNAME_PASSWORD)
    total_tasks = len(TASK_LIST)

    for tasks in TASK_LIST:
        assigned_tasks_per_user = 0
        percent_assigned_tasks_per_user = 0
        completed_tasks_per_user = 0
        percent_completed_tasks_per_user = 0
        uncompleted_overdue_tasks_per_user = 0
        percent_uncompleted_overdue_tasks_per_user = 0
        for user in USERNAME_PASSWORD.keys():
            if tasks['username'] == user:
                assigned_tasks_per_user += 1
                if total_tasks > 0:
                    percent_assigned_tasks_per_user = (assigned_tasks_per_user / total_tasks) * 100
                if tasks['completed']:
                    completed_tasks_per_user += 1
                    if assigned_tasks_per_user > 0:
                        percent_completed_tasks_per_user =\
(completed_tasks_per_user / assigned_tasks_per_user) * 100
                elif not tasks['completed'] and tasks['due_date'] < CURRENT_DATE:
                    uncompleted_overdue_tasks_per_user += 1
                    if assigned_tasks_per_user > 0:
                        percent_uncompleted_overdue_tasks_per_user = \
(uncompleted_overdue_tasks_per_user / assigned_tasks_per_user) * 100   
        with open("user_overview.txt", "a", encoding="utf-8") as user_over_file:
            user_over_file.write(f"User: {user}\n")
            user_over_file.write(f"""Total number of tasks assigned: {assigned_tasks_per_user}\n""")
            user_over_file.write(f"""Percentage of total tasks assigned: {percent_assigned_tasks_per_user:.2f}%\n""")
            user_over_file.write(f"""Percentage of tasks completed: {percent_completed_tasks_per_user:.2f}%\n""")
            user_over_file.write(f"""Percentage of tasks overdue: {percent_uncompleted_overdue_tasks_per_user:.2f}%\n\n""") 


def display_statistics():
    """Display statistics from task_overview.txt and user_overview.txt files"""
    # Check if report files exist, if not generate them
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        print("Reports have not been generated yet. Generating now...")
        generate_task_overview()
        generate_user_overview()
        print("Reports have been generated")
    # Display task_overview.txt file
    print("\nTask Overview\n")
    with open("task_overview.txt", "r", encoding="utf-8") as task_over_file:
        for line in task_over_file:
            print(line.strip())
    # Display user_overview.txt file
    print("\nUser Overview\n")
    with open("user_overview.txt", "r", encoding="utf-8") as user_over_file:
        for line in user_over_file:
            print(line.strip())


def main():
    """Main function to run the task manager program"""
    create_tasks()
    login()
    while True:
        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.
        # Display different menu options if the user is an admin
        if CURRENT_USER == 'admin':
            menu = input("Select one of the following Options below:\n"
                        "r - Registering a user\n"
                        "a - Adding a task\n"
                        "va - View all tasks\n"
                        "vm - View my task\n"
                        "gr - Generate reports\n"
                        "ds - Display statistics\n"
                        "e - Exit\n"
                        ": ").lower()
        else:
            menu = input("Select one of the following Options below:\n"
                        "a - Adding a task\n"
                        "va - View all tasks\n"
                        "vm - View my task\n"
                        "e - Exit\n"
                        ": ").lower()

        if menu == 'r':
            reg_user() 
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()        
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr':
            generate_task_overview()
            generate_user_overview()
        elif menu == 'ds' and CURRENT_USER == 'admin':
            display_statistics()
        elif menu == 'e':
            print('Goodbye!!!')
        else:
            print("You have made a wrong choice, Please Try again")


if __name__ == "__main__":
    main()
