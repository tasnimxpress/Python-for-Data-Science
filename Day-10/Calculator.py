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

n1 = float(input('First number: '))
for key in symbols:
    print(key)
operation = input(f'Which operation you want to do: ')
n2 = float(input('second number: '))


calculation = symbols[operation]
print(calculation(n1, n2))
