"""
Fizz buzz is a group word game for children to teach them about division.
Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", 
and any number divisible by five with the word "buzz", 
and any number divisible by both three and five with the word "fizzbuzz".
"""
numbers = []
for number in range(1, 101):
    numbers.append(number)
    # print(numbers)

# print(numbers)

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    else:
        number

    print(number)
