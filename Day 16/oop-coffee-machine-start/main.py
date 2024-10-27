from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#Print report
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        print("Turning off...")
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) #czyli, nie tzreba tworzyć obiektu, zeby miec dostęp do klasy
        # Check resource sufficient
        if coffe_maker.is_resource_sufficient(drink):
            #Process coins
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)




#Check transaction successful
#Make coffee