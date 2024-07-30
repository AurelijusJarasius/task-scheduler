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
