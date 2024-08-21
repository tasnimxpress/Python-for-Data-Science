import math
"Functions with input, arguments, parameters"

# # function


# from math import ceil, floor


# def greet():
#     for n in range(3):
#         print('Hello')


# greet()

# # function with input


# def greet_with_name(name):
#     print(f'How are you, {name}?')


# greet_with_name('tasnim')

# # functions with more than 1 input


# def greet_with(name, location):
#     print(f'How are you {name}?')
#     print(f'How much do you know about {location}?')


# # Positional argumrnt
# greet_with('tasnim', 'dhaka')
# # Keyword argument
# greet_with(location='Dhaka', name='Tasnim')


# # function in practice


# def paint_calc(height, width, cover):
#     total_can = ceil((height * width) / cover)
#     print(f'You need {total_can} cans of paint.')


# test_h = int(input('Enter height: '))
# test_w = int(input('Enter widht: '))
# coverage = 5
# paint_calc(test_h, test_w, coverage)


# Is Prime number
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')


num = int(input('Enter number: '))
prime_checker(num)
