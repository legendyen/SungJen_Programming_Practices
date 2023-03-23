from dictionaries import MENU, profit, resources


def check_resources(food_name):
    ingredients = MENU[food_name]["ingredients"]
    for k in ingredients:
        if resources[k] < ingredients[k]:
            print(f"Sorry there is not enough {k}.")
    print("PLease insert coins.")


def process_coins(quarters, dimes, nickles, pennies, food_name):
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if MENU[food_name]["cost"] <= total:
        global profit
        profit += MENU[food_name]["cost"]
        change = total - MENU[food_name]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {food_name}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_food(food_name):
    ingredients = MENU[food_name]["ingredients"]
    for i in ingredients:
        resources[i] -= ingredients[i]


# TODO: Prompt user by asking which food do they want?
while True:
    print("Hamburger: $3.0\nSandwich: $2.5\nHot-dog: $1.5")
    prompt = input("What would you like? (hamburger/sandwich/hot-dog)\n").lower()
    # TODO: Turn off the Vendor Machine by entering “off” to the prompt
    if prompt == "off":
        break
    # TODO: Print report by entering "report" to the prompt
    elif prompt == "report":
        for key in resources:
            print(f"{key.title()}: {resources[key]}")
        print(f"Money: {profit}")
        print("________________")
    # TODO: When receive food order, check resources sufficient
    elif prompt == "hamburger" or prompt == "sandwich" or prompt == "hot-dog":
        check_resources(prompt)
        # TODO: Process coins and check if transactions is successful
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        process_coins(quarter, dime, nickle, penny, prompt)
        # TODO: Make food and update resources
        make_food(prompt)
