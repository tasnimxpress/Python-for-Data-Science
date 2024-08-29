from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
transaction = MoneyMachine()

menu = Menu()


profit = 0
machine_on = True
while machine_on:
    item = menu.get_items()
    order = input(f'What would you like? ({item}): ')

    if order == 'report':
        coffee_machine.report()
    elif order == 'off':
        machine_on = False
    else:
        drink = menu.find_drink(order)
        coffee_machine.is_resource_sufficient(drink)
        money = transaction.make_payment(drink)
        if money is True:
            coffee_machine.make_coffee(drink)
