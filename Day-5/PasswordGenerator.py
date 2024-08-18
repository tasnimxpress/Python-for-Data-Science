"""
This program will generate a strong password based on your preference."""

import string
import random

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

num_letter = int(input('How many letters would you like in your password?: '))
num_symbol = int(input('How many symbols would you like?: '))
num_number = int(input('How many numbers would you like?: '))

characters = []
for i in range(num_letter):
    characters.append(random.choice(letters))

for i in range(num_symbol):
    characters.append(random.choice(symbols))

for i in range(num_number):
    characters.append(random.choice(numbers))


shuffle = random.sample(characters, len(characters))

password = ''.join(shuffle)

print(password)
