"""
1. Give a prompt to the user asking if:
    * they wish to create a new savings account
    * or access an existing one.
2. if the user would like to create a new account,
    * then accept their name and initial deposit,
    * and create a 5 digit random number
    * and make it as the account number of their new savings account.
3. if they are accessing an existing account:
    * accept their name and account number to validate the user
    * give them options to:
            * withdraw,
            * deposit or
            * display their available balance.
"""

import random
import csv
import pandas as pd
PATH = "E:/GitHub/100DaysOfPython/Day-23/AccountDetails.csv"


class Bank:
    def __init__(self):
        self.initialBalance = 0
        self.details = []
        self.data = pd.DataFrame(self.details)
        self.csv = self.data.to_csv(PATH)

    def createAccount(self, name, deposit):
        num = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=5)
        pin = int(''.join(map(str, num)))
        self.initialBalance += deposit
        with open(PATH, 'a', newline='') as file:
            raw = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            raw.writerow([{pin}, {deposit}, {name}])
            self.details.append(raw)
            print(raw)

        # account = {'pin': pin,
        #            'name': name,
        #            'balance': deposit}

        # self.details.append(account)
        # # self.data.loc[2.5] = 30.0, 1.3
        # self.data.loc[-1] = pin, name, deposit
        # self.data = self.data.sort_index().reset_index(drop=True)

        # self.data = pd.DataFrame(self.details)
        # self.csv = self.data.to_csv(PATH)
        # return self.data

    def userData(self):
        # self.csv = self.data.to_csv(PATH)
        print(self.data)

    def displayDetails(self):
        # df = pd.DataFrame(self.details)
        print(self.details)


class customer:
    pass


bank = Bank()
print(bank.details)


# user menu
bankOpen = True
while bankOpen:
    print('Type 1 to create a new account.\nType 2 to log in an existing account: ')
    choice = int(input())

    if choice == 1:
        user_name = input('Enter your name: ')
        deposit = int(input('Enter your deposit amount: '))
        bank.createAccount(user_name, deposit)
    elif choice == 2:
        print(bank.displayDetails())
