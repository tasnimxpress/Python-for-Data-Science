# With dictionary
import os

bidders = {}

def highest_bidder():
    highest_bid = 0
    winner = ''
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f'Winner is {winner}')

running = True
while running:
    name = input('name: \n')
    price = int(input('price: \n$'))
    bidders[name]=price
    user = input('more user? "yes" or "no": ')

    if user == 'yes':
        os.system('cls')

    if user == 'no':
        highest_bidder()
        running = False