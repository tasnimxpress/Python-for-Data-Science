"""
This program will calculate your love score with your partner.
Based on how many times TRUE LOVE occurrs in your name."""

name1 = input('Enter your name: ')
name2 = input('Enter name with whom you want to know your score: ')

NAME = (name1 + name2).lower()

# print(NAME)

t = NAME.count('t')
r = NAME.count('r')
u = NAME.count('u')
e = NAME.count('e')
l = NAME.count('l')
o = NAME.count('o')
v = NAME.count('v')

true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
