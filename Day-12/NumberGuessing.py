"Flowchart is available in the current folder"
import random

LIFE = 10
NUMBER = random.randint(1, 100)


def attempt(difficulty_level):
    if difficulty_level == 'hard':
        return LIFE - 5
    else:
        return LIFE


print(NUMBER)

choose_level = input('Choose a Game level- Easy or Hard: ').lower()

game_on = True

while game_on:
    current_attempt = attempt(choose_level)
    print(f'You have {current_attempt} attempts')
    guess = int(input('\nEnter your guess: '))

    if current_attempt == 0:
        game_on = False


if guess > NUMBER:
    print('Too High')
elif guess < NUMBER:
    print('Too low')
else:
    print('You guess it correct.')
