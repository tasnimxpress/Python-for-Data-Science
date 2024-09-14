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

from abc import ABCMeta, abstractmethod
import random
import csv
import pandas as pd
PATH = "E:/GitHub/100DaysOfPython/Day-23/AccountDetails.csv"


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class Bank:
    def __init__(self):
        self.initialBalance = 0
        self.details = {}
        self.data = pd.DataFrame(self.details)
        self.csv = self.data.to_csv(PATH)

    def createAccount(self, name, deposit):
        pin = random.randint(10000, 99999)
        self.details[pin] = [name, deposit]

    def authenticate(name, accountNumber):
        pass

    def withdraw(self, amount):
        pass

    def deposti(self, amount):
        pass

    def displayBalance(self):
        pass


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
