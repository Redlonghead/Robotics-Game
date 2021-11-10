from replit import db, clear
from colorama import Fore, Style
from hiddenPass import hiddenPass
from Menu import menu

'''variables = {
  "variable1":"value1"
}

username = ""'''

users = {}
try:
  users = db["users"]
except KeyError:
  db["users"] = {}

def makeAccount():
  global username
  print("Make an account so you can save your progress\nMake sure you take note of any spaces or capitals because they matter:")
  username = input("Username: ")
  pass1 = hiddenPass("Password: ")
  pass2 = hiddenPass("Confirm Password: ")
  while pass1 != pass2:
    pass1 = input("Those aren't the same, try again\nPassword: ")
    pass2 = hiddenPass("Re-confirm Password: ")
  users[username] = {
    "password": pass1,
    "variables": variables
  }
  input(f"Login Created\n{Fore.WHITE}{Style.DIM}Press Enter{Style.RESET_ALL}")

def login(loadData=True):
  global variables, username
  print("Login in below.")
  username = input("Username: ")
  password = hiddenPass('Password: ')
  try:
    while password != users[f"{username}"]["password"]:
      username = input("Username or password incorrect, try again\nUsername: ")
      password = hiddenPass('Password: ')
    if loadData:
      variables = users[f"{username}"]["variables"]
  except KeyError:
    input("Unknown username, check your spelling\nPress Enter to Login again.")
    clear()
    login()  

def signInMenu():
  global variables, username
  choice = menu(["Login", "Play as Guest", "Make a new account"], ">> ", "Sign In", 2)
  if choice == 0:
    login()
  elif choice == 1:
    username = "guest"
  elif choice == 2:
    makeAccount()

def save():
  if username != "guest":
    users[f"{username}"]["variables"] = variables
  else:
    choice = menu(["Login", "Don't Save"], ">> ", "You can't save as a guest, do you want to login to save?", 2)
    if choice == 0:
      login(False)
      users[f"{username}"]["variables"] = variables
    else:
      pass