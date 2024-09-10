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


class Bank:
    def __init__(self):
        self.initialBalance = 0

    def createAccount(self, name, deposit):
        self.initialBalance += deposit
        with open('E:/GitHub/100DaysOfPython/Day-23/AccountDetails.csv', 'w') as acc:
            details = acc.write(f"'name': {name}, 'balance': {
                                self.initialBalance}")
            return details

    def displayDetails(self):
        # self.createAccount(name='name', deposit=self.initialBalance)
        with open('E:/GitHub/100DaysOfPython/Day-23/AccountDetails.csv', 'r') as acc:
            print(acc.read())


class customer:
    pass


bank = Bank()
# user menu
print('Type 1 to create a new account.\nType 2 to log in an existing account: ')
choice = int(input())

if choice == 1:
    user_name = input('Enter your name: ')
    deposit = int(input('Enter your deposit amount: '))
    bank.createAccount(user_name, deposit)
elif choice == 2:
    bank.displayDetails()
