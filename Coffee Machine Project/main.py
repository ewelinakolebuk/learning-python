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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coin():
    print("Please insert coins.")
    quarters_to_dollars = int(input("How many quarters? "))*0.25
    print(quarters_to_dollars)
    dimes_to_dollars = int(input("How many dimes? "))*0.1
    nickles_to_dollars = int(input("How many nickles? "))*0.05
    pennies_to_dollars = int(input("How many pennies? "))*0.01
    total = quarters_to_dollars+dimes_to_dollars+nickles_to_dollars+pennies_to_dollars
    return total
    # coins={               #do wyjebania
    #     "quarter": 0.25,
    #     "dime": 0.1,
    #     "nickel": 0.05,
    #     "penny": 0.01,
    #        }
    # for key in coins:
    #     value=coins[key]*int(input(f"How many key? "))

def choose_what_to_do():
    """Choose what to do - coffee, report, off"""
    is_on = True
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]
    current_money = 0
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            print ("Turning off...")
            is_on = False
        elif user_choice=="report":
            print(f"Water: {current_water}ml\nMilk: {current_milk}ml\nCoffee: {current_coffee}g\nMoney: ${current_money}")
        elif user_choice!="espresso" and user_choice!="latte" and user_choice!="cappuccino":
            print("Wrong answer.")
        else:
            def drink(coffe):
                """Check RESOURCES sufficient"""
                #print(MENU[coffe])
                if current_water - MENU[coffe]["ingredients"]["water"] >= 0:
                    if current_milk - MENU[coffe]["ingredients"].get("milk", 0) >= 0:
                        if current_coffee - MENU[coffe]["ingredients"]["coffee"] >= 0:
                            return "Yes"
                        else:
                            print("Sorry there is not enough coffee.")
                    else:
                        print ("Sorry there is not enough milk.")
                else:
                    print ("Sorry there is not enough water.")
            is_enough_resources = drink(user_choice)
            if is_enough_resources =="Yes":
                inserted_coins = process_coin()
                #Check transaction successful?
                if inserted_coins>=MENU[user_choice]["cost"]:
                    current_money+=MENU[user_choice]["cost"]
                    current_water-=MENU[user_choice]["ingredients"]["water"]
                    current_milk-=MENU[user_choice]["ingredients"].get("milk",0)
                    current_coffee-=MENU[user_choice]["ingredients"]["coffee"]
                    if inserted_coins>MENU[user_choice]["cost"]:
                        print(f"Here is ${round(inserted_coins - MENU[user_choice]["cost"], 2)} dollars in change.")
                    print("Coffee making...")
                    print(f"Here is your {user_choice}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")

choose_what_to_do()


