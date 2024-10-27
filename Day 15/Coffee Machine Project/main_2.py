MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(chosen_coffee):
    """Check resources sufficient"""
    # print(MENU[coffe])
    if RESOURCES["water"] - MENU[chosen_coffee]["ingredients"]["water"] >= 0:
        if RESOURCES["milk"] - MENU[chosen_coffee]["ingredients"].get("milk", 0) >= 0:
            if RESOURCES["coffee"] - MENU[chosen_coffee]["ingredients"]["coffee"] >= 0:
                return "Yes"
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")

def process_coin():
    print("Please insert coins.")
    quarters_to_dollars = int(input("How many quarters? "))*0.25
    dimes_to_dollars = int(input("How many dimes? "))*0.1
    nickles_to_dollars = int(input("How many nickles? "))*0.05
    pennies_to_dollars = int(input("How many pennies? "))*0.01
    total = quarters_to_dollars+dimes_to_dollars+nickles_to_dollars+pennies_to_dollars
    return total



def choose_what_to_do():
    """Choose what to do - coffee, report, off"""
    is_on = True
    current_money = 0
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            print ("Turning off...")
            is_on = False
        elif user_choice=="report":
            print(f"Water: {RESOURCES["water"]}ml\nMilk: {RESOURCES["milk"]}ml\nCoffee: {RESOURCES["coffee"]}g\nMoney: ${current_money}")
        elif user_choice!="espresso" and user_choice!="latte" and user_choice!="cappuccino":
            print("Wrong answer.")
        else:
            if is_enough_resources(user_choice):
                inserted_coins = process_coin()
                #Check transaction successful?
                if inserted_coins>=MENU[user_choice]["cost"]:
                    current_money+=MENU[user_choice]["cost"]
                    RESOURCES["water"]-=MENU[user_choice]["ingredients"]["water"]
                    RESOURCES["milk"]-=MENU[user_choice]["ingredients"].get("milk",0)
                    RESOURCES["coffee"]-=MENU[user_choice]["ingredients"]["coffee"]
                    #Coffee making
                    if inserted_coins>MENU[user_choice]["cost"]:
                        print(f"Here is ${round(inserted_coins - MENU[user_choice]["cost"], 2)} dollars in change.")
                    print("Coffee making...")
                    print(f"Here is your {user_choice}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")

choose_what_to_do()


