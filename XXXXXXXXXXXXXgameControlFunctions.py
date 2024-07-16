import time
from colorama import Fore, Style, Back
from replit import clear
#from getkey import getkey, keys
from Menu import *
from globa import *

#given a yes or no question, this function returns a True for yes and a False for no with editable lists for yes's and no's and any combination of capital and lowercase numbers
def yesOrNo(question):
  positives = ["yes", "y", "yeah", "ya", "ok", "go", "onward", "forward", "positive, YES, Yes, si", "ita"]
  #negatives = ["no", "n", "nah", "naw", "negative"] #oops I don't actually need this
  answer = input(f"{question}: ")
  if answer.lower() in positives:
    return True
  else:
    return False

#easy print - wait for enter or print - wait for time function and it can clear after
#explaned in function Explanations
def printWait(text, c=False, t=0):
  print(text)
  if t != 0:
    time.sleep(t)
  else:
    input(f"{Fore.WHITE}{Style.DIM}Press Enter{Style.RESET_ALL}")
    #inpute = getkey()
    #while inpute != keys.ENTER:
    #  inpute = getkey()
  if c:
    clear()

#takes two numbers in num1, num2 format and returns a list of integer equivalents
def getCoords():
  bad = True
  thing = [100, 100]
  while bad:
    inpute = input(f"Where do you want to attack?\nEnter X, Y coordinates (the city is {boardX} by {boardY}): ")
    new = inpute.split(",")
    try:
      thing = [abs(int(new[0])), abs(int(new[1]))]
      break
    except TypeError:
      printWait("Invalid coordinates, try again\nHINT: Use numbers not words")
    except IndexError:
      printWait("Invalid coordinates, try again\nHINT: Make sure there are exactly 2 numbers seperated by a comma")
    except ValueError:
      printWait("Invalid coordinates, try again\nHINT: Use numbers not words")
    if thing[0] > boardX or thing[1] > boardY:
      printWait(f"Invalid coordinates, the board is {boardX} by {boardY} and you gave at least one number that was too big to fit on it")
    clear()
  return thing

def buy(item, prices, itemNum):
  global money
  repeat = True
  while repeat:
    ask = f"How many {item}s would you like to buy?\nRemember you have {Fore.BLUE}{Style.BRIGHT}${money}{Style.RESET_ALL} and {Fore.BLUE}{Style.BRIGHT}{inventory[item]} {item}s{Style.RESET_ALL}."
    options = []
    for i in range(0, len(prices)):
      options.append(f"{itemNum[i]} {item}s for ${prices[i]}")
    options.append(f"{Style.BRIGHT}Nothing, exit store.{Style.RESET_ALL}")
    choice = menu(options, ">> ", ask, 2)
    if choice == len(options) - 1:
      printWait(f"Ok, you didn't buy any {item}s")
      repeat = False
    elif money - prices[choice] >= 0:
      money -= prices[choice]
      inventory[item] += itemNum[choice]
      printWait(f"Your purchase was successful.\nYou now have {Fore.BLUE}{Style.BRIGHT}${money}{Style.RESET_ALL} and {Fore.BLUE}{Style.BRIGHT}{inventory[item]} {item}s{Style.RESET_ALL}.")
      clear()
    else:
      printWait(f"You don't have enough money to buy that many more {item}s")

def lose():
  print("╔╗──╔╦═══╦╗─╔╗╔╗──╔═══╦═══╦═══╗")
  print("║╚╗╔╝║╔═╗║║─║║║║──║╔═╗║╔═╗║╔══╝")
  print("╚╗╚╝╔╣║─║║║─║║║║──║║─║║╚══╣╚══╗")
  print("─╚╗╔╝║║─║║║─║║║║─╔╣║─║╠══╗║╔══╝")
  print("──║║─║╚═╝║╚═╝║║╚═╝║╚═╝║╚═╝║╚══╗")
  printWait("──╚╝─╚═══╩═══╝╚═══╩═══╩═══╩═══╝")
  clear()
  exit()

def work():
  global money, timeleft
  printWait("You spent a day working and made $100")
  money += 100
  timeleft -= 1

def mainLoop():
  attackOrBuy = menu(["Attack", "Buy Stuff", "Work"], ">> ", "What would you like to do:", 2)
  if attackOrBuy == 0:
    attack()
    #time.sleep(0)
  elif attackOrBuy == 1:
    buy("bomb", [15, 30, 40, 50, 60], [2, 4, 6, 8, 10])
  elif attackOrBuy == 2:
    work()

def end():
  #once time has run out----------------
  if city >= 10:
	  printWait("You ran out of time!\nGood try")
	  lose()

  else:
	  printWait("Nice Job!")
	  clear()
	  print("█████████████████████████████████████████████")
	  print("█▄─█─▄█─▄▄─█▄─██─▄███▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█░█")
	  print("██▄─▄██─██─██─██─█████─█─█─█─███─███─█▄▀─██▄█")
	  printWait("▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▀")
	  clear()

def printBoard(thing=0, x=0, y=0):
  print(f"{Back.CYAN}   ", end="")
  for p in range(0, boardX):
    maths = p+1
    if maths <= 9:
      print(f"{maths}  ", end="")
    else:
      print(f"{maths} ", end="")
  print()
  for i in range(0, boardY):
    maths = i+1
    if maths <= 9:
      print(f" {maths} ", end="")
    else:
      print(f"{maths} ", end="")
    for o in range(0, boardX):
      if i+1==y and o+1==x and thing:
        print(thing, end="")
      else:
        print(board[i][o], end="")
    print()
  print(f"{Style.RESET_ALL}")

def changeBoard(thing, x, y):
  board[y-1][x-1] = thing

def loc(x, y):
  return board[y-1][x-1]

def attack():
  global timeleft, city
  if inventory["bomb"] > 0:
    print(f"You have {Fore.RED}{Style.BRIGHT}{timeleft}{Style.RESET_ALL} days left!")
    printBoard()
    target = getCoords()
    x = target[0]
    y = target[1]
    ################################################################
    # If input = a:
    # 		print new graphics, showing that "a" has been destroyed.
    # or just put True/False statements; such as if a = True,:
    #																									print graphic for building "a"
    #NOT sure exactly how to loop it so that we don't have to repeat software every time . . . 
    # make sure that target has been destroyed.
    #If target has:
    #time.sleep(5)
    clear()
    for i in range(0, y):
      printBoard(bomb, x, i+1)
      time.sleep(0.2)
      clear()
    if loc(x, y) != hole:
      printBoard(bang, x, y)
      time.sleep(1)
      clear()
      changeBoard(hole, x, y)
      printBoard()
      if loc(x, y) == badHouse:
        city -= 100/board.count(badHouse)
        printWait("You destroyed a dangerous house")
      else:
        printWait(f"Oh no, you destroyed a safe building,\ngood thing no one was in there, try to avoid that next time")
    else:
      printBoard(conf, x, y)
      printWait("Your target has not been destroyed, because you already destroyed it.")
    #time.sleep(5)
    clear()
    timeleft -= 1
    inventory["bomb"] -= 1
    print(f"You have {Fore.RED}{Style.BRIGHT}{timeleft}{Style.RESET_ALL} days left!")
    printWait(f"You have destroyed {Fore.MAGENTA}{Style.BRIGHT}{round(100 - city, 2)}%{Style.RESET_ALL} of the cities' dangerous houses")
    #time.sleep(5)
    clear()
  else:
    printWait("You have no bombs")