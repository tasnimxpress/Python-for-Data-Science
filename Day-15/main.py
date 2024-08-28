# Capstone project - Coffee machine

from resources import MENU, RESOURSE
import os
import time
PROFIT = 0


def report(inventory):
    """
    Generates a report of the machine's current stock and profit information.

    Args:
        inventory (dict): A dictionary representing the current stock of resources in the machine, 
        where keys are ingredient names and values are their available quantities.
    """
    initial_report = {}

    initial_report['ingredients'] = inventory
    initial_report['cost'] = PROFIT
    return initial_report


def format(report_data):
    """
    Formats the machine's stock and profit data into a readable string.

    Returns:
        str: A formatted string displaying the quantities of items in machine's stock, as well as the total profit in dollars.
    """
    Water = report_data['ingredients']['water']
    Milk = report_data['ingredients']['milk']
    Coffee = report_data['ingredients']['coffee']
    Money = report_data["cost"]

    return (f'Water: {Water} ml\nMilk: {
        Milk} ml\nCoffee: {Coffee} g\nMoney: ${Money}')


def remaining_resourse(customer_order, inventory):
    """
    Calculates the remaining resources in the machine's stock after fulfilling a customer's order.

    Returns:
        dict: A dictionary showing the remaining quantities of each resource in the machine's stock after subtracting the quantities required for the customer's order. If an ingredient is not needed for the order, its original value from the inventory is retained.
    """
    current_resourse = {}
    for i in set(inventory) | set(customer_order):
        try:
            remaining_resourse = inventory[i] - customer_order[i]
        except:
            remaining_resourse = inventory.get(i)
        current_resourse[i] = remaining_resourse

    return current_resourse


def is_resourse_sufficient(order, remaining_resourse):
    """
    Checks if available resources are sufficient for a customer's order.

    Args:
        order (dict): Required ingredients and their quantities.
        remaining_resourse (dict): Available ingredients and their quantities.

    Returns:
        bool: True if all ingredients are sufficient; otherwise False, with a message indicating any shortage.
    """
    for item in order:
        if order[item] > remaining_resourse[item]:
            print(f"\nWe dont have enough {item}")
            return False
    return True


def check_transaction(item_price, inserted_amount):
    """
    Checks if the inserted amount is sufficient for the item price and provides the necessary feedback.

    Args:
        item_price (float): The price of the item being purchased.
        inserted_amount (float): The amount of money inserted by the customer.

    Returns:
        bool: True if the inserted amount is equal to or greater than the item price; False otherwise. Prints the amount of change if applicable, or a refund message if insufficient money.
    """
    if item_price < inserted_amount:
        change = round(inserted_amount - item_price, 2)
        print(f"\nHere is {change} dollars in change.")
        return True
    elif item_price == inserted_amount:
        return True
    else:
        print(f"\nSorry that's not enough money. item price ${
              item_price}; you inserted ${round(inserted_amount, 2)} \nMoney refunded.")
        return False


print('Welcome to the Blackberry Cafe')
machine_on = True
while machine_on:
    order = input('\nWhat do you like? (espresso/latte/cappuccino): ').lower()

    if order == 'report':
        print(format(report(RESOURSE)))
    elif order == 'clean':
        os.system('cls')
        print('Welcome to the Blackberry Cafe')
    elif order == 'off':
        os.system('cls')
        machine_on = False
    elif order not in ['espresso', 'latte', 'cappuccino']:
        print(f"Sorry, We don't serve {order}")
    else:
        choice = MENU[order]['ingredients']

        check_resourse = is_resourse_sufficient(choice, RESOURSE)
        if check_resourse is True:
            print('\nPlease insert coins.')
            quarter = float(input('How many quarters: '))
            nickel = float(input('How many nickels: '))
            dime = float(input('How many dimes: '))
            penny = float(input('How many pennies: '))

            total_coins = (quarter * 0.25) + (nickel * 0.05) + \
                (dime * 0.10) + (penny * 0.01)
            price = MENU[order]['cost']

            transaction = check_transaction(price, total_coins)
            if transaction is True:
                print(f"\nHere is your {order}. Enjoy!")
                PROFIT += MENU[order]['cost']
                current_resourse = remaining_resourse(choice, RESOURSE)
                RESOURSE = current_resourse
                time.sleep(5)
                os.system('cls')
