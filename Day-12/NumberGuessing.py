"Flowchart is available in the current folder"
import random

EASY = 5
HARD = 10
NUMBER = random.randint(1, 100)

print(NUMBER)

choose_level = input('Choose a Game level- Easy or Hard: ').upper()
guess = int(input('\nEnter your guess: '))


def attempt(user_guess, difficulty_level):
    if user_guess != NUMBER:
        return difficulty_level - 1


if guess > NUMBER:
    print('Too High')
elif guess < NUMBER:
    print('Too low')
else:
    print('You guess it correct.')
