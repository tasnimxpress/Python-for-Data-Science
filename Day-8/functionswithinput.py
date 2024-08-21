"Functions with input, arguments, parameters"

# function


def greet():
    for n in range(3):
        print('Hello')


greet()

# function with input


def greet_with_name(name):
    print(f'How are you, {name}?')


greet_with_name('tasnim')

# functions with more than 1 input


def greet_with(name, location):
    print(f'How are you {name}?')
    print(f'How much do you know about {location}?')


# Positional argumrnt
greet_with('tasnim', 'dhaka')
# Keyword argument
greet_with(location='Dhaka', name='Tasnim')
