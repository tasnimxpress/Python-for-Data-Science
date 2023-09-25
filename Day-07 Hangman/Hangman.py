# Start Project here
# choice generate string
# sample generate list

import os
import random
import words
import lives

print(lives.logo)

restart = True
while restart:
    remain_live = len(lives.stage) - 1
    choose_level = input(f"{lives.stage[10]}\nHey! Good luck, Keep me alive. Don't loose.\nChoose level:\nType 'beginner' or 'advanced':\n").lower()

    # generate a random word
    generate_word = ''
    if choose_level == 'beginner':
        generate_word = random.choice(words.beginner)
    elif choose_level == 'advanced':
        generate_word = random.choice(words.advanced)
    else:
        choose_level = input(f"Choose right level to play.\nType 'beginner' or 'advanced': \n").lower()
        if choose_level == 'beginner':
            generate_word = random.choice(words.beginner)
        elif choose_level == 'advanced':
            generate_word = random.choice(words.advanced)

    #print(generate_word)

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

        if guess not in generate_word:
            remain_live -= 1
            show = len(lives.stage) - (remain_live+1)
            print(f"You guessed {guess} and it's not in the word.\nYou lose {show} live. Remain {remain_live}\n{lives.stage[remain_live]}")

        print(f"{' '.join(blank)}")

        if remain_live == 0:
            end = True
            print(f'You lose\nThe word was {generate_word}')


        if '_' not in blank:
            end = True
            print(f'{lives.win}\nYou win')

    play_again = input('Want to play again? Type "yes" or "no":\n').lower()

    if play_again == 'no':
        print("Don't forget to come again")
        restart = False
