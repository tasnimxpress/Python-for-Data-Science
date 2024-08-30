# Capstone project - Hangman
"""
Hangman is a guessing game for two or more players.
One player thinks of a word, phrase, or sentence and the other(s) tries to guess it
by suggesting letters or numbers within a certain number of guesses.
Originally a paper-and-pencil game, this is a virtual version of the game where you will play with computer generated word."""


import random
from Hangman_art import stages, logo
from word_list import random_words

print(f"{logo}\nWelcome to the game.\n\nGuess the word.")

chosen_word = random.choice(random_words)
# print(chosen_word)


display = []
for letter in chosen_word:
    display.append(letter)

# print(display)

for i in range(len(display)):
    display[i] = '_'

print(display)

word_length = len(chosen_word)
lives = len(stages)
guess_list = []


end_game = False
while not end_game:
    guess = input('\nEnter your guess: ').lower()

    if guess in guess_list:
        print("\nYou've already guessed it")

    for letter in range(0, word_length):
        if guess in chosen_word[letter]:
            display[letter] = guess

    print(display)

    if (guess not in chosen_word) and (guess not in guess_list):
        print(
            f"\n{stages[lives-1]}\nYou guessed {guess}, Thats not in the word.\nYou lost a live. Remaining life {lives - 1}.\n")
        lives -= 1

        if lives == 0:
            end_game = True
            print(f'\nYou lost.\nWord is: {chosen_word}')

    guess_list.append(guess)

    if "_" not in display:
        end_game = True
        print(f"\nYou win\nWord is: {''.join(display)}")
