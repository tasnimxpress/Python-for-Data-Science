import resource
import random
import os

TURNS = 10
def level(difficulty):
    if difficulty == 'easy':
        return TURNS
    if difficulty == 'hard':
        return TURNS-5

def compare_number(guess_num, actual_num):
    if guess_num > actual_num:
        print(f'Too high')
    elif guess_num < actual_num:
        print(f'Too low')
    else:
        print(f'You got it. The number was {actual_num}')

play_again = True
while play_again:
    print(resource.logo)
    generate_number = random.randint(1, 100)
    print('I am guessing a number between 1 and 100')
    choose_level = input("Choose difficulty level 'easy' or 'hard': \n").lower()

    attempt = level(difficulty=choose_level)
    print(f'You have {attempt} attempt')

    last_attempt = False
    while not last_attempt:
        guess = int(input('\nGuess: '))
        compare_number(guess, generate_number)
        if guess == generate_number:
            last_attempt = True

        if guess != generate_number:
            attempt -= 1
            print(f'Remain attempt {attempt}')

            if attempt == 0:
                print('\nNo more attempt')
                print(f'The number was {generate_number}')
                last_attempt = True

    user_play_again = input('\nWant to play again? type "yes" or "no": ').lower()
    if user_play_again == 'yes':
        os.system('cls')
    if user_play_again == 'no':
        play_again = False
