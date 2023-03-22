# import os.system module to clear console for every new bid
import os
clear = lambda: os.system('cls')
clear()

print("Welcome to the secret auction program.")

prompt = True
bid_dict = {}
while prompt == True:
  name = input("What is your name?\n")
  bid = input("What is your bid?: \n$")
  bid_dict[name] = bid
  
  # set up if-else statements to excecute control flow whether to clear the console or stop the loop
  question = input("Are there any other bidders? Type 'y' or 'n'\n")
  if question == 'y':
    clear()
  elif question == 'n':
    prompt = False
    
    # use items() to retrieve tuple and set up reverse-sorted list to look for biggest value
    list = []
    for k, v in bid_dict.items():
      list.append((v, k))
    list = sorted(list, reverse=True)
    winner_name = list[0][1]
    winner_price = list[0][0]
    print(f"The winner is {winner_name} with a bid of {winner_price}")
