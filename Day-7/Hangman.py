"""
Hangman is a guessing game for two or more players.
One player thinks of a word, phrase, or sentence and the other(s) tries to guess it
by suggesting letters or numbers within a certain number of guesses.
Originally a paper-and-pencil game, this is a virtual version of the game where you will play with computer generated word."""


# For & while loop, if-else, list, string, range
import random
from re import L
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ['test', 'exam', 'bee']
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
limit = len(display)

lives = len(stages)
end_game = False
while not end_game:
    guess = input('Enter your guess: ').lower()
    limit -= 1

    for letter in range(0, word_length):

        if guess in chosen_word[letter]:
            display[letter] = guess

        if guess not in chosen_word[letter]:
            lives -= 1
            print('You lost one life.')
            print(stages[lives])

    print(display)

    if "_" not in display:
        end_game = True
        print('You win')
    else:
        print('You lost')
