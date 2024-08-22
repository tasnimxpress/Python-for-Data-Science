"""
A first-price sealed-bid auction (FPSBA) is a common type of auction. It is also known as blind auction. 
In this type of auction, all bidders simultaneously submit sealed bids so that no bidder knows the bid of any other participant. 
The highest bidder pays the price that was submitted."""

import os
bidders = {}

auction_continue = True
while auction_continue:
    name = input('Enter your name: ')
    bid = int(input('Enter your bid: $'))

    bidders[name] = bid

    os.system('cls')
    users = input(
        "Is there any other bidder? \nType 'Y' for yes, 'N' to close the auction: \n").lower()
    os.system('cls')

    if users == 'n':
        auction_continue = False
        print('We are closing the auction.\n')

        # print(bidders)

highest_bidder = 0
winner = {}
for key in bidders:
    if bidders[key] > highest_bidder:
        highest_bidder = bidders[key]
        winner['Name'] = key
        winner['Bid'] = bidders[key]

print(f'The winner is {winner["Name"]} with a bid of ${winner['Bid']}.')
