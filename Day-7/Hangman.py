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

display = []
for letter in chosen_word:
    display.append(letter)
print(display)

for i in range(len(display)):
    display[i] = '_'

print(display)
word_length = len(chosen_word)
limit = len(chosen_word)

while limit > 0:
    guess = input('Enter your guess: ').lower()
    limit -= 1

    for letter in range(0, word_length):
        if guess in chosen_word[letter]:
            display[letter] = guess
    print(display)
    # else:
    #     print('false')
