import gspread
from google.oauth2.service_account import Credentials
import datetime

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
            break
            return({user_input})
        else:
            print(f"Invalid input. Please enter a name from the list.")
            break

def project_name():
    """
    User input to enter name of their project
    """
    while True:
        project_name_input = input("Enter your project name (50 characters max):\n")
        if len(project_name_input) <= 50:
            print(f"{project_name_input} accepted")
            break
        else:
            print("Project name must be 50 characters or less.")


def task_date():
    """
    User input for date
    """
    while True:
        date_input = input("Enter a date (YYYY-MM-DD):\n")
        try:
            valid_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            print(f"Date {date_input} is valid.")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

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
    except ValueError:
        print("Please enter a valid number.")


#start()
#consultant_list()
#consultant_choice()
#project_name()
#task_date()
task_input()


