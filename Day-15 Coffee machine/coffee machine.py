from menus import MENU, resources

PROFIT = 0

#is resource sufficient
def check_resource(coffee_type):
    if resources['water'] < coffee_type['water']:
        print('\nNot enough water in machine!')
        return False
    elif resources['milk'] < coffee_type['milk']:
        print('\nNot enough milk in machine!')
        return False
    elif resources['coffee'] < coffee_type['coffee']:
        print('\nNot enough coffee in machine!')
        return False
    else:
        return True


#is there enough coins
def check_enough_coins():
    quarters = 0.25 * int(input('How many quarters: $'))
    dimes = 0.10 * int(input('How many dimes: $'))
    nickles = 0.05 * int(input('How many nickles: $'))
    pennies = 0.01 * int(input('How many pennies: $'))
    total = (quarters + dimes + nickles + pennies)
    return total


#is transaction complete
def is_transaction_complete(coffee_type, total):
    if total >= coffee_type['cost']:
        changed = total - coffee_type['cost']
        changed = round(changed, 2)
        print(f'\nHere is your change: {changed}')
        global PROFIT
        PROFIT += coffee_type['cost']
        return True
    else:
        print(f'\nNot enough money. Returned {total}')
        return False


#update resources and make coffee
def make_coffee(coffee_type, menu):
    """Deduct the required ingredients from the resources."""
    for item in menu:
        resources[item] -= menu[item]
    print(f'\nHere is your {coffee_type} ☕️. Enjoy')



machine_stop = False
while not machine_stop:
    user_choice = input('\nWhat would you like? (latte/espresso/cappuccino):\n').lower()

    if user_choice == 'off':
        machine_stop = True
    elif user_choice == 'report':
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {PROFIT}")

    else:
        drink = MENU[user_choice]

        if check_resource(drink['ingredients']) is True:
            print('Please insert coins.')
            payment = check_enough_coins()

            if is_transaction_complete(drink, payment) is True:
                print(f'Making {user_choice}')

                make_coffee(user_choice, drink['ingredients'])
