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


class SavingsAccount(Account):
    def __init__(self):
        self.AccountDetails = {}

    def createAccount(self, name, deposit):
        self.accountNumber = random.randint(10000, 99999)
        self.AccountDetails[self.accountNumber] = [name, deposit]
        print(f'\nAccount has been created, account number: {
              self.accountNumber}\n')

    def authenticate(self, name, accountNumber):
        if accountNumber in self.AccountDetails.keys():
            if self.AccountDetails[accountNumber][0] == name:
                print('\nAuthentication successfull.\n')
                self.accountNumber = accountNumber
                return True
        else:
            print('\nAuthentication Failed.\n')
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.AccountDetails[self.accountNumber][1]:
            print('\nInsufficient Balance.')
        else:
            self.AccountDetails[self.accountNumber][1] -= withdrawalAmount
            print(f'\nCashout successfull.')
            self.displayBalance()

    def deposit(self, depositAmount):
        self.AccountDetails[self.accountNumber][1] += depositAmount
        print(f'\nDeposit successfull.')
        self.displayBalance()

    def displayBalance(self):
        print(f'\nAvailable balance: {
              self.AccountDetails[self.accountNumber][1]}')


account = SavingsAccount()


# user menu
while True:
    print('Type 1 to create a new account.\nType 2 to log in an existing account\nType 3 to close the app: ')
    choice = int(input())

    if choice == 1:
        user_name = input('\nEnter your name: ')
        deposit = int(input('Enter your deposit amount: '))
        account.createAccount(user_name, deposit)
    elif choice == 2:
        name = input('\nEnter your user name: ')
        pin = int(input('Enter your pin: '))
        authentication = account.authenticate(name, pin)

        if authentication is True:
            while True:
                print(
                    '\nType 1 to deposit.\nType 2 to withdraw.\nType 3 to see available balance.\nType 4 to log out: ')
                user_choice = int(input())
                if user_choice == 1:
                    depositAmount = int(input('\nEnter deposit amount: '))
                    account.deposit(depositAmount)
                elif user_choice == 2:
                    cashoutAmount = int(input('\nEnter withdrawal amount: '))
                    account.withdraw(cashoutAmount)
                elif user_choice == 3:
                    account.displayBalance()
                elif user_choice == 4:
                    break
    elif choice == 3:
        quit()
