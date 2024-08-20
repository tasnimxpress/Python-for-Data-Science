"""
Hangman is a guessing game for two or more players. 
One player thinks of a word, phrase, or sentence and the other(s) tries to guess it 
by suggesting letters or numbers within a certain number of guesses. 
Originally a paper-and-pencil game, this is a virtual version of the game where you will play with computer generated word."""


# For & while loop, if-else, list, string, range

import random

word_list = ['test', 'exam', 'below']
chosen_word = random.choice(word_list)

print(chosen_word)

guess = input('Enter your guess: ').lower()
