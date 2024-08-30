"Program of Rock paper scissors game"

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

element = [rock, paper, scissors]

users_input = int(input(
    "What do you choose? Type '0' for rock, '1' for paper, '2' for Scissors: "))

if users_input >= 3 or users_input < 0:
    print("You type an invalid number. You loss.")
else:
    computer_choice = random.choice(element)
    users_choice = element[users_input]

    print(f"{users_choice}")
    print(f"Computers choice:\n{computer_choice}")

    if computer_choice == users_choice:
        print('Draw')
    elif computer_choice == element[0] and users_choice == element[2]:
        print("computer wins")
    elif computer_choice == element[2] and users_choice == element[1]:
        print("computer wins")
    elif computer_choice == element[1] and users_choice == element[0]:
        print("computer wins")
    else:
        print("you win")
