from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    is_on = True
    drinks = Menu()
    machine = CoffeeMaker()
    money = MoneyMachine()

    while is_on:
        choice = input(f"What would you like? ({drinks.get_items()}): ").lower()
        drink = drinks.find_drink(choice)

        if choice == "off":
            is_on = False
        elif choice == "report":
            machine.report()
            money.report()
        elif machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
        else:
            continue


coffee_machine()