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
