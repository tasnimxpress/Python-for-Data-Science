# Capstone project - Coffee machine

from resources import MENU, RESOURSE


def check_resourse(customer_order, machine_capacity):
    item_needed = MENU[customer_order]['ingredients']
    item_cost = MENU[customer_order]['cost']

    current_resourse = {}
    for i in RESOURSE:
        try:
            current_resourse[i] = machine_capacity[i] - item_needed[i]
            current_resourse['money'] = item_cost
        except:
            current_resourse[i] = machine_capacity[i]

    return (current_resourse)


def report(data):
    initial_report = {}

    initial_report['water'] = data['water']
    initial_report['milk'] = data['milk']
    initial_report['coffee'] = data['coffee']
    initial_report['money'] = 0

    return initial_report


def format(report_data):
    Water = report_data['water']
    Milk = report_data['milk']
    Coffee = report_data['coffee']
    Money = report_data["money"]

    return (f'Water: {Water} ml\nMilk: {
        Milk} ml\nCoffee: {Coffee} g\nMoney: ${Money}')


order = input('What do you like? (espresso/latte/cappuccino): ').lower()
start_report = report(RESOURSE)
print(format(start_report))

machine_on = True
while machine_on:
    user = order
    print(f'heres your {user}')
    order = input('What do you like? (espresso/latte/cappuccino): ').lower()
    resourses = check_resourse(user, RESOURSE)

    if order == 'report':
        resourses = check_resourse(user, RESOURSE)
        print(format(resourses))

    if order == 'off':
        machine_on = False
