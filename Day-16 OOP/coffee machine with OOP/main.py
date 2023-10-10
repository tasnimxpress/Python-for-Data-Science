from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

on = True
while on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: \n")

    if choice == 'off':
        on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.get_items()
        menu_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(menu_drink) and money_machine.make_payment(menu_drink.cost):
            coffee_maker.make_coffee(menu_drink)
