# Start Project here
# choice generate string
# sample generate list

import os
import random
import words
import lives

live = len(lives.lives)-1
print(lives.logo)
print(lives.lives[6])

# generate a random word
generate_word = random.choice(words.word_list)
print(generate_word)

# make word blank
blank = []
length = len(generate_word)
for index in range(0, length):
    blank += '_'
print(f"{' '.join(blank)}")

end = False
while not end:
    # make user guess
    guess = input('Guess: ').lower()
    os.system('cls')

    if guess in blank:
        print('You already guessed this letter.\n')
    # fill blank with guess
    for index in range(length):
        letter = generate_word[index]
        if letter == guess:
            blank[index] = letter

    #print(f"{' '.join(blank)}")
    if guess not in generate_word:
        live -= 1
        show = len(lives.lives) - (live+1)
        print(f"You guessed {guess} and it's not in the word.\nYou lose {show} live. Remain {live}\n{lives.lives[live]}")
    if live == 0:
        end = True
        print('You lose')
    print(f"{' '.join(blank)}")
    if '_' not in blank:
        end = True
        print('You win')
