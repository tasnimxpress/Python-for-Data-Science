# Capstone project - Coffee machine

from resources import MENU, RESOURSE


def report(data):
    initial_report = {}

    initial_report['ingredients'] = data
    initial_report['cost'] = 0
    return initial_report


def format(report_data):
    Water = report_data['ingredients']['water']
    Milk = report_data['ingredients']['milk']
    Coffee = report_data['ingredients']['coffee']
    Money = report_data["cost"]

    return (f'Water: {Water} ml\nMilk: {
        Milk} ml\nCoffee: {Coffee} g\nMoney: ${Money}')


def remaining_resourse(customer_order, machine_capacity):
    item_needed = MENU[customer_order]['ingredients']

    current_resourse = {}
    for i in set(machine_capacity) | set(item_needed):
        try:
            remaining_resourse = machine_capacity[i] - item_needed[i]
        except:
            remaining_resourse = machine_capacity.get(i)
        current_resourse[i] = remaining_resourse

    return current_resourse


# remaining_resourse = {'coffee': 58, 'milk': 50, 'water': 50}
# MENU['espresso']['ingredients'] = {'water': 50, 'coffee': 18}


def check_resourse(order, remaining_resourse):
    resourse_needed = MENU[order]['ingredients']

    for item in resourse_needed and remaining_resourse:
        if remaining_resourse[item] >= resourse_needed[item]:
            return True
        else:
            False


order = input('What do you like? (espresso/latte/cappuccino): ').lower()

START_REPORT = report(RESOURSE)
if order == 'report':
    print(format(START_REPORT))

else:
    machine_on = True
    while machine_on:
        is_sufficient = check_resourse(order, RESOURSE)
        if is_sufficient is True:
            print('True')
        else:
            print('not enough resourse')
        order = input(
            'What do you like? (espresso/latte/cappuccino): ').lower()
        user = order
        # print(user)
        START_REPORT = report(RESOURSE)

        current_resourse = remaining_resourse(order, RESOURSE)
        RESOURSE = current_resourse
        print(RESOURSE)

        if order == 'off':
            machine_on = False
