#These are awesome menus I (Andrew) made that I expect we will want to use eventually

from getkey import getkey, keys
import cursor
import replit
from colorama import Fore, Style

#example: menu(["option1", "option2", "option3"], ">> ", "This is a menu", 2) #This will return 0 for option 1, 2 for option2, etc

def menu(options:list, indicator:str, description:str, returnMethod:int, startIndex:int=0):
  cursor.hide()
  replit.clear()
  selected = startIndex
  #inpute = getkey()
  #print(f"this selected = {selected}")
  if indicator == "numbered":
    useNumbered = True
  else:
    useNumbered = False
  inpute = 0
  while True:
    #print(f"that selected = {selected}")
    #inpute = getkey()
    if inpute == keys.UP:
        if selected == 0:
          selected = len(options) - 1
        else:
          selected -= 1
    elif inpute == keys.DOWN:
        if selected == len(options) - 1:
          #print(f"{Fore.RED}YES{Style.RESET_ALL}")
          selected == 0
        else:
          selected += 1
    if not inpute == keys.ENTER:
      replit.clear()
      #print(f"not labeled selected = {selected}")
      if description != "":
        print(description)
      for i in range(0, len(options)):
        #print(f"i = {i}")
        if useNumbered:
          indicator = f"{i + 1}. "
        if selected == i:
          print(f"{indicator}{Fore.GREEN}{options[i]}{Style.RESET_ALL}")
        else:
          print(f"{indicator}{options[i]}")
      inpute = getkey()
      #print(f"last selected = {selected}")
    else:
      break
  cursor.show()
  if returnMethod == 1:
    return options[selected]
  elif returnMethod == 2: #numbers
    return selected
  else:
    return [selected, options[selected]]