"""
This program will check if a person is eligible to take a ride in rollercoster.
The conditions to eligibility is - Height over 120 contimeter.
Also, if they are eligible then we should check their age.
1. If they are above 18 then pay adult bill.
2. If they are below 18 then pay kids bill.
3. if they are between 12 and 18 then pay teenage bill.
"""

HEIGHT = 120
PHOTO_PRICE = 3

customer_height = int(input("Enter your height in centimeter: "))

if customer_height >= HEIGHT:
    age = int(input('Enter your age: '))

    if 12 <= age <= 18:
        BILL = 12

    elif 45 <= age <= 55:
        BILL = 0
        print('Everything will be fine, have a free ride with us.')

    elif age < 18:
        BILL = 7

    else:
        BILL = 20

    want_photo = input('Do you want photo? y or n: ')
    if want_photo == 'y':
        BILL += PHOTO_PRICE

    print(f'Please Pay ${BILL}')

else:
    print('Sorry, you have to grow taller.')
