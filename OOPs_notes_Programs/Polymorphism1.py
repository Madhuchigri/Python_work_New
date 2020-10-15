# Overriding and Super() Method

class Employee:

    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40


    def display_number_working_hours(self):
        print("Number of working hours for an employee:", self.numberofworkinghours)


class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45 # Overriding the value

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours() # super method helps in resetting value back


employee = Employee()
employee.setnumberofworkinghours()
employee.display_number_working_hours()
trainee = Trainee()
trainee.setnumberofworkinghours()
trainee.display_number_working_hours()
print("Number of working hours of a trainee after the reset:", end = '')
trainee.resetnumberofworkinghours()
trainee.display_number_working_hours()

