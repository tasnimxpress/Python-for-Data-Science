# dictionary within List (nested dictionary)
import os

bidders = []

def new_bidder(name, bid):
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bidders.append(bidder)

def find_highest_bidder():
    winner = max(bidders, key=lambda x: x['bid'])
    print(f"Winner is {winner['name']}")

restart = True
while restart:

    user_name = input("what's your name?\n")
    bid_amount = int(input("enter your bid amount:\n"))
    new_bidder(name=user_name, bid=bid_amount)

    new_user = input("is there any new user? Type 'yes' or 'no':\n")

    if new_user == 'yes':
        os.system('cls')
    if new_user == 'no':
        find_highest_bidder()
        restart = False
