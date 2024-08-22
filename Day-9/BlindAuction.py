"""
A first-price sealed-bid auction (FPSBA) is a common type of auction. It is also known as blind auction. 
In this type of auction, all bidders simultaneously submit sealed bids so that no bidder knows the bid of any other participant. 
The highest bidder pays the price that was submitted."""

import os
import time
from auctionlogo import logo, Winner_logo

bidders = {}

auction_continue = True
while auction_continue:
    print(f'{logo}\nWelcome to the Blind Auction.\n')
    name = input('Enter your name: ')
    bid = int(input('Enter your bid: $'))

    bidders[name] = bid

    os.system('cls')
    users = input(
        "Is there any other bidder? \nType 'Y' for yes, 'N' to close the auction: \n").lower()
    time.sleep(1)
    os.system('cls')

    if users == 'n':
        auction_continue = False
        print('Bidding is closed.\nWe are analyzing the bids.')

        time.sleep(3)
        # print(bidders)


def result(bidding_record):
    highest_bidder = 0
    winner = {}
    for key in bidding_record:
        if bidding_record[key] > highest_bidder:
            highest_bidder = bidding_record[key]
            winner['Name'] = key
            winner['Bid'] = bidding_record[key]

    print(f'\nWe got the result.\n{Winner_logo}:\nThe winner is {
        winner["Name"]} with a bid of ${winner['Bid']}')


result(bidders)
