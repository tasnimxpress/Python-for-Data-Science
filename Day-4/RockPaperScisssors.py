"Program of Rock paper scissors game"

import random

rock = "1111"
paper = "2222"
scissors = "3333"

element = [rock, paper, scissors]

users_input = int(input(
    "What do you choose? Type '0' for Paper, '1' for Rock, '2' for Scissors: "))

computer_choice = random.choice(element)
users_choice = element[users_input]

print(f"Computers choice:\n{computer_choice}")
print(f"Your choice:\n{users_choice}")

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
