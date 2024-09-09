# polymorphism

class Employee:
    def __init__(self):
        self.workingHours = 40

    def display_working_hours(self):
        print(self.workingHours)


class Trainee(Employee):
    def __init__(self):
        super().__init__()
        self.workingHours = 30


employee = Employee()
print(f'Number of working hours for employee: {employee.workingHours}')

trainee = Trainee()
print(f'Number of working hours for trainee: {trainee.workingHours}')
