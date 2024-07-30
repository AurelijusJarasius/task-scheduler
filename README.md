Bugs
date_input - request for date was before adding in tasks, had to remove the original function and re add it into get_task_information function

Recourses
re - Regular expression https://docs.python.org/3/library/re.html

raw string - https://www.digitalocean.com/community/tutorials/python-raw-string 

Errors
SyntaxWarning: invalid escape sequence '\ '
  prog_start = """ - Fixed by adding raw string prefix

SyntaxWarning: invalid escape sequence '\s'
  if re.match("^[a-zA-Z\s\.,'\"-]+$", project_name_input): - Fixed by adding raw string prefix

SyntaxWarning: invalid escape sequence '\s'
  if re.match("^[a-zA-Z\s\.,'\"-]+$", get_task_information): - Fixed by adding raw string prefix
