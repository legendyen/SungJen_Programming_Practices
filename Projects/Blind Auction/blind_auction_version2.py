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
  question = input("Are there any other bidders? Type 'y' or 'n'\n")
  if question == 'y':
    clear()
  elif question == 'n':
    prompt = False
    
    # Set default value to None and check for largest number in bid_dictionary
    highest_price = None
    highest_bidder_name = None
    for name, bid in bid_dict.items():
      if highest_price is None or bid >  highest_price:
        highest_price = bid
        highest_bidder_name = name
    print(f"The winner is {highest_bidder_name} with a bid of {highest_price}")
