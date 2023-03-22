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
    
    # set default value to None and check for largest number in bid_dictionary
    highest_price = None
    highest_bidder_name = None
    for name, bid in bid_dict.items():
      if highest_price is None or bid >  highest_price:
        highest_price = bid
        highest_bidder_name = name
    print(f"The winner is {highest_bidder_name} with a bid of {highest_price}")
