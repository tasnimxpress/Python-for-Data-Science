# Capstone project - Coffee machine

from resources import MENU, RESOURSE

PROFIT = 0


def report(data):
    initial_report = {}

    initial_report['ingredients'] = data
    initial_report['cost'] = PROFIT
    return initial_report


def format(report_data):
    Water = report_data['ingredients']['water']
    Milk = report_data['ingredients']['milk']
    Coffee = report_data['ingredients']['coffee']
    Money = report_data["cost"]

    return (f'Water: {Water} ml\nMilk: {
        Milk} ml\nCoffee: {Coffee} g\nMoney: ${Money}')


def remaining_resourse(customer_order, machine_capacity):
    current_resourse = {}
    for i in set(machine_capacity) | set(customer_order):
        try:
            remaining_resourse = machine_capacity[i] - customer_order[i]
        except:
            remaining_resourse = machine_capacity.get(i)
        current_resourse[i] = remaining_resourse

    return current_resourse


def is_resourse_sufficient(order, remaining_resourse):
    for item in order:
        if order[item] > remaining_resourse[item]:
            print(f"We dont have enough {item}")
            return False
    return True


machine_on = True
while machine_on:
    order = input('What do you like? (espresso/latte/cappuccino): ').lower()

    # START_REPORT = report(RESOURSE)

    if order == 'report':
        print(format(report(RESOURSE)))
    elif order == 'off':
        machine_on = False
    else:
        choice = MENU[order]['ingredients']

        check_resourse = is_resourse_sufficient(choice, RESOURSE)
        if check_resourse is True:
            print(f"Here is your {order}. Enjoy!")
            PROFIT += MENU[order]['cost']
            current_resourse = remaining_resourse(choice, RESOURSE)
            RESOURSE = current_resourse
