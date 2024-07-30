# Task Scheduler
An application for scheduling project activities created as part of project submission to Code Institute for the Diploma in Full Stack Software Development (E-commerce applications).

The application can be viewed on the Code Institute mock terminal on [Heroku](https://task-scheduler-v1-ff610b0f7ba4.herokuapp.com/)

## Contents
- [User Experience](#user-experience)
    - [Initial Discussion](#initial-discussion)
    - [User Stories](#user-stories)
        - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Returning Visitor Goals](#returning-visitor-goals)
        - [Frequent Visitor Goals](#frequent-visitor-goals)
    - [Design](#design)
        - [Flow Chart](#flow-chart)
- [Features](#features)
- [Technologies Used](#technologies-used)
    - [Languagues](#languages)
    - [Frameworks](#frameworks)
- [Testing](#testing)
    - [PEP8 Python Validator](#pep8-python-validator)
        - [Python](#python)
    - [Manual](#manual)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
        - [First Time Visitor Goals](#first-time-visitor-goals-1)
        - [Returning Visitor Goals](#returning-visitor-goals-1)
        - [Frequent Visitor Goals](#frequent-visitor-goals-1)
    - [Bugs](#bugs)
      - [Known](#known)
      - [Fixed](#fixed)
- [Deployment & Local Development](#deployment-local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
- [Credits](#credits)
    - [Code Used](#code-used)
    - [Resources](#resources)
    - [Acknowledgments](#acknowledgments)


## User Experience
### Initial Discussion
text
### User Stories
#### First Time Visitor Goals
text

#### Returning Visitor Goals
text

#### Frequent Visitor Goals
text

### Design
text

#### Flow Chart
text

#### ASCII Art
text

## Features
text

## Technologies Used
### Languages
- Python
### Frameworks
text

## Testing
### PEP8 Python Validator
#### Python
test

### Manual
text

### Testing User Stories from User Experience (UX) Section
#### First Time Visitor Goals
text

#### Returning Visitor Goals
text

#### Frequent Visitor Goals
text

### Bugs
#### Known
text

#### Fixed
text

## Deployment & Local Development
### Deployment
text

### Local Development
text

## Credits
### Code Used
text

### Resources
text

### Acknowledgments
text









Bugs
date_input - request for date was before adding in tasks, had to remove the original function and re add it into get_task_information function

Recourses
re - Regular expression https://docs.python.org/3/library/re.html

raw string - https://www.digitalocean.com/community/tutorials/python-raw-string 

multiple rows - https://stackoverflow.com/questions/69489384/joining-multiple-rows-into-comma-separated-strings-by-group-in-python

clear terminal after error - https://teamtreehouse.com/community/ossystemcls-messing-with-my-loop-loop-is-fine-without-the-clear-screen-command-can-someone-explain

Errors
SyntaxWarning: invalid escape sequence '\ '
  prog_start = """ - Fixed by adding raw string prefix

SyntaxWarning: invalid escape sequence '\s'
  if re.match("^[a-zA-Z\s\.,'\"-]+$", project_name_input): - Fixed by adding raw string prefix

SyntaxWarning: invalid escape sequence '\s'
  if re.match("^[a-zA-Z\s\.,'\"-]+$", get_task_information): - Fixed by adding raw string prefix
