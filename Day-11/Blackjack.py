"""Blackjack is a casino banking game.
It is the most widely played casino banking game in the world. It uses decks of 52 cards and descends from a global family of casino banking games known as "twenty-one".
This is a simplified virtual version of Blackjack written in python"""

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    card = []
    for n in range(2):
        card.append(n)
        n = random.choice(cards)
    return card


def total_score(user):
    score = 0
    for i in range(len(user)):
        card_number = user[i]
        score += card_number
    return score


computer = random_card()
player = random_card()

print(f"computers first card {computer}, {total_score(computer)}")
print(f"Your card: {player}, current score: {total_score(player)}")

another_card = input("\nType 'y' to get another card, 'n' to pass it: ")
# print(computer_card)


# print(player_card)
