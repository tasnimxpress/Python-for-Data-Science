#  Tip calculator
# * take input from user : 
#     * total Bill, 
#     * total people, 
#     * tip percentage
# * print how much each person should pay.

print('Welcome to the tip calculator.')

bill_1 = input('What is the total bill? ')
bill_2 = bill_1.strip('$')
total_bill = float(bill_2)
number_of_people = int(input('How many people to split the bill? '))
tip_1 = input('what percentage tip would you like to give? ')
tip_2 = tip_1.strip('%')
tip_percentage = float(tip_2)

tip = (tip_percentage * total_bill)/100

print(tip)

payable = total_bill + tip

print(payable)

each_person = round((payable/number_of_people), 1)

print(each_person)

print(f'Each person should pay: ${each_person}')

