# OOP

class Employee:
    # common class attribute for all
    numberOfWorkingHour = 40


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

# set attibute
emp1.name = 'Ron'
print(emp1.name)

# it will not create same attribute for other object

print(f"emp1: {emp1.numberOfWorkingHour}\nemp2: {
      emp2.numberOfWorkingHour}\nemp3: {emp3.numberOfWorkingHour}")

# change the common attribute
Employee.numberOfWorkingHour = 50
print(f"emp1: {emp1.numberOfWorkingHour}\nemp2: {
      emp2.numberOfWorkingHour}\nemp3: {emp3.numberOfWorkingHour}")

# change class attributes
emp1.numberOfWorkingHour = 40
print(emp1.numberOfWorkingHour)
# it changes only for emp1, emp2 will remain same

print(emp2.numberOfWorkingHour)
