"""
Program to create a game using if else statement, logical operators, control flow"""

Greetings = "Welcome to treasure island.\nYour mission is to find the treasure. Caution: Don't Die."
print(Greetings)

turn = input(
    "\nYou're at a cross road. Where do you want to go? \nType 'l' for left and 'r' for right: ")

if turn == "l":
    print("\nYou came to a lake. \nThere is an island in the middle of the lake.")
    lake = input("Type 'w' to wait for a boat, type 's' to swim across. ")

    if lake == 'w':
        print('\nYou arrive at the lake unharmed. \nThere is a house with 3 door. one yellow, one red, one blue.\nhich door your want to open? ')
        color = input("Type 'b' for blue, 'y' for yellow, 'r' for red: ")

        if color == 'b':
            print('\nYou enter a room of beasts. Game Over.')
        elif color == 'r':
            print("\nThis room is buring in fire. Game Over.")
        else:
            print("\nCongrats.\nYou get the Gems.")

    else:
        print("\nYou attacked by sharks. \nGame Over.")

else:
    print("\nThis road is blocked. Game Over.")
