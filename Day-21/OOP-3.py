class Employee:
    # instance method
    def employeeDetails(self):
        self.name = 'Naruto'

    # static method
    @staticmethod
    def Greetings():
        print('Welcome to our Orgenization.')


emp = Employee()
emp.employeeDetails()
# print(emp.name)

emp.Greetings()
