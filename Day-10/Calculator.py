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

is_working = True
while is_working:
    n1 = float(input('Enter first number: '))
    for key in symbols:
        print(key)
    operation = input(f'Pick an operation from above: ')
    n2 = float(input('Enter second number: '))

    calculation = symbols[operation]
    answer = calculation(n1, n2)
    print(f'{n1} {operation} {n2} = {answer}')

    calculate_again = input(
        '\nType "y" to start a new calculation.\nType "a" to calculate with previous answer\nType "n" to close the calculator\n: ')
    if calculate_again == 'a':
        operation = input(f'Pick another operation: ')
        n3 = float(input('Enter third number: '))
        calculate_with_answer = symbols[operation]
        with_answer = calculate_with_answer(answer, n3)
        answer = with_answer
        print(answer)

    calculate_again = input(
        '\nType "y" to start a new calculation.\nType "a" to calculate with previous answer\nType "n" to close the calculator\n: ')

    if calculate_again == 'n':
        is_working = False
