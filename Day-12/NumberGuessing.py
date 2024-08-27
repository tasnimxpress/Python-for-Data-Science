"Flowchart is available in the current folder"
import random

LIFE = 10
NUMBER = random.randint(1, 100)


def attempt(difficulty_level):
    if difficulty_level == 'hard':
        return LIFE - 5
    else:
        return LIFE


def lives(Number, guess, turns):
    if Number != guess:
        return turns - 1


def is_correct(Number, guess):
    if guess > Number:
        print('Too High')
    elif guess < Number:
        print('Too low')
    else:
        print(f'You guess it correct. Number was {Number}')


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choose_level = input('\nChoose a Game level- Easy or Hard: ').lower()

    game_on = True
    current_attempt = attempt(choose_level)

    while game_on:

        print(f'You have {current_attempt} attempts')
        guess = int(input('\nEnter your guess: '))
        life = lives(NUMBER, guess, current_attempt)

        current_attempt = life
        is_correct(NUMBER, guess)

        if current_attempt == 0:
            game_on = False
            print(f'\nYou are out of life. Number was {NUMBER}')
        if NUMBER == guess:
            game_on = False
        elif life != 0:
            print('Guess again')


while input('\nType "y" to play number guessing game: ') == 'y':
    game()
