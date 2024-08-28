# Capstone project - Coffee machine

from resources import MENU, RESOURSE


def report(data):
    initial_report = {}

    initial_report['ingredients'] = data
    initial_report['cost'] = 0
    return initial_report


# def format(report_data):
#     data = report_data['ingredients']

#     Water = data['water']
#     Milk = data['milk']
#     Coffee = data['coffee']
#     Money = data["cost"]

#     return (f'Water: {Water} ml\nMilk: {
#         Milk} ml\nCoffee: {Coffee} g\nMoney: ${Money}')


def check_resourse(customer_order, machine_capacity):
    item_needed = MENU[customer_order]['ingredients']

    current_resourse = {}
    for i in RESOURSE:
        try:
            current_resourse[i] = machine_capacity[i] - item_needed[i]
        except:
            pass

    return (current_resourse)


order = input('What do you like? (espresso/latte/cappuccino): ').lower()

START_REPORT = report(RESOURSE)
if order == 'report':
    print(START_REPORT)

else:
    machine_on = True
    while machine_on:

        order = input(
            'What do you like? (espresso/latte/cappuccino): ').lower()
        user = order
        print(user)
        print(check_resourse(user, START_REPORT))

        print(f'heres your {user}')

        if order == 'report':
            print(format(START_REPORT))
        else:
            current_resourse = check_resourse(user, RESOURSE)
            print(current_resourse)
            start_report = current_resourse
        print(current_resourse)

        order = input(
            'What do you like? (espresso/latte/cappuccino): ').lower()
        resourses = check_resourse(user, RESOURSE)

        if order == 'off':
            machine_on = False
