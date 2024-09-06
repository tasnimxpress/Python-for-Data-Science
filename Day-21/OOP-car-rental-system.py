"""ABSTRACTION AND ENCAPSULATION
write a program to provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user"""


class Car:
    def __init__(self, listofCar):
        self.carDict = listofCar
        self.carList = [key for key in self.carDict]

    def displayCarList(self):
        print('Our available cars:')
        return [print(i) for i in self.carList]

    def showDetails(self, requestedCar):
        print('\nCar is available')
        print(f'Rent per day ${self.carDict[requestedCar]}')

    def fareDetails(self, requestedCar, num_days):
        total_price = self.carDict[requestedCar] * num_days
        print(f"Please pay: ${total_price}")


class Customer:
    def RequestRentACar(self):
        print('Enter a car name you want to rent: ')
        self.choice = input().capitalize()
        return self.choice

    def agreed(self):
        print("Type 'y' if you agreed to rent: ")
        agreed = input().lower()
        if agreed == 'y':
            return True
        else:
            print('Thank you.')

    def NumDays(self):
        print('Number of days you would like to borrow the car: ')
        self.days = int(input())
        return self.days

    def transactionMade(self):
        print('Please sign the contract. Type "y": ')
        self.contract = input().lower()
        if self.contract == "y":
            return True
        else:
            print('See you soon.')


cars = Car({'Hatchback': 30, 'Sedan': 50, 'SUV': 100})
customer = Customer()


# user menu
while True:
    print('Enter 1 to display the available car.')
    print('Enter 4 to quit the app.')
    user_choice = int(input())
    if user_choice == 1:
        cars.displayCarList()

        chosen_car = customer.RequestRentACar()
        if chosen_car in cars.carList:
            cars.showDetails(chosen_car)
            if customer.agreed() == True:
                num_days = customer.NumDays()
                cars.fareDetails(chosen_car, num_days)
                contract = customer.transactionMade()
                if contract == True:
                    print('You borrowed the car.')

        else:
            print('Car not available')
    else:
        quit()
