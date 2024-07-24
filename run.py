import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import re

prog_start = """

  _____                                        _____ _             _   _                   
 |  __ \                                      / ____| |           | | (_)                  
 | |__) | __ ___   __ _ _ __ __ _ _ __ ___   | (___ | |_ __ _ _ __| |_ _ _ __   __ _       
 |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \   \___ \| __/ _` | '__| __| | '_ \ / _` |      
 | |   | | | (_) | (_| | | | (_| | | | | | |  ____) | || (_| | |  | |_| | | | | (_| |_ _ _ 
 |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_| |_____/ \__\__,_|_|   \__|_|_| |_|\__, (_|_|_)
                   __/ |                                                        __/ |      
                  |___/                                                        |___/       
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


def start():
    """
    Program start and welcome message
    """
    print(prog_start)
    print("Hey there! Welcome to the Task Scheduler!\n")

def consultant_list():
    """
    Display consultant list
    """
    print("Choose your prefered consultant from the list\n")
    consultant = SHEET.worksheet("consultant")
    consultant_data = consultant.get_all_values()
    print(consultant_data)

def consultant_choice():
    """
    User input to choose consultant from a fixed list
    """
    consultant_names = ["Johnny Bravo", "Homer Simpson", "Ned Flanders", "Peter Griffins", "Fred Flinstone"]

    user_inputs = []

    while True:
        user_input = input(f"Select your consultant by their full name: ")
    
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
        
        if re.match("^[a-zA-Z\s\.,'\"-]+$", project_name_input):
            print(f"{project_name_input} accepted")
            return project_name_input
        else:
            print("Project name must contain text only")

def task_input():
    """
    User input for number of tasks within a project & naming tasks
    """
    print("Please input the number of tasks for your project")
    print("Number of tasks should be a number between 1 and 10")
    
    try:
        number_of_tasks = int(input("Enter the number of tasks required for your project:\n"))
        if number_of_tasks < 1 or number_of_tasks > 10:
            print("Number of tasks should be a number between 1 and 10")
        else:
            print(f"You have entered {number_of_tasks} task(s)")
            return number_of_tasks
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
            if not re.match("^[a-zA-Z\s\.,'\"-]+$", description):
                print("Description must contain text only")

            date_of_task = input(f"Enter date for the task {i + 1} (YYYY-MM-DD):\n")
            try:
                datetime.strptime(date_of_task, "%Y-%m-%d")
            except ValueError:
                print("Please enter a valid date in the format YYYY-MM-DD.")
                continue

            task_descriptions.append({'description': description, 'date_of_task' : date_of_task})
            break

    return task_descriptions

if __name__ == "__main__":
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

def update_worksheet(project_data):
    print("Updating worksheet...\n")
    projects_worksheet = SHEET.worksheet("projects")
    projects_worksheet.append_row(project_data)
    print("Worksheet updated successfully!\n")

update_worksheet(project_data)

#start()
#consultant_list()
#consultant_choice()
#project_name()

#task_input()
#number_of_tasks = task_input()
#task_descriptions = get_task_information(number_of_tasks)







