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

password_list = []
for i in range(num_letter):
    password_list.append(random.choice(letters))

for i in range(num_symbol):
    password_list.append(random.choice(symbols))

for i in range(num_number):
    password_list.append(random.choice(numbers))

# reorder the password to make it hard to predict
reorder_list = random.sample(password_list, len(password_list))

# convert password_list to string
password = ''.join(reorder_list)


"Alternative Approach"
# # reorder the password to make it hard to predict
# random.shuffle(password_list)

# # convert password_list to string
# password = ""
# for i in password_list:
#     password += i

print(password)
