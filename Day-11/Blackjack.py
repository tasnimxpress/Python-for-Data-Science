"""Blackjack is a casino banking game.
It is the most widely played casino banking game in the world. It uses decks of 52 cards and descends from a global family of casino banking games known as "twenty-one".
This is a simplified virtual version of Blackjack written in python"""

# Capstone project - Blackjack game
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_card(card_list):
    n = random.choice(cards)
    card_list.append(n)
    return card_list


def total_score(user):
    score = 0
    for i in range(len(user)):
        card_number = user[i]
        score += card_number
    return score


def blackjack(user):
    if total_score(user) == 21:
        return True
    else:
        return False


def ace(user):
    if cards[0] in user:
        return True
    else:
        return False


def ace_count(user):
    if ace(user) == True:
        if total_score(user) >= 21:
            cards[0] = 1
        else:
            cards[0]
    return total_score(user)


play_again = True
while play_again:
    computer = []
    for i in range(2):
        generate_card(computer)

    player = []
    for i in range(2):
        generate_card(player)

    computer_score = total_score(computer)
    player_score = total_score(player)

    should_continue = True
    while should_continue:
        print(f"\ncomputers first card {computer}: {computer_score}")
        print(f"Your card: {player}, current score: {player_score}\n")

        another_card = input(
            "\nType 'y' to get another card, 'p' to pass it: ").lower()
        if another_card == 'y':
            card = generate_card(player)

        if ace(player) == True:
            ace_count(player)

        if ace(computer) == True:
            ace_count(computer)

        computer_score = total_score(computer)
        player_score = total_score(player)

        if blackjack(computer) == True:
            should_continue = False
            print('You lose')

        elif blackjack(player) == True:
            should_continue = False
            print('You win')

        elif computer_score < 16:
            card = generate_card(computer)

        elif another_card == 'p':
            should_continue = False

        print(f"\ncomputers first card {computer}, {computer_score}")
        print(f"Your card: {player}, current score: {player_score}\n")

    if player_score > 21:
        print('You lose')
    elif player_score == computer_score:
        print('Draw')
    elif computer_score < player_score < 21:
        print('You win')
    elif computer_score > 21 and player_score <= 21:
        print('Your win')
    else:
        print('you lose')

    new_game = input(
        "press 'n' to stop. Type any other key if you want to start a new game: ").lower()
    if new_game == 'n':
        play_again = False
