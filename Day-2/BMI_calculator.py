"the formula of calculating BMI = weight(kg)/squre of height(m^2)"

height = float(input("Input height in meter: \n"))
weight = float(input("Input weight in kilogram (kg): \n"))

BMI = int(weight/(height*height))

print(f"Your BMI is {BMI}")
