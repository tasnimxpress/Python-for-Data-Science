import resource
import random
import os

TURNS = 10
def level(difficulty):
    if difficulty == 'easy':
        return TURNS
    if difficulty == 'hard':
        return TURNS-5

play_again = True
while play_again:
    print(resource.logo)
    print('I am guessing a number between 1 and 100')

    choose_level = input("Choose difficulty level 'easy' or 'hard': \n").lower()

    generate_number = random.randint(1, 100)
    #print(f'number is {generate_number}\n')

    attempt = level(difficulty=choose_level)
    print(f'You have {attempt} attempt')

    last_attempt = False
    while not last_attempt:
        guess = int(input('\nGuess: '))

        if guess == generate_number:
            print(f'You got it. The number was {generate_number}')
            last_attempt = True

        if guess != generate_number:
            attempt -= 1

            if guess > generate_number:
                print(f'Too high\nRemain attempt {attempt}')
            elif guess < generate_number:
                print(f'Too low\nRemain attempt {attempt}')

            if attempt == 0:
                print('\nNo more attempt')
                print(f'The number was {generate_number}')
                last_attempt = True

    user_play_again = input('\nWant to play again? type "yes" or "no": ').lower()
    if user_play_again == 'yes':
        os.system('cls')
    if user_play_again == 'no':
        play_again = False
