# class write in Pascal Case
# MyClass or HelloWorld or ClassName


#creating class
class Atm:
    #constructor (__init__(self) special function)
    #constructor do not need to call to execute.
    #it executes automatically when we create objects under the class
    #write function or variables inside constructor in the class
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input('''
        1. press 1 create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. exit
        ''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin
        user_balance = int(input('Enter your balance: '))
        self.balance = user_balance
        print('\nPin creation successful')
        self.menu()

    def change_pin(self):
        old_pin = input('Enter your current pin: ')
        if old_pin == self.pin:
            pin_update = input('Enter your new pin: ')
            self.pin = pin_update
            print('Pin update successful')
        else:
            print('Pin does not match.')
        self.menu()

    def check_balance(self):
        enter_pin = input('Enter your pin: ')
        if enter_pin == self.pin:
            print(f"Current balance: {self.balance} Taka")
        else:
            print('Pin does not match')
        self.menu()

    def withdraw(self):
        enter_pin = input('Enter your pin: ')
        if enter_pin == self.pin:
            balance_withdraw = int(input('Enter amount to withdraw: '))
            if self.balance >= balance_withdraw:
                update_balance = self.balance - balance_withdraw
                self.balance = update_balance
                print(f"Cash out {balance_withdraw} Taka")
            else:
                print('Insufficient money')
        else:
            print('Pin does not match')
        self.menu()

#class itself does not give any output unless it has any object.
#object access the class(set of rules).

#creating object
Machine = Atm()
