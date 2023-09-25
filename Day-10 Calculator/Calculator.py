def addition(a, b):
    x = a + b
    return x

def subtraction(a, b):
    x = a - b
    return x

def multiplication(a, b):
    x = a * b
    return x

def division(a, b):
    x = a / b
    return x

def power(a, b):
    x = a**b
    return x


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": power
}

def calculator():
    input_a = float(input('\nenter a number: '))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        symbol = input('Choose operation: ')
        input_b = float(input('Enter next number: '))
        calculation_function = operations[symbol]
        answer = calculation_function(input_a, input_b)

        print(f"\n{input_a} {symbol} {input_b} = {answer}\n")

        choose_rerun = input(f'To calculate with {answer} type "yes", "no" to start new: ')
        if choose_rerun == "yes":
            input_a = answer

        if choose_rerun == "no":
            should_continue = False
            calculator()

calculator()

