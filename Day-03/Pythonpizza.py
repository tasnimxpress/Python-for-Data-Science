"""
This is a automatic pizza billing system. 
Based on users preference it will calculate final bill."""

Greeting = 'Thank you for choosint python pizza delivery.'
size = input('What size pizza do you want? s/ m/ l: ')

if size == "s":
    BILL = 15
elif size == "m":
    BILL = 20
else:
    BILL = 25


if size == 's' or size == 'm' or size == 'l':
    extra_cheese = input('Do you want extra cheese? y or n: ')
    extra_pepparoni = input('Do you want extra pepparoni? y or n: ')

    if extra_pepparoni == 'y':
        if size == 's':
            BILL += 2
        else:
            BILL += 3

    if extra_cheese == "y":
        BILL += 1

    print(f'{Greeting}\nPay bill ${BILL}')

else:
    print("We don't offer this size pizza. We have small, medium and large.")
