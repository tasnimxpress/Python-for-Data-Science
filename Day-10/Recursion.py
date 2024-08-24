"Factorial Function"


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number*factorial(number - 1)


num = int(input('Enter number: '))
print(factorial(num))


# Fibonacchi series

def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


nth_number = int(input('Enter nth number: '))

for i in range(nth_number):
    print(fib(i))
