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
            "water": 120,
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



def report(resource, profit):
    """Print report"""
    print(f"""Water: {resource['water']}ml
Milk: {resource['milk']}ml
Coffee: {resource['coffee']}g
Money: ${profit}
""")


def resource_check(menu):
    """Check if resource is sufficient"""
    for key in menu['ingredients']:
        if resources[key] < menu['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def transaction_check(cost):
    """Check if coin is sufficient"""
    t_coin = 0
    print("Please insert coins")
    t_coin = float(input("How many $1: ")) * 1
    t_coin += float(input("How many 50C: ")) * 0.5
    t_coin += float(input("How many 20C: ")) * 0.2
    t_coin += float(input("How many 10C: ")) * 0.1

    if t_coin >= cost:
        change = t_coin - cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(menu):
    """Deduct resources"""
    for key in menu['ingredients']:
        resources.update({key: resources[key] - menu['ingredients'][key]})


def coffee_machine():
    profit = 0
    is_on = True

    while is_on:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if action == 'off':
            is_on = False
        elif action == 'report':
            report(resources, profit)
        else:
            if resource_check(MENU[action]):
                if transaction_check(MENU[action]['cost']):
                    make_coffee(MENU[action])
                    profit += MENU[action]['cost']
                    print(f"Here is your {action}. Enjoy!")


coffee_machine()
