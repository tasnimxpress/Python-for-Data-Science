"Calculator"

# functions to add, subtract, multiply, divide


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


symbols = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

n1 = float(input('Enter first number: '))
for key in symbols:
    print(key)
operation = input(f'Pick an operation from above: ')
n2 = float(input('Enter second number: '))


calculation = symbols[operation]
answer = calculation(n1, n2)
print(f'{n1} {operation} {n2} = {answer}')
