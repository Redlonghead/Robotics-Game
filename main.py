################################################################
#                 Demo Daze                        						 #
#               Last updated; 11.6.2021             	         #
################################################################
# Created by KMC Robotics:   
#   Programming
#                       - Rachel J
#												- Connor B
#                       - Andrew M
#                       - Ricky
#                       - Andrew
#    Testing
#                       - 
#                       
#
################################################################
################################################################
#BASIC PYGAME(COPY AND PASTE,IF NEEDED)
#pygame.init()
#screen = pygame.display.set_mode[14,14]
#pygame.draw.line(screen, [8,9, 5], [5,7], [9,8], 7)
#pygame.display.flip()
################################################################
import time, random
from colorama import Fore, Style, Back
from replit import clear
#import pygame #we aren't using this right now
#from gameControlFunctions import *
#separate file we can add to for sub-organizing functions
from Menu import menu
from globa import *
from Bar import *

#printBoard(bang, 1, 1)

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
    printBoard()
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
# It would just be better to use "Print" here that way it won't say "press enter" under it ; same for the "lose"
    printWait("Nice Job!")
    clear()
    print("█████████████████████████████████████████████")
    print("█▄─█─▄█─▄▄─█▄─██─▄███▄─█▀▀▀█─▄█▄─▄█▄─▀█▄─▄█░█")
    print("██▄─▄██─██─██─██─█████─█─█─█─███─███─█▄▀─██▄█")
    print("▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▀")
    clear()
    exit()

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
    #printBoard()
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
      old = loc(x, y)
      changeBoard(hole, x, y)
      printBoard()
      if old == badHouse:
        city -= 100/badCount
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
    printWait(f"You have destroyed {Fore.MAGENTA}{Style.BRIGHT}{round(100 - city, 2)}% {Style.RESET_ALL} of the cities' dangerous houses")
    #time.sleep(5)
    clear()
  else:
    printWait("You have no bombs")

#Intro ---------------------------
if yesOrNo("Would you like read the intro"): #for testing, we can make it run or not run the intro
  clear()
  printWait("DEMO DAZE\nby KMC Robotics")
  #time.sleep(1)
  #time.sleep(3)
  clear()
  printWait("Welcome to Demolition City")
  #time.sleep(2)
  printWait("Your objective is to destroy all the houses in the city, using bombs. \n These houses pose a threat to public safety. \n If you do not destroy all the dangerous houses, the citizens will have many accidents.")
  #time.sleep(2)
  printWait("You will have to: \n -Buy bombs,\n -Make money and \n -Destroy all the houses \n However, you only have  only 30 days to destroy all the dangerous houses.")
  #time.sleep(5)
  clear()
  printWait("If you fail, public safety will be compromised.")
  #time.sleep(4)
  clear()
  printWait("You will plant and set off the bombs by: ")
  ############################################################# ######
  #INSERT INSTRUCTIONS TO DESTORY BUILDINGS IN ABOVE STATEMENT
  printWait("Entering X and Y coordinates to locate where you want to drop the bomb at\nYou will be able to place a bomb exactly where you want it to be!\nThere will be a text box for you to enter in coordinates\nYou will need to enter them in coordinate pairs, without parentheses, e.g. 1,1 or 4,2")
	

#Help-----------------------------
clear()
help = input("Do you wish to return to the instructions for clarification? ")
if help:
  printWait("Your objective is to destroy all the buildings in the city\nYou have five days to do so\nYou will be notified each time a day ends\nIf you do not destroy the city within five days, you will lose and your character will die.\nYou can win by destroying all the buildings.")
  #time.sleep(10)
  clear()
  printWait("You will now start the game.")
  #time.sleep(2)
else:
	printWait("You will now start the game.")

#else:
#	print("You did not enter Yes or No, therefore, we will start the game now")
###############################################################
#time.sleep(3)
clear()


#target = input("Where do you want to attack first? Please enter X, Y coordinates:") 
################################################################
# If input = a:
# 		print new graphics, showing that "a" has been destroyed.
# or just put True/False statements; such as if a = True,:
#																									print graphic for building "a"
#NOT sure exactly how to loop it so that we don't have to repeat software every time . . . 
# make sure that target has been destroyed.
#If target has:

#while time hasn't run out-----------------
while True:
	if timeleft > 0 and not city <= 1:
		mainLoop()
		if inventory["bomb"] == 0 and money <= 15:
			printWait("You do not have any bombs left or money to buy any!")
			printWait("You will have to work, so you can earn money too buy bombs.")
	else:
		end()
#and if we want to prevent them from goint to the "Buy Stuff" platform if they have no money:
while True:
	if timeleft > o and not city <= 1:
		mainLoop()
		if inventory["bomb"] == o and money >= 15:
			printWait("You do not have enough money to buy bombs")
			printWait("You have to attack, or work to make money")
