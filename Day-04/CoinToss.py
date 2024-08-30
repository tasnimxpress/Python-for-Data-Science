"""This is virtual coin toss program, You will choose side and then we will toss the program to 
see if you win or loss."""

import random

user_choice = input("Head or Tail? Type 'H' or 'T': ")

random_toss = random.randint(0, 1)

if random_toss == 0:
    side = 'Tail'
else:
    side = 'Head'

if (random_toss == 1 and user_choice == 'H') or (random_toss == 0 and user_choice == 'T'):
    print(f"It's {side}. You win.")
else:
    print(f"It's {side}. You lose.")
