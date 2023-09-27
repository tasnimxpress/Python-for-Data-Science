import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)>21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    else:
        return sum(cards)

def compare_score(user_score, computer_score):
    if user_score>21 and computer_score>21:
        return "over 21, You lose."
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


def play():
    user_card = []
    computer_card = []

    game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"\nyour card: {user_card}, current score: {user_score}")
        print(f"\ncomputers card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input('\nType "y" to get another card and "n" to pass: ')
            if user_choice == 'y':
                user_card.append(deal_card())
            else:
                game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play()


