# Who has higher follower?

import random
import resources
from game_data import data
import os

def format_account(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['description']
    country = account['country']
    # follower = account['follower_count']
    return f'{name}, a {description}, from {country}'


def check(a_follower, b_follower, guess):
    """Checks followers against user's guess
      and returns True if they got it right.
      Or False if they got it wrong."""
    if a_follower['follower_count'] > b_follower['follower_count'] and guess == 'a':
        return True
    elif b_follower['follower_count'] > a_follower['follower_count'] and guess == 'b':
        return True
    else:
        return False

# generate random account from the game data
play = True
while play:
    # display art
    print(resources.logo)

    right = True
    current_score = 0
    account_b = random.choice(data)

    while right:
        account_a = account_b
        account_b = random.choice(data)

        if account_a == account_b:
            account_b = random.choice(data)

        #format the data into printable format
        a = 'Account A: '+ format_account(account_a)
        print(a)
        print(resources.vs)
        b = 'Account B: '+ format_account(account_b)
        print(b)

        #ask user for a guess
        user_guess = input("\nWhich account has more follower? Type 'a' or 'b': \n").lower()

        #check if user is right
        is_correct = check(account_a, account_b, user_guess)

        #track score
        score = 0
        if is_correct:
            score += 1
            current_score += score
            os.system('cls')
            print(f'Right. Current score: {current_score}\n')

        if not is_correct:
            os.system('cls')
            print('Wrong')
            print(f'\nFinal score: {current_score}\n')
            right = False

    play_again = input('Want to play again? "yes" or "no": \n').lower()
    if play_again == 'yes':
        os.system('cls')
    if play_again == 'no':
        play = False
