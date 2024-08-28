# Capstone project - Coffee machine

from resources import MENU, CAPACITY

order = input('What do you like? (espresso/latte/cappuccino): ').lower()

if order == 'report':
    for item in CAPACITY:
        # print(item)
        print(f"{item}: {CAPACITY[item]}")

# for order in MENU:
print(MENU[order]['ingredients'])
