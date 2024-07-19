import gspread
from google.oauth2.service_account import Credentials

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
    print("Program starting...\n")
    print("Hey there! Welcome to the Task Scheduler!\n")


def consultant_choice():
    """
    Display consultant list and get users choice
    """
    print("Choose your prefered consultant from the list\n")
    consultant = SHEET.worksheet('consultant')
    consultant_data = consultant.get_all_values()
    print(consultant_data)

    consultant_str = input("Select your consultant by First name:\n")
    user_input = input(f"You have chosen {consultant_str} is this correct? (Y/N)")
    if user_input.lower() == "y":
        print("Great!")
    else:
        consultant_str = input("Select your consultant by First name:\n")
        user_input = input(f"You have chosen {consultant_str} is this correct? (Y/N)")

start()
consultant_choice()
