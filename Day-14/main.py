# Capstone project - Higher Lower game

"""
The objective is simple: guess which of the two cards shown is higher. 
If you get the answer correct, a new card will appear and simply guess again which you think is higher. 
Every game has infinite questions so try your best to get a high score streak."""

import random
import time
import os
from art import vs, logo
from Game_data import data


def random_card():
    card = random.choice(data)
    return card


def check_answer(card1_follower, card2_follower):
    if card1_follower > card2_follower:
        return True
    else:
        return False


SCORE = 0


should_continue = True
while should_continue:
    print(f"{logo}\nWelcome to the Higher Lower game.\n")

    card1 = random_card()
    card2 = random_card()

    if card1['follower_count'] == card2['follower_count']:
        card2 = random_card()

    game_on = True
    while game_on:
        print(f'Compare A: {card1['name']}, {card1['description']}, from {
            card1['country']}.')

        print(vs)

        print(f'Against B: {card2['name']}, {card2['description']}, from {
            card2['country']}.')

        guess = input(f'\nWho has more follower? Type "A" or "B": ').lower()

        card1_follower = card1['follower_count']
        card2_follower = card2['follower_count']

        if (check_answer(card1_follower, card2_follower) is True and guess == 'a') or (check_answer(card1_follower, card2_follower) is False and guess == 'b'):
            print('Correct')
            time.sleep(1)
            os.system('cls')
            card1 = card2
            card2 = random_card()
            if card1['follower_count'] == card2['follower_count']:
                card2 = random_card()
            SCORE += 1

        else:
            print('You lose')
            print(f'Final score: {SCORE}')
            game_on = False

    play_again = input('\nType "y" to play again, "n" to close: ')
    os.system('cls')
    if play_again == 'n':
        print('Goodbye')
        should_continue = False
