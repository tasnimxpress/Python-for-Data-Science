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


def format_data(card):
    name = card['name']
    description = card['description']
    card_country = card['country']
    return (f'{name}, {description}, from {card_country}.')


def random_card():
    card = random.choice(data)
    return card


def check_answer(card1_follower, card2_follower):
    if card1_follower > card2_follower:
        return True
    else:
        return False


should_continue = True
while should_continue:
    SCORE = 0
    print(f"{logo}\nWelcome to the Higher Lower game.\n")

    card_a = random_card()
    card_b = random_card()

    card_a_follower = card_a['follower_count']
    card_b_follower = card_b['follower_count']

    game_on = True
    while game_on:
        if card_a_follower == card_b_follower:
            card_b = random_card()
        print(f'Compare A: {format_data(card_a)}.')
        print(vs)
        print(f'Against B: {format_data(card_b)}.')

        guess = input(f'\nWho has more follower? Type "A" or "B": ').lower()

        if (check_answer(card_a_follower, card_b_follower) is True and guess == 'a') or (check_answer(card_a_follower, card_b_follower) is False and guess == 'b'):
            print('Correct')
            time.sleep(1)
            os.system('cls')
            card_a = card_b
            card_b = random_card()
            SCORE += 1
            print(f"You're right. Current score: {SCORE}")

        else:
            os.system('cls')
            print(f'Sorry, Thats wrong. Final score: {SCORE}')
            game_on = False

    play_again = input('\nType "y" to play again, "n" to close: ')
    os.system('cls')
    if play_again == 'n':
        print('Goodbye')
        should_continue = False
