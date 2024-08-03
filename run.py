import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import re
import os

prog_start = r"""
 _    _      _                          _ 
| |  | |    | |                        | |
| |  | | ___| | ___ ___  _ __ ___   ___| |
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
\  /\  /  __/ | (_| (_) | | | | | |  __/_|
 \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task_scheduler')

def main_menu():
    """
    Main menu options for users to select
    """
    while True:
        print(prog_start)
        print('Main Menu:\n')
        print('1. Instructions\n')
        print('2. Start a new project\n')
        print('3. View consultant list\n')
        print('4. View project list\n')
        print('5. Exit\n')

        choice = input('Choose an option (1-4):\n')

        if choice == '1':
            instructions()
        elif choice == '2':
            start_new_project()
        elif choice == '3':
            consultant_list()
        elif choice == '4':
            project_list()
        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please select a valid option')

def instructions():
    print('Thank you for using task scheduler, I am here to help you schedule your projects. Please follow these steps.\n')
    print('1. Choose your preferred consultant.\n')
    print('2. Enter the name of the project you are working on.\n')
    print('3. Enter the number of tasks (between 1 - 10) within your project.\n')
    print('4. Enter task descriptions.\n')
    print('5. Enter task dates.\n')

def project_list():
    """
    Display project list
    """
    projects = SHEET.worksheet("projects")
    project_data = projects.get_all_values()

    for row in project_data:
        print("-".join(row))

def consultant_list():
    """
    Display consultant list
    """
    print("Choose your prefered consultant from the list\n")
    consultant = SHEET.worksheet("consultant")
    consultant_data = consultant.get_all_values()

    for row in consultant_data:
        print("-".join(row))

def consultant_choice():
    """
    User input to choose consultant from a fixed list
    """
    consultant_names = ["JOHNNY BRAVO", "HOMER SIMPSON", "NED FLANDERS", "PETER GRIFFINS", "FRED FLINTSTONE"]

    user_inputs = []

    while True:
        user_input = input(f"Select your consultant by their full name:\n").upper()
    
        if user_input in consultant_names:
            user_inputs.append(user_input)
            print(f"Great! You have chosen {user_input}")
            return user_input
        else:
            print(f"Invalid input. Please enter a name from the list.")

def project_name():
    """
    User input to enter name of their project
    """
    while True:
        project_name_input = input("Enter your project name (50 characters max):\n")
        if len(project_name_input) > 50:
            print("Project name must be 50 characters or less.")
            continue
        
        if re.match(r"^[a-zA-Z\s\.,'\"-]+$", project_name_input):
            print(f"{project_name_input} accepted")
            return project_name_input
        else:
            print("Project name must contain text only")

# Does not print number of entered tasks
def task_input():
    """
    User input for number of tasks within a project & naming tasks
    """
    print("Please input the number of tasks for your project")
    print("Number of tasks should be a number between 1 and 10")
    
    while True:
        try:
            number_of_tasks = int(input("Enter the number of tasks required for your project:\n"))
            if number_of_tasks > 1 or number_of_tasks < 10:
                print(f"You have entered {number_of_tasks} task(s)")
                return number_of_tasks
            else:
                print("Number of tasks should be a number between 1 and 10")
        except ValueError:
            print("Please enter a valid number.")

def get_task_information(number_of_tasks):
    """
    User input to add descriptions for the number of tasks chosen
    """
    task_descriptions = []
    for i in range(number_of_tasks):
        while True:
            description = input(f"Enter description for task {i + 1}:\n")

            if len(description) > 100:
                print("Description must be 100 characters or less")
                continue
            if not re.match(r"^[a-zA-Z\s\.,'\"-]+$", description):
                print("Description must contain text only")
                continue

            date_of_task = input(f"Enter date for the task {i + 1} (YYYY-MM-DD):\n")
            try:
                datetime.strptime(date_of_task, "%Y-%m-%d")
            except ValueError:
                print("Please enter a valid date in the format YYYY-MM-DD.")
                continue

            task_descriptions.append({'description': description, 'date_of_task' : date_of_task})
            break

    return task_descriptions

def update_worksheet(project_data):
    """
    Upload data to projects worksheet
    """
    print("Updating worksheet...\n")
    projects_worksheet = SHEET.worksheet("projects")

    for task in project_data['tasks']:
        row = [
            project_data['consultant'],
            project_data['project_name'],
            task['date_of_task'],
            task['description']
        ]
        projects_worksheet.append_row(row)

    print("Worksheet updated successfully!\n")

def start_new_project():
    consultant_list()
    consultant = consultant_choice()
    project = project_name()
    number_of_tasks = task_input()
    tasks = get_task_information(number_of_tasks)
    
    project_data = {
        'consultant': consultant,
        'project_name': project,
        'number_of_tasks': number_of_tasks,
        'tasks': tasks
    }

    print("Project Data:", project_data)
    update_worksheet(project_data)

if __name__ == "__main__":
    main_menu()





