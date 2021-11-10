from colorama import Back, Style

def bar(length:str, filled:str):
  filled -= 1
  temp = ""
  for i in range(0, length):
    if i <= filled:
        if i < length/5:
          temp += f"{Back.RED} "
        elif i >= length/5 and i < length/5*2:
          temp += f"{Back.YELLOW} "
        else:
          temp += f"{Back.GREEN} "
    else:
      temp += f"{Style.RESET_ALL} "
  return temp + f"{Style.RESET_ALL}"