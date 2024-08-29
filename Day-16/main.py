from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    item = menu.get_items()
    order = input(f'What would you like? ({item}): ')

    if order == 'report':
        coffee_machine.report()
        money_machine.report()
    elif order == 'off':
        machine_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost) is True:
                coffee_machine.make_coffee(drink)
