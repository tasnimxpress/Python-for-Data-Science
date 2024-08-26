"""Blackjack is a casino banking game.
It is the most widely played casino banking game in the world. It uses decks of 52 cards and descends from a global family of casino banking games known as "twenty-one".
This is a simplified virtual version of Blackjack written in python"""

# Capstone project - Blackjack game
import random
import os


def generate_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def total_score(user_card):
    if 11 in user_card and sum(user_card) > 21:
        user_card.remove(11)
        user_card.append(1)
    if sum(user_card) == 21 and len(user_card) == 2:
        return 0
    return sum(user_card)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    computer_cards = []
    player_cards = []

    for _ in range(2):
        player_cards.append(generate_card())
        computer_cards.append(generate_card())

    play = True
    while play:
        computer_score = total_score(computer_cards)
        player_score = total_score(player_cards)

        print(f"Your card: {player_cards}, current score: {player_score}")
        print(f"computers first hand {computer_cards}\n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            play = False
        else:
            another_card = input(
                "\nType 'y' to get another card, 'p' to pass it: ").lower()
            if another_card == 'y':
                player_cards.append(generate_card())
            else:
                play = False

        while computer_score < 16 and computer_score != 0:
            computer_cards.append(generate_card())
            computer_score = total_score(computer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {
          computer_cards}, final score: {computer_score}\n")
    print(compare(player_score, computer_score))


while input(
        "Type 'y' to play blackjack game: ").lower() == 'y':
    os.system('cls')
    blackjack()
