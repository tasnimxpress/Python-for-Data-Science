# Capstone project - Higher Lower game

"""
The objective is simple: guess which of the two cards shown is higher. 
If you get the answer correct, a new card will appear and simply guess again which you think is higher. 
Every game has infinite questions so try your best to get a high score streak."""

# 'name': 'Instagram',
# 'follower_count': 346,
# 'description': 'Social media platform',
# 'country': 'United States'

import random
from art import vs, logo
from Game_data import data


card1 = random.choice(data)
card2 = random.choice(data)

print(f'{card1['name']}, {card1['description']}, from {
    card1['country']}, has {card1['follower_count']} million follower.')

print(vs)
print(f'{card2['name']}, {card2['description']}, from {
    card2['country']}')

guess = input(f'\nWho has more follower? Type "A" or "B": ').lower()


if guess == 'a' and card1['follower_count'] > card2['follower_count']:
    print('Correct')
else:
    print('You lose')
