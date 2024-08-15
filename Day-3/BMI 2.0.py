"""
This program will calculate BMI using customer input - 
weight and height 
and then it will interpret the condition of their BMI based on the BMI value.
"""

Greeting = 'Welcome to the BMI calculator.'

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in meter: '))

BMI = round(weight / (height * height), 2)

# print(f'Your BMI is {BMI}')

if BMI > 35:
    print(f"your BMI is {BMI} and your are clinically obese.")
elif 35 >= BMI > 30:
    print(f"your BMI is {BMI} and your are obese.")
elif 30 >= BMI > 25:
    print(f"your BMI is {BMI} and your are slightly overweight.")
elif 25 >= BMI > 18.5:
    print(f"your BMI is {BMI} and your are normal weight.")
else:
    print(f"your BMI is {BMI} and your are underweight.")
