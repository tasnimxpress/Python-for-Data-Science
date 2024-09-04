# complete OOP

# class
class Employee():

    # initializer
    def __init__(self, emp_name, emp_designation):
        self.name = emp_name
        self.degignation = emp_designation
        self.salesMade = 6

    # method
    def achived_target(self, sales):
        if self.salesMade <= sales:
            return ('Target achived')
        else:
            return ('Not achived')


# check if employee achived target
employee1 = Employee('ben', 'Sales Executive')
print(employee1.name)

parformance = employee1.achived_target(10)
print(parformance)

employee2 = Employee('Harry', 'Manager')
print(employee2.name)
parformance2 = employee2.achived_target(4)
print(parformance2)
