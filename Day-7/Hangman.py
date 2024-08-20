"""
Hangman is a guessing game for two or more players.
One player thinks of a word, phrase, or sentence and the other(s) tries to guess it
by suggesting letters or numbers within a certain number of guesses.
Originally a paper-and-pencil game, this is a virtual version of the game where you will play with computer generated word."""


# For & while loop, if-else, list, string, range, module
import random
from Hangman_art import stages
from word_list import random_words

word_list = ['test', 'exam', 'bee']
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append(letter)

# print(display)

for i in range(len(display)):
    display[i] = '_'

print(display)

word_length = len(chosen_word)
lives = len(stages)

end_game = False
while not end_game:
    guess = input('Enter your guess: ').lower()
    # lives += lives
    for letter in range(0, word_length):
        if guess in chosen_word[letter]:
            display[letter] = guess

    if guess not in chosen_word:
        print(f"You lost  live. remaining life {lives - 1}\n{stages[lives-1]}")
        lives -= 1
        if lives == 0:
            end_game = True
            print('You lost')

    print(display)

    if "_" not in display:
        end_game = True
        if "_" not in display:
            print(f"{''.join(display)}\n'You win'")
