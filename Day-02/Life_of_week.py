"""A year is counted by 52.176 week, 
and a person who lived 90 years, has spend 4000 week. 
This program will calculate how many weeks you have left by your age.
The formula is - Age in weeks = Age in years × 52.176"""

"We are being optimistic about life expectancy of 90 years."
total_week = 90 * 52.176

age = input("Your age:\n")
age = int(age)

spend_week = age * 52.176
left_week = int(total_week - spend_week)

print(f"You have {left_week} weeks left.")
