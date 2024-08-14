"This calculator will divide money in equal"

Greeting = "Welcome to the tip calculator."

print(Greeting)

bill = input("Please enter your bill: \n")
tips = input("What percentage of tip you want to give?\n")
persons = input("How many people to split the bill?\n")

bill = bill.strip("$")
tips = tips.strip("%")

bill_count = float(bill)
tip_count = float(tips)

given_tips = bill_count * tip_count / 100
total_person = int(persons)

bill_with_tip = bill_count + given_tips
result = bill_with_tip / total_person

print(f"Each person should pay: ${result}")
