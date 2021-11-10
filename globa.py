#this lets us reference global variables in all files as opposed to only main.py so long as they are defined in here
#this can also potentially let use change game configurations easier or let people customize them
import random
from colorama import Back

boardX = 10
boardY = 10
timeleft = 30
city = 100
inventory = {
  "bomb": 0
}
money = 0
bldEmojis = ["🏢 ", "🏛️  ", "🏘️  ", "🏠 ", "🏚️  ", "🏨 ", "⛪ ", "🏫 ", "🕌 ", "🏭 ", "🏦 ", "🪦  "]
badHouse = "🏚️  "
bomb = "💣 "
bang = "💥 "
conf = "😕 "
#hole = "   "
hole = f"{Back.BLACK}  {Back.CYAN} "
#hole = "🕳️  "
board=[]
badCount = 0
for i in range(0, boardY):
  board.append([])
  for o in range(0, boardX):
    newBuild = random.choice(bldEmojis)
    board[i].append(newBuild)
    if newBuild == badHouse:
      badCount += 1