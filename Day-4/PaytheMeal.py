"""
This program will select a random name from a list of names,
selected person will pay the bill for meal."""
import random

name_string = input('Enter the name: ')
names = name_string.split(', ')

# print(names)

number_of_name = len(names)

toss = random.randint(0, number_of_name-1)
paid_by = names[toss]

print(f'{paid_by} will pay the meal.')

"Another approach to write this code is use choice function from list object."

# option_2 = random.choice(names)

# print(f'From second toss: {option_2} will pay the bill')
