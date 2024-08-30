"Program to convert the students score to corresponding grade"

student_data = {
    'Harry': 81,
    'Ron': 79,
    'Harmione': 98,
    'Neville': 60,
    'Malfoy': 35,
    'Draco': 70,
}

# print(student_data)

grades = {}
for name in student_data:
    # print(name)
    if student_data[name] >= 91:
        grades[name] = 'outstanding'
    elif 90 >= student_data[name] >= 81:
        grades[name] = 'Exceeds Expectations'
    elif 80 >= student_data[name] >= 70:
        grades[name] = 'Acceptable'
    else:
        grades[name] = 'Fail'

print(grades)

print(grades['Harry'])
